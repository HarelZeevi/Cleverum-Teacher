import cv2
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class ImageStream(QWidget):
    """
    A PyQt widget for displaying a live video stream & screenshots from an OpenCV video capture device.

    The widget shows the frames in a QLabel widget,
    which can be resized to match the size of the frame.

    Parameters:
        parent (QWidget): The parent widget for this widget. Default is None.
    """
    def __init__(self, parent, width, height):
        super(ImageStream, self).__init__(parent)

        # Set the video size to be displayed
        self.video_size = (width, height)

        # Initialize the UI
        self.init_ui()



    def init_ui(self):
        """
        Initialize the UI for the widget.

        This method creates a QVBoxLayout to add the QLabel widget to,
        and creates a QFrame widget to hold the QLabel widget.
        """
        # Create a QVBoxLayout to add the QLabel to
        layout = QVBoxLayout(self)

        # Create a QFrame to hold the video frame
        self.video_frame = QFrame(self)
        self.video_frame.setFrameShape(QFrame.Panel)
        self.video_frame.setFrameShadow(QFrame.Sunken)
        layout.addWidget(self.video_frame)

        # Create a QLabel widget to show the video frames
        self.video_label = QLabel(self.video_frame)
        self.video_label.resize(self.video_size[0], self.video_size[1])
 
        # creating a QGraphicsDropShadowEffect object
        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(15)
        shadow1.setOffset(4, 4)
        shadow1.setColor(Qt.black)
        self.video_label.setGraphicsEffect(shadow1)
        
        self.video_label.setStyleSheet("QFrame{\n"
    "    border-style: outset;\n"
    "    border-width: 2px;\n"
    "    border-radius: 5px;\n"
    "    border-color: black;\n"
    "}")

        layout.addWidget(self.video_label)

        # setting blur radius   
        #shadow.setBlurRadius(15)

        # adding shadow to the label

        self.setLayout(layout)



    def update_frame(self, frame):
        """
        Update the video frame shown in the widget.

        Parameters:
            frame (numpy.ndarray): A numpy array containing the video
            frame to be displayed. The array should 
            have shape (height, width, channels).
        """
        # Resize the frame to match the video size
        frame = cv2.resize(frame, self.video_size)

        # Convert the frame to RGB and create a QImage from it
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        qimage = QImage(frame_rgb.data, self.video_size[0], self.video_size[1], QImage.Format_RGB888)

        # Set the QImage as the QPixmap of the QLabel
        pixmap = QPixmap.fromImage(qimage)
        self.video_label.setPixmap(pixmap)

