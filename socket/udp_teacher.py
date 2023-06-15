import socket
import threading
import cv2 
import numpy as np


class UdpTeacher:
    def __init__(self, **kwargs):
        self.PORT = kwargs['port']
        self.clients = kwargs['clients']
        self.token = kwargs['token']
        self.max_clients = kwargs['max_clients']

        # define a udp server listener for a further udp communication
        self.udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # auth state flag 
        self.auth_flag = True 



    def auth_students(self):
        '''This funciton authenticate students and adds them to the clients list'''
        
        print('Authenticating...')

        self.udp_sock.bind(('0.0.0.0', self.PORT))

        print(self.udp_sock.getsockname()[1])


        # while authentcating 
        while self.auth_flag:

            # message will contain the user's full name and the token for auth 
            msg, address = self.udp_sock.recvfrom(1024)
             
            try:
                # unpack name and token
                name, token = tuple(msg.decode().strip().split(', '))
            except:
                continue

            # init response message
            response = b'AUTH_FAILED'
            
            # auth completed 
            if token == self.token:     
                response = b'AUTH_SUCCESS'
     
                # add client's ip to clients list 
                self.clients.append(str(address[1]))           
               
                if self.max_clients == len(self.clients):
                    self.auth_flag = False

            self.udp_sock.sendto(response, address)
            

        # stopped auth, now get camera stream
        self.clients_info(0, 2)


    def terminate(self):
        ''' This funciton terminates the server and sends 
            an allerting message tp the clients before'''
        
        for client in self.clients:
            self.udp_sock.send(b"TEST_FINISHIED", (client[index], 8081))
            
        self.udp_sock.close()



    def get_screenshot(self, index):
        ''' This function gets a screenshot from the client '''
        address = (self.clients[index], 8081)
        self.udp_sock.sendto(b"GET_SCREENSHOT", address)



    def start_video_stream(self, index):
        ''' This fucntion starts getting a camera video stream from 
            the client'''
        address = (self.clients[index], 8081)
        print("sending to ", address)
        self.udp_sock.sendto(b"GET_FRAMES", address)



    def stop_video_stream(self, index):
        ''' This function asks the client to stop the video stream  '''
        
        address = (self.clients[index], 8081)
        print("sending to ", address)
        self.udp_sock.sendto(b"STOP_VIDEO_STREAM", address)
   
    

    def clients_info(self, start_ind, end_ind):
        ''' This funciton gets the client screenshots & 
            video streams for a given start & end indices in the 
            clients list'''

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

        frame_data = b''

        # Continuously receive video frame chunks over UDP and accumulate them into frames
        while True:
        
            for i in range(chunks_num): 
                
                # Receive a chunk of data over UDP
                data, addr = self.udp_sock.recvfrom(CHUNK_SIZE)

                # accumulate data
                frame_data += data
                
            
            try:
                # read image as an numpy array
                image = np.asarray(bytearray(frame_data), dtype="uint8")
                
                # use imdecode function
                frame = cv2.imdecode(image, cv2.IMREAD_COLOR)

                # display image
                cv2.imshow('Received', frame)
               
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            
            except Exception as e:
                continue

            # zero frame data
            frame_data = b''
               


if __name__ == '__main__':
    server = UdpTeacher(port=8080, token='ABC123', max_clients=2, clients=['127.0.0.1', '192.168.5.228'])
    server.clients_info(0, 2)
