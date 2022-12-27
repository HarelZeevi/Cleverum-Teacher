import register
import sign_in
from PyQt5 import QtCore, QtWidgets
import sys
import time 


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = sign_in.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    ui = register.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()