from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import cv2
from video_stream import VideoStream


class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()

        # Create a central widget for the main window
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a QVBoxLayout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create a VideoStream widget and add it to the layout
        self.video_stream = VideoStream()
        layout.addWidget(self.video_stream)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

        # Open a video capture device
        self.cap = cv2.VideoCapture(0)

        # Start the video stream
        self.start_video_stream()



    def start_video_stream(self):
        """
        Start the video stream by reading frames from the video capture device and displaying them in the VideoStream widget.
        """
        ret, frame = self.cap.read()

        if ret:
            self.video_stream.update_frame(frame)
      
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        
        # Call this method again after a delay
        self.timer = self.startTimer(int(fps))



    def timerEvent(self, event):
        """
        Called when the timer set in start_video_stream() triggers.

        :param event: A QTimerEvent object.
        """
        self.start_video_stream()


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()

