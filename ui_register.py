# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1040, 682)
        MainWindow.setMinimumSize(QSize(1040, 682))
        MainWindow.setMaximumSize(QSize(1040, 682))
        font = QFont()
        font.setFamily(u"Rekha")
        font.setPointSize(30)
        font.setItalic(False)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color:#2C2F33;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(420, 530, 121, 41))
        font1 = QFont()
        font1.setFamily(u"DejaVu Sans")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setKerning(False)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #FED049;\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-radius: 10px;\n"
"	border-color: beige;\n"
"	padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"		background-color: #7289DA;\n"
"}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 110, 181, 51))
        font2 = QFont()
        font2.setFamily(u"Sitka Text")
        font2.setPointSize(26)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: white;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(790, 430, 250, 246))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(150, 180, 681, 311))
        self.frame_2.setStyleSheet(u"background-color: #23272A;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QComboBox { background-color: green; }")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        font3 = QFont()
        font3.setPointSize(13)
        self.comboBox_2.setFont(font3)
        self.comboBox_2.setStyleSheet(u"color:white;")

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font3)
        self.comboBox.setStyleSheet(u"color:white;\n"
"border-color:green;")

        self.horizontalLayout.addWidget(self.comboBox)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        font4 = QFont()
        font4.setPointSize(14)
        self.lineEdit_2.setFont(font4)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	color:white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1px solid rgb(170, 255, 0)  ;\n"
"}")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit_2, 6, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font4)
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"	color:white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1px solid rgb(170, 255, 0)  ;\n"
"}")

        self.gridLayout.addWidget(self.lineEdit_4, 2, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font4)
        self.lineEdit_6.setStyleSheet(u"QLineEdit{\n"
"	color:white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1px solid rgb(170, 255, 0)  ;\n"
"}")

        self.gridLayout.addWidget(self.lineEdit_6, 4, 1, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        font5 = QFont()
        font5.setFamily(u"padmaa")
        font5.setPointSize(13)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font4)
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"	color:white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1px solid rgb(170, 255, 0)  ;\n"
"}")

        self.gridLayout.addWidget(self.lineEdit_5, 4, 0, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        font6 = QFont()
        font6.setFamily(u"padmaa")
        font6.setPointSize(13)
        font6.setBold(False)
        font6.setWeight(50)
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font4)
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	color:white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1px solid rgb(170, 255, 0)  ;\n"
"}")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit_3, 6, 1, 1, 1)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"color:white;")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font4)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	color:white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1px solid rgb(170, 255, 0)  ;\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.label_4.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit_3.raise_()
        self.label_5.raise_()
        self.lineEdit_4.raise_()
        self.label_6.raise_()
        self.lineEdit_5.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.lineEdit_6.raise_()
        self.frame_2.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"SUBMIT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/bg/learn1.png\"/></p></body></html>", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"---Select Role---", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Teacher", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Student", None))
        self.comboBox_2.setItemText(3, "")

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"---Select Gender---", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Male", None))
        self.comboBox.setItemText(3, "")

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.lineEdit_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"First name", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_3.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ID", None))
    # retranslateUi

