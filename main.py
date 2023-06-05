# -*- coding: utf-8 -*-

# Form impementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import resources
import threading 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout

# for http requests
import requests
import json

import math
import sys

sys.path.append('./pages/')
from register import Register
from sign_in import Login


class Ui_MainWindow(object):
   
    def __init__(self):
        self.PAGE_SIZES = {
            0: (1040, 681),
            1: (1040, 681),
            2: (1374, 824),
            3: (1456, 691)
            }


    def changeWidget(self, index):

        self.main.setFixedSize(*self.PAGE_SIZES[index])
        self.main.resize(QtCore.QSize(*self.PAGE_SIZES[index]))
         

    def setupUi(self, MainWindow):
        self.main = MainWindow 
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Cleverum")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.resize(1040, 681)
        self.nextSize = 0
        self.centralwidget.setObjectName("centralwidget")
        
        # define the stack of widgets 
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        print(self.stackedWidget.geometry()) 

        # Connect the currentChanged signal to the changeWidget method
        self.stackedWidget.currentChanged.connect(self.changeWidget)
        
        ''' Here we define the imported pages and add them to the stack of widgets'''
        
        # login page 
        self.login = QtWidgets.QWidget()
        ui = Login()
        ui.setupUi(self.login, self.stackedWidget)
        self.login.setObjectName("login")
        self.stackedWidget.addWidget(self.login)

        # Update the background of the main window to be the background color of the current frame's stylesheet
        #current_widget = self.stackedWidget.currentWidget()
        #background_color = current_widget.styleSheet().split(":")[-1].strip()
        #self.centralwidget.setStyleSheet("background-color: " + background_color + ";")
    
        # register page 
        self.register = QtWidgets.QWidget()
        ui = Register()
        ui.setupUi(self.register, self.stackedWidget)
        self.register.setObjectName("register")
        self.stackedWidget.addWidget(self.register)
              
        MainWindow.setCentralWidget(self.stackedWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
