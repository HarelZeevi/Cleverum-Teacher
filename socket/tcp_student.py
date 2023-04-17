import socket
import sys

class TcpStudent:
    def __init__(self, **kwargs):
        self.PORT = kwargs['server_port']

        self.fullname = kwargs['fullname']
        self.HOST = kwargs['host']
        self.token = kwargs['token']

        # define a tcp socket 
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
       
    
    def connect(self):
        ''' This function connects to a remote socket server 
            and authenticate using the token'''
        
        self.sock.connect((self.HOST, self.PORT))
        auth_info = f'{self.token},{self.fullname}'
        print("connected")
        
        self.sock.send(auth_info.encode())
        
        data = self.sock.recv(1024) 

        self.sock.close()



  

if __name__ == '__main__':
    print(sys.argv[1] + " " + sys.argv[2])
    client = TcpStudent(server_port=8080, host='localhost', token='ABC123', fullname=sys.argv[1] + " " + sys.argv[2])

