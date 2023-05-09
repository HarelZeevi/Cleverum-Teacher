import socket
import threading


class TcpTeacher:
    def __init__(self, **kwargs):
        self.PORT = kwargs['port']
        self.clients = []
        self.token = kwargs['token']
        self.max_clients = kwargs['max_clients']

        # creating a tcp socket for clients list 
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('0.0.0.0', self.PORT))


    def run(self):
        ''' This function gets runs the server '''
        self.sock.listen(9)
        
        print("[server is listening]...")
        while True:
            client, address = self.sock.accept()
            
            #client.settimeout(60)
            t = threading.Thread(target = self.handle_client, daemon=True, args=(client, address))
            t.start()
           
            # reached maximum clients - start getting info
            if len(self.clients) == self.max_clients:
                print("[Reached Clients Limit. Server Stopped]....")
                self.sock.close()
                return          

       


    def handle_client(self, client, address):
        ''' This funciton handles a new incomming client '''
 
        data = client.recv(1024)
        
        if data:
            # unpack data saperated by comma 
            token, fullname = data.decode().split(',')
           
            # check if authentication was passed successflly
            self.client_auth(address, client, token)
        
        else:
            print('Client disconnected')
   


    def terminate(self):
        ''' This funciton terminates the server and sends 
            an allerting message tp the clients before'''
        print("terminating") 
        
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()




    def client_auth(self, address, client, token):
        ''' This function authenticate an incomming client
            asks for its token, and check if the token is correct'''
   
        # check the client's token
        if self.token == token:
           
            # append address to clients
            self.clients.append(address[0])

        else:
            client.send(b'AUTH_FAILED')
        



if __name__ == '__main__':
    server = TcpTeacher(port=8080, token='ABC123', max_clients=40)
    server.run()
