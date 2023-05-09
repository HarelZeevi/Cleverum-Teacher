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
   
    def __init__(self, **kwargs):
        
        # init udp ocket 
        UdpTeacher.__init__(self, **kwargs)
        
        # init pyqt gui
        TestPanel.__init__(self)
        

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

        self.udp_sock.bind(('0.0.0.0', self.PORT))
        
        # check boundaries
        if start_ind < 0 or end_ind > len(self.clients):
            print('Indices out of bounds')
            return 
        
        # unpack client
        for i in range(start_ind, end_ind): 
            client_thread = threading.Thread(target = self.start_video_stream, daemon=True, args=(i, ))
            client_thread.start()

        # Define the chunk size (in bytes)
        CHUNK_SIZE = 65506

        # Receive the number of chunks
        chunks_num, addr = self.udp_sock.recvfrom(CHUNK_SIZE)
        chunks_num = int(chunks_num.decode())
        print("Chunks for ", addr, ": ", chunks_num)
        frame_data = b''
 
        input("Should we Start?")
        
        # Continuously receive video frame chunks over UDP and accumulate them into frames
        while True:
        
            for i in range(chunks_num): 
                
                # Receive a chunk of data over UDP
                data, addr = self.udp_sock.recvfrom(CHUNK_SIZE)
                
                print("data", data)

                # accumulate data
                frame_data += data
               
            print(frame_data)
            
            try:
                # read image as an numpy array
                image = np.asarray(bytearray(frame_data), dtype="uint8")
                
                # use imdecode function
                frame = cv2.imdecode(image, cv2.IMREAD_COLOR)
                
                print(frame)
                if addr == self.clients[start_ind]:
                    self.cam1.update_frame(frame)
                
                else:
                    self.cam2.update_frame(frame)

                # display image
                #cv2.imshow('Received', frame)
               
                #if cv2.waitKey(1) & 0xFF == ord('q'):
                #    break
            
            except Exception as e:
                print(e)
    
            # zero frame data
            frame_data = b''
               






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    # run gui
    integrated_obj = TestPanelSock(port=8080, token='ABC123', max_clients=2, clients=['127.0.0.1', '147.235.200.89'])
    integrated_obj.setupUi(Form)
    integrated_obj.setup_slots()

    # run udp server
    t_server = threading.Thread(target=integrated_obj.clients_info, daemon=True, args=(0, 2))
    t_server.start()

    Form.show()
   
    sys.exit(app.exec_())

