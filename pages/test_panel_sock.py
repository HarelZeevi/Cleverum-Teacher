import resources
from PyQt5 import QtCore, QtGui, QtWidgets

from test_panel import TestPanel
from image_stream import ImageStream

import sys
sys.path.append('./socket/')
from udp_teacher import UdpTeacher

import socket
import threading
import cv2 
import numpy as np
import time


class TestPanelSock(TestPanel, UdpTeacher):
    ''' This class inherits from the TestPanel class which is responsible for 
        the Gui of the test in Pyqt, and from UdpTeacher that is reponsible for 
        the backend of the test panel.'''
   
    def __init__(self, test_id, access_token, time, **kwargs):
        
        # init udp ocket 
        UdpTeacher.__init__(self, **kwargs)
        
        # init pyqt gui
        TestPanel.__init__(self, test_id, access_token, time)



    def setup_slots(self):
        ''' this function setups the slots of the camera
            streams and screenshots'''

        # add Imagestreams inside the slots

        width = 240
        height = 200
        

        self.cam1 = ImageStream(self.camera1, width, height)
        self.cam1.setMinimumSize(width, height)
       
        self.cam2 = ImageStream(self.camera2, width, height)     
        self.cam2.setMinimumSize(width, height)


        width = 280
        height = 200
        
        self.sh1 = ImageStream(self.screenshot1, width, height)     
        self.sh1.setMinimumSize(width, height)       

        self.sh2 = ImageStream(self.screenshot2, width, height)     
        self.sh2.setMinimumSize(width, height)
        



    def refresh_screenshot(self):
        ''' This funciton sends a screenshot-refresh request to both 
            of the students that appear on the screen'''
        # sending get screenshot to each client
        print("\n\n\n\n\nrefreshing\n\n\n\n\n\n")
        for i in range(2):
            addr = (self.clients[i], 8081)
            self.udp_sock.sendto(b"GET_SCREENSHOT", addr)



    def clients_info(self, start_ind, end_ind):
        ''' This funciton gets the client screenshots & 
            video streams for a given start & end indices in the 
            clients list'''

        print(self.clients)
      
        '''
        # Load image as cv2 frame
        img1 = cv2.imread('/home/harel/Pictures/img1.png')
        img2 = cv2.imread('/home/harel/Pictures/img2.png')

        self.sh1.update_frame(img1)

        self.sh2.update_frame(img2)
        '''

        # check boundaries
        if start_ind < 0 or end_ind > len(self.clients):
            print('Indices out of bounds')
            return 
        
        # unpack client
        for i in range(start_ind, end_ind): 
            client_thread = threading.Thread(target = self.start_video_stream, daemon=True, args=(i, ))
            client_thread.start()

        # Define the chunk size (in bytes)
        CHUNK_SIZE = 65509

        # Receive the number of chunks
        chunks_num, addr = self.udp_sock.recvfrom(CHUNK_SIZE)
        chunks_num = int(chunks_num.decode())
        frame_data = b''
  
        last_sender = addr
        # Continuously receive video frame chunks over UDP and accumulate them into frames
        while True:
        
            for i in range(chunks_num): 
                
                # Receive a chunk of data over UDP
                data, addr = self.udp_sock.recvfrom(CHUNK_SIZE)
                
                # accumulate data
                frame_data += data
                
            try:

                header = frame_data[0:6].decode()
                isScreenshot = False
                
                print(header)
                if "scr" in header:
                    isScreenshot = True
                    print("received screenshot")

                # rest of the frame 
                frame_data = frame_data[6:]

                # read image as an numpy array
                image = np.asarray(bytearray(frame_data), dtype="uint8")
                
                # use imdecode function
                frame = cv2.imdecode(image, cv2.IMREAD_COLOR)
                
                if addr[0] == self.clients[start_ind]:
                    self.cam1.update_frame(frame)

                    if isScreenshot:
                        self.sh1.update_frame(frame)


                elif addr[0] == self.clients[start_ind + 1]:
                    self.cam2.update_frame(frame)

                    if isScreenshot:
                        self.sh2.update_frame(frame)
                

                # display image
                #cv2.imshow('Received', frame)
               
                #if cv2.waitKey(1) & 0xFF == ord('q'):
                #    break
            
            except Exception as e:
                #continue
                a = 1
    
            # zero frame data
            frame_data = b''
               






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    # run gui
    integrated_obj = TestPanelSock(port=8080, token='ABC123', max_clients=2, clients=['127.0.0.1', '192.168.5.228'])
    integrated_obj.setupUi(Form)
    integrated_obj.setup_slots()

    # run udp server
    t_server = threading.Thread(target=integrated_obj.clients_info, daemon=True, args=(0, 2))
    t_server.start()

    Form.show()
   
    sys.exit(app.exec_())

