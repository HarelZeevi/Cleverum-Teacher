import socket
import threading
import cv2

class Client:
    def __init__(self, **kwargs):
        self.PORT = kwargs['port']
        self.HOST = kwargs['host']
        self.token = kwargs['token']
       
        # define a udp server listener for a further udp communication
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
         # streaming flag
        self.streaming = False


        self.start()

       
    def start(self):
        ''' This function fires up a udp server listener '''

        # bind the server 
        self.sock.bind((self.HOST, self.PORT))
        print(f'[UDP Server at {self.HOST}:{self.PORT} is Active]...')


        # listener that recieves commands from server
        command, _  = self.sock.recvfrom(1024)
        print("command: ", command)

        # starting video streaming
        stream_thread = threading.Thread(target=self.start_video_stream, daemon=True)
        stream_thread.start()

        while True:
            # listener that recieves commands from server
            command, _  = self.sock.recvfrom(1024)
            print("command: ", command)

            self.route(command.decode())
  
         

    def route(self, command):
        ''' Listen from incomming requests from the server
            and send send the route it to the different methods'''
        
        if command == 'GET_SCREENSHOT':
            self.send_screenshot()
        

    
    def send_screenshot(self):
        ''' This function sends  a screenshot to the server'''
        pass



    def start_video_stream(self, camera_index=0):
        ''' This fucntion starts transmitting  a camera video stream to
            the server'''
        
        # Define the chunk size (in bytes)
        CHUNK_SIZE = 65506

        # Initialize the camera
        cap = cv2.VideoCapture(camera_index)
        
        # Check if the camera is working
        if not cap.isOpened():
            print("Could not open camera")
            return

        # used to record the time when we processed last frame
        prev_frame_time = 0

        # used to record the time at which we processed current frame
        new_frame_time = 0
        
        self.streaming = True

        # Loop to read frames from the camera and send them to the UDP socket
        while self.streaming:

            # Capture a frame from the camera
            ret, frame = cap.read()

            # Convert the frame to a byte array
            data = cv2.imencode('.jpg', frame)[1].tobytes()

            # Send the data in chunks over UDP
            num_chunks = len(data) // CHUNK_SIZE + 1
           
            # sending number of chunks 
            self.sock.sendto(str(num_chunks).encode(), (self.HOST, 8080))               
            

            for i in range(num_chunks):
                print(len(data))
                end = min((i + 1) * CHUNK_SIZE + 1, len(data))
                print(end)
                chunk = data[i * CHUNK_SIZE: end]
                self.sock.sendto(chunk, (self.HOST, 8080))               
            
       
        # Release the camera and close the UDP socket
        cap.release()
        
        cv2.destroyAllWindows()



    def stop_video_stream(self):
        '''This function stops streaming video to the server'''
        
        self.streaming = False



if __name__ == '__main__':
    client = Client(port=8081, host='localhost', token='ABC123')
