import socket
import threading
import cv2 
import struct
import numpy as np 


class Client:
    def __init__(self, **kwargs):
        self.TCP_PORT = kwargs['tcp_port']
        self.UDP_PORT = kwargs['udp_port']

        self.fullname = kwargs['fullname']
        self.HOST = kwargs['host']
        self.token = kwargs['token']

        # define a tcp socket 
        self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        
        # define a udp server listener for a further udp communication
        self.udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.udp_thread = threading.Thread(target=self.start_udp)
        self.udp_thread.start()

       
        # Connect to tcp server for authentication
        self.connect()



    def start_udp(self):
        ''' This function fires up a udp server listener '''

        # bind the server 
        self.udp_sock.bind((self.HOST, self.UDP_PORT))
        print(f'[UDP Server at {self.HOST}:{self.UDP_PORT} is Active]...')

        # starting video streaming
        stream_thread = threading.Thread(target=self.start_video_stream, daemon=True)
        stream_thread.start()

        while True:
            # listener that recieves commands from server
            command = self.udp_sock.recvfrom(1024)
            print("command: ", command)
  
         

    def connect(self):
        ''' This function connects to a remote socket server 
            and authenticate using the token'''
        
        self.tcp_sock.connect((self.HOST, self.TCP_PORT))
        auth_info = f'{self.token},{self.fullname}'
        print("connected")
        
        self.tcp_sock.send(auth_info.encode())
        
        data = self.tcp_sock.recv(1024)
        print(data) 
        self.udp_client_addr = (self.HOST, int(data.decode()))

        self.tcp_sock.close()



    def listen(self):
        ''' Listen from incomming requests from the server
            and send send the route it to the different methods'''
        pass


    
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

        # Loop to read frames from the camera and send them to the UDP socket
        while True:

            # Capture a frame from the camera
            ret, frame = cap.read()

            # Convert the frame to a byte array
            data = cv2.imencode('.jpg', frame)[1].tobytes()

            # Send the data in chunks over UDP
            num_chunks = len(data) // CHUNK_SIZE + 1
           
            # sending number of chunks 
            self.udp_sock.sendto(str(num_chunks).encode(), (self.HOST, self.TCP_PORT))               
            

            for i in range(num_chunks):
                print(len(data))
                end = min((i + 1) * CHUNK_SIZE + 1, len(data))
                print(end)
                chunk = data[i * CHUNK_SIZE: end]
                self.udp_sock.sendto(chunk, (self.HOST, self.TCP_PORT))               
            
       
        # Release the camera and close the UDP socket
        cap.release()
        
        cv2.destroyAllWindows()



    def stop_video_stream(self):
        '''This function stops streaming video to the server'''
        pass        



    def send_info(start_ind, end_ind):
        ''' This funciton sends the client screenshots & 
            video streams'''

        pass



    def auth(self):
        ''' This function authenticate the client with the token
            if the token sent to the server is correct the auth will be
            deon successfully'''
    

if __name__ == '__main__':
    client = Client(tcp_port=8080, udp_port=8081, host='localhost', token='ABC123', fullname='Harel Zeevi')
