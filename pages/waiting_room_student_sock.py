import resources
from PyQt5 import QtCore, QtGui, QtWidgets

from waiting_room_student import Ui_Form as WaitingRoomStudent
from image_stream import ImageStream

import sys
sys.path.append('./../socket/')
from tcp_student import TcpStudent

import socket
import threading
import cv2 
import numpy as np



class WaitingRoomStudentSock(TcpStudent, WaitingRoomStudent):
    ''' This class inherits from the WaitingRoomStudent class which is responsible for 
        the Gui of the student's waiting room in Pyqt, and from TcpStudent that is reponsible for 
        the backend of the student's waiting room.'''


    def __init__(self, **kwargs):
        
        # init tcp socket 
        TcpStudent.__init__(self, **kwargs)
        
        # init pyqt gui
        WaitingRoomStudent.__init__(self)
 
        # while in waiting room
        self.camera_streaming = True

        # Open a video capture device
        self.cap = cv2.VideoCapture(0)


    def setup_camera_slot(self):
        ''' this function setups the slot of the camera stream'''

        # add Imagestreams inside the slots

        width = 480
        height = 400
        

        self.cam = ImageStream(self.camera_frame, width, height)
        self.cam.setMinimumSize(width, height)
   


    def show_camera_stream(self):
        ''' This function shows the student's it's camera stream ''' 
        while self.camera_streaming:
            
            ret, frame = self.cap.read()
        
            if ret:
                self.cam.update_frame(frame)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    # run gui
    integrated_obj = WaitingRoomStudentSock(server_port=8080, host='localhost', token='ABC123', fullname=sys.argv[1] + " " + sys.argv[2])
    
    # Connect to tcp server for authentication
    integrated_obj.connect()
    


    integrated_obj.setupUi(Form)
    integrated_obj.setup_camera_slot()
   

    stream_thread = threading.Thread(target=integrated_obj.show_camera_stream, daemon=True) 
    Form.show()
    stream_thread.start() 
    
    sys.exit(app.exec_())
    self.camera_streaming = False
