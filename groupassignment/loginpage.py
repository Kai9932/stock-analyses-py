# loginpage.py

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import os
from homepage import HomePage
from signup import SignupWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 834)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Left image
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 461, 791))
        self.label.setPixmap(QtGui.QPixmap("D:/User Files/Downloads/ChatGPT Image Jun 8, 2025, 09_25_36 PM.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # Password input
        self.textEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(490, 480, 281, 40))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textEdit_3.setAlignment(QtCore.Qt.AlignCenter)

        # Username input
        self.textEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(490, 370, 281, 40))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.setAlignment(QtCore.Qt.AlignCenter)

        # Login button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 700, 121, 41))
        self.pushButton.setObjectName("pushButton")

        # Sign Up button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 700, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        # Top-right image
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 0, 341, 281))
        self.label_2.setPixmap(QtGui.QPixmap("D:/User Files/Downloads/ChatGPT Image Jun 8, 2025, 09_38_59 PM.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        # Divider lines
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(450, 0, 16, 781))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(460, 290, 341, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons
        self.pushButton.clicked.connect(lambda: self.handle_login(MainWindow))
        self.pushButton_2.clicked.connect(lambda: self.open_signup(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Page"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "Password"))
        self.textEdit_4.setPlaceholderText(_translate("MainWindow", "Username"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Sign Up"))

    def handle_login(self, login_window):
        username = self.textEdit_4.text().strip()
        password = self.textEdit_3.text().strip()

        if not username or not password:
            QMessageBox.warning(login_window, "Input Error", "Please enter both username and password.")
            return

        with open("users.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 2:
                    stored_user, stored_pass = parts[0], parts[1]
                    if username == stored_user and password == stored_pass:
                        QMessageBox.information(login_window, "Login Success", "Welcome!")
                        self.open_homepage(login_window, username)
                        return

        QMessageBox.warning(login_window, "Login Failed", "Wrong username or password.")

    def open_homepage(self, login_window, username):
        self.home_window = HomePage(username=username)
        self.home_window.show()
        login_window.close()

    def open_signup(self, login_window):
        self.signup_window = SignupWindow()
        self.signup_window.show()
        login_window.close()


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = LoginWindow()
    MainWindow.show()
    sys.exit(app.exec_())
