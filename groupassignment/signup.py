# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class SignupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.save_user_and_open_login)
        self.ui.pushButton.clicked.connect(self.clear_fields)
        self.ui.pushButton_3.clicked.connect(self.go_to_login)

    def go_to_login(self):
        from loginpage import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    def clear_fields(self):
        self.ui.textEdit_4.clear()  # First Name
        self.ui.textEdit_3.clear()  # Last Name
        self.ui.textEdit_5.clear()  # Email
        self.ui.textEdit_6.clear()  # Password
        self.ui.spinBox.setValue(0)  # Age

    def save_user_and_open_login(self):
        firstname = self.ui.textEdit_4.toPlainText().strip()  # First Name
        lastname = self.ui.textEdit_3.toPlainText().strip()   # Last Name
        password = self.ui.textEdit_6.toPlainText().strip()   # Password
        email = self.ui.textEdit_5.toPlainText().strip()
        age = self.ui.spinBox.value()

        if age < 18:
            QMessageBox.warning(self, "Age Restriction", "Users must be 18 and above to sign up")
            return
        if not firstname or not lastname or not password or not email:
            QMessageBox.warning(self, "Incomplete", "Please fill in all fields")
            return

        username = firstname + lastname
        with open("users.txt", "a") as file:
            file.write(f"\n{username},{password},{email}\n")

        QMessageBox.information(self, "Registered", "Account created! Continue to login page")

        from loginpage import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(380, 30, 351, 61))
        self.textEdit_4.setObjectName("textEdit_4")  # First Name

        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(380, 100, 351, 61))
        self.textEdit_3.setObjectName("textEdit_3")  # Last Name

        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(380, 310, 351, 61))
        self.textEdit_5.setObjectName("textEdit_5")  # Email

        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(380, 240, 351, 61))
        self.textEdit_6.setObjectName("textEdit_6")  # Password

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        labels = ["Email", "Password", "Age", "Last Name", "First Name"]
        positions = [310, 250, 180, 100, 30]
        for i, (text, y) in enumerate(zip(labels, positions)):
            label = QtWidgets.QLabel(self.centralwidget)
            label.setGeometry(QtCore.QRect(190, y, 181, 51))
            label.setFont(font)
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setText(text)
            setattr(self, f"label_{i+1}", label)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 400, 181, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Clear")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 400, 181, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Continue")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 470, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("I have an account")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(380, 170, 351, 61))
        self.spinBox.setObjectName("spinBox")  # Age

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.label_6.setPixmap(QtGui.QPixmap("C:/xampp/htdocs/argriculture/images/background.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")

        self.label_6.lower()
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        # center align all text
        self.textEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_6.setAlignment(QtCore.Qt.AlignCenter)

        self.textEdit_4.setStyleSheet("QTextEdit { padding-top: 15px; }")
        self.textEdit_3.setStyleSheet("QTextEdit { padding-top: 15px; }")
        self.textEdit_5.setStyleSheet("QTextEdit { padding-top: 15px; }")
        self.textEdit_6.setStyleSheet("QTextEdit { padding-top: 15px; }")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SignupWindow()
    window.show()
    sys.exit(app.exec_())
