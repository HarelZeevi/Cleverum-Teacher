import socket
import threading
import cv2 
import numpy as np


class Server:
    def __init__(self, **kwargs):
        self.PORT = kwargs['port']
        self.HOST = '127.0.0.1'
        self.clients = []
        self.token = kwargs['token']
        self.max_clients = kwargs['max_clients']

        # creating a tcp socket for clients list 
        self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_sock.bind((self.HOST, self.PORT))

         # define a udp server listener for a further udp communication
        self.udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    def run(self):
        ''' This function gets runs the server '''
        self.tcp_sock.listen(9)
        
        print("[server is listening]...")
        while True:
            client, address = self.tcp_sock.accept()
            
            #client.settimeout(60)
            t = threading.Thread(target = self.handle_client, daemon=True, args=(client, address))
            t.start()
           
            print(len(self.clients))
            
            # reached maximum clients - start getting info
            if len(self.clients) == self.max_clients:
                print("start")
                self.clients_info(0, 1)
                return          

       


    def handle_client(self, client, address):
        ''' This funciton handles a new incomming client '''
 
        data = client.recv(1024)
        
        if data:
            # unpack data saperated by comma 
            token, fullname = data.decode().split(',')
           
            print(token)

            # check if authentication was passed successflly
            self.client_auth(address, client, token)
        
        else:
            print('Client disconnected')
   


    def terminate():
        ''' This funciton terminates the server and sends 
            an allerting message tp the clients before'''
        
        for client in self.clients:
            self.udp_sock.send(b"TEST_FINISHIED", (client[index], 8081))
            
        self..udp_sock.close()



    def get_screenshot(self, index):
        ''' This function gets a screenshot from the client '''
        address = (self.clients[index], 8081)
        self.udp_sock.sendto(b"GET_SCREENSHOT", address)



    def start_video_stream(self, index):
        ''' This fucntion starts getting a camera video stream from 
            the client'''
        address = (self.clients[index], 8081)
        self.udp_sock.sendto(b"GET_FRAMES", address)



    def stop_video_stream(self, index):
        ''' This function asks the client to stop the video stream  '''
        pass        



    def establish_udp(self, index):
        ''' This function establishes a udp conenction with a given addres
            and return it's socket '''
        pass

    

    def clients_info(self, start_ind, end_ind):
        ''' This funciton gets the client screenshots & 
            video streams for a given start & end indices in the 
            clients list'''

        print(self.clients)

        # close tcp conenction 
        self.tcp_sock.close()
        
        self.udp_sock.bind((self.HOST, self.PORT))

        print(self.udp_sock.getsockname()[1])

        # check boundaries
        if start_ind < 0 or end_ind > len(self.clients):
            print('Indices out of bounds')
            return 
        
        ''' 
        # unpack client 
        for i in range(start_ind, end_ind):
           
            client_thread = threading.Thread(target = self.start_video_stream, daemon=True, args=(i, ))
            #threading.Timer(2,display,['Timeout:'])
            client_thread.start()
        '''

        # Define the chunk size (in bytes)
        CHUNK_SIZE = 65506

        # Receive the number of chunks
        chunks_num, addr = self.udp_sock.recvfrom(CHUNK_SIZE)
        chunks_num = int(chunks_num.decode())

        frame_data = b''

        print(chunks_num)

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
                print(e)
    
            # zero frame data
            frame_data = b''
               

    def client_auth(self, address, client, token):
        ''' This function authenticate an incomming client
            asks for its token, and check if the token is correct'''
   
        # check the client's token
        if self.token == token:
           
            # append address to clients
            self.clients.append(address[0])
            client.send(f'{self.udp_sock.getsockname()[1]}'.encode())

        else:
            client.send(b'AUTH_FAILED')
        
        # close tcp connection
        client.close()



if __name__ == '__main__':
    server = Server(port=8080, token='ABC123', max_clients=1)
    server.run()
