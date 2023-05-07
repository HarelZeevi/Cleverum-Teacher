import socket
import threading

import requests
import json
import keyring
from PyQt5 import QtCore, QtGui, QtWidgets
import resources

from waiting_room_teacher import WaitingRoomTeacher

import sys
print(sys.path)
sys.path.append('./socket/')
print(sys.path)
from tcp_teacher import TcpTeacher




class WaitingRoomTeacherSock(TcpTeacher, WaitingRoomTeacher):
    ''' This class integrates the socket backend with the pyqt frontend
        and implements both classes with the combined functionality'''

    
    def __init__(self, **kwargs):
        
        # init stcp ocket 
        TcpTeacher.__init__(self, **kwargs)
        
        # init pyqt gui
        WaitingRoomTeacher.__init__(self)


    
    def handle_client(self, client, address):
        ''' This funciton handles a new incomming client '''
 
        data = client.recv(1024)
        
        if data:
            # unpack data saperated by comma 
            token, fullname = data.decode().split(',')
           
            # update gui of names
            self.names.append(fullname)
            self.update_names()

            # check if authentication was passed successflly
            self.client_auth(address, client, token)
            

            # reached maximum clients - start getting info
            if len(self.clients) == self.max_clients:
                print("get info")
                return       

        else:
            print('Client disconnected')
   

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    # run gui
    integrated_obj = WaitingRoomTeacherSock(port=8080, token='ABC123', max_clients=40)
    integrated_obj.setupUi(Form)
    integrated_obj.update_names()

    # run tcp server
    t_server = threading.Thread(target=integrated_obj.run, daemon=True)
    t_server.start()


    Form.show()
   
    sys.exit(app.exec_())
