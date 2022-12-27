# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import resources
from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 682)
        MainWindow.setMinimumSize(QtCore.QSize(1040, 682))
        MainWindow.setMaximumSize(QtCore.QSize(1040, 682))
        font = QtGui.QFont()
        font.setFamily("Rekha")
        font.setPointSize(30)
        font.setItalic(False)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:#2C2F33;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.submit_btn.setGeometry(QtCore.QRect(440, 560, 121, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.submit_btn.setFont(font)
        self.submit_btn.setStyleSheet("QPushButton{\n"
"    background-color: #FED049;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background-color: #7289DA;\n"
"        color: white;\n"
"}")
        self.submit_btn.setObjectName("submit_btn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 110, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(26)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(190, 180, 621, 311))
        self.frame_2.setStyleSheet("background-color: #23272A;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.confirmPswd = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.confirmPswd.setFont(font)
        self.confirmPswd.setStyleSheet("QLineEdit{\n"
"    color:white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(170, 255, 0)  ;\n"
"}")
        self.confirmPswd.setText("")
        self.confirmPswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPswd.setObjectName("confirmPswd")
        self.gridLayout.addWidget(self.confirmPswd, 6, 1, 1, 1)
        self.id = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.id.setFont(font)
        self.id.setStyleSheet("QLineEdit{\n"
"    color:white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(170, 255, 0)  ;\n"
"}")
        self.id.setText("")
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("padmaa")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("padmaa")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: white;")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.fname = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fname.setFont(font)
        self.fname.setStyleSheet("QLineEdit{\n"
"    color:white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(170, 255, 0)  ;\n"
"}")
        self.fname.setObjectName("fname")
        self.gridLayout.addWidget(self.fname, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("padmaa")
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: white;")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.pswd = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pswd.setFont(font)
        self.pswd.setStyleSheet("QLineEdit{\n"
"    color:white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(170, 255, 0)  ;\n"
"}")
        self.pswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pswd.setObjectName("pswd")
        self.gridLayout.addWidget(self.pswd, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("padmaa")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("padmaa")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.lname = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lname.setFont(font)
        self.lname.setStyleSheet("QLineEdit{\n"
"    color:white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(170, 255, 0)  ;\n"
"}")
        self.lname.setObjectName("lname")
        self.gridLayout.addWidget(self.lname, 2, 1, 1, 1)
        self.email = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.email.setFont(font)
        self.email.setStyleSheet("QLineEdit{\n"
"    color:white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(170, 255, 0)  ;\n"
"}")
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("padmaa")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: white;")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setStyleSheet("QComboBox { background-color: green; }")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.utype = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.utype.setFont(font)
        self.utype.setStyleSheet("color:white;")
        self.utype.setObjectName("utype")
        self.utype.addItem("")
        self.utype.addItem("")
        self.utype.addItem("")
        self.utype.addItem("")
        self.utype.setItemText(3, "")
        self.horizontalLayout.addWidget(self.utype)
        self.gender = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.gender.setFont(font)
        self.gender.setStyleSheet("color:white;\n"
"border-color:green;")
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.setItemText(3, "")
        self.horizontalLayout.addWidget(self.gender)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-130, 340, 391, 411))
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(680, 140, 591, 611))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(-120, -200, 321, 341))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(190, 500, 198, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: white;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(390, 500, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #7289da;")
        self.label_12.setObjectName("label_12")
        self.label_4.raise_()
        self.label_9.raise_()
        self.submit_btn.raise_()
        self.label_3.raise_()
        self.frame_2.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submit_btn.setText(_translate("MainWindow", "SUBMIT"))
        self.label_3.setText(_translate("MainWindow", "Register"))
        self.label_5.setText(_translate("MainWindow", "Confirm Password"))
        self.label_7.setText(_translate("MainWindow", "ID"))
        self.label_8.setText(_translate("MainWindow", "Email"))
        self.label.setText(_translate("MainWindow", "Password"))
        self.label_2.setText(_translate("MainWindow", "Last Name"))
        self.label_6.setText(_translate("MainWindow", "First name"))
        self.utype.setItemText(0, _translate("MainWindow", "---Select Role---"))
        self.utype.setItemText(1, _translate("MainWindow", "Teacher"))
        self.utype.setItemText(2, _translate("MainWindow", "Student"))
        self.gender.setItemText(0, _translate("MainWindow", "---Select Gender---"))
        self.gender.setItemText(1, _translate("MainWindow", "Female"))
        self.gender.setItemText(2, _translate("MainWindow", "Male"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/illustrations/imgs/8.png\"/></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/illustrations/imgs/3.png\"/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/bg/Beige Minimal Personal Make Up Artist Logo.png\"/><img src=\":/illustrations/imgs/11.png\"/></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Already have an account? "))
        self.label_12.setText(_translate("MainWindow", "Login here!"))

        # submit button click event hooking 
        self.submit_btn.clicked.connect(self.submit_form)

    # this function will be called when the submit button is clicked 
    def submit_form(self):
        print("hi")
        self.submit_btn.setStyleSheet("QPushButton{\n"
                                        "    background-color: #EF9A53;\n"
                                        "    color: white;\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 2px;\n"
                                        "    border-radius: 10px;\n"
                                        "    border-color: beige;\n"
                                        "    padding: 6px;\n"
                                        "}\n"
                                        "\n")
        
        PARAMS = {
                "email": self.email.text(),
                "password": self.pswd.text(),
                "confirmPassword": self.confirm_pswd.text(),
                "id": self.id.text(),
                "userType": self.utype.currentText()[0], # only the first letteris needed: S / T 
                "firstName": self.fname.text(),
                "lastName": self.lname.text(),
                "gender": self.gender.currentText()[0] # only the first letteris needed: F / M               
        }

        URL = "http://localhost:8080/api/register"
        r = requests.post(url = URL, json=PARAMS)
        print(r.text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
