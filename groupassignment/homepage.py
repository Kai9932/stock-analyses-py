from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from searchpage import SearchPage

class homepage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Page")
        self.setGeometry(100, 100, 600, 400)
        label = QtWidgets.QLabel("Welcome to the Home Page!", self)
        label.move(50, 50)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 500, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 360, 131, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 141, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../xampp/htdocs/argriculture/images/members.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 290, 131, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 251, 581))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 220, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 950, 151, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(550, 880, 131, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(550, 830, 131, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(550, 780, 131, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 650, 131, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(550, 730, 131, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 231, 31))
        self.label_2.setObjectName("label_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(320, 200, 431, 331))
        self.calendarWidget.setObjectName("calendarWidget")
        self.textEdit.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.label_4.raise_()
        self.pushButton_10.raise_()
        self.pushButton_4.raise_()
        self.pushButton.raise_()
        self.pushButton_5.raise_()
        self.label_2.raise_()
        self.calendarWidget.raise_()
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Logout"))
        self.pushButton_5.setText(_translate("MainWindow", "Settings"))
        self.pushButton_4.setText(_translate("MainWindow", "Search"))
        self.pushButton_2.setText(_translate("MainWindow", "Home"))
        self.pushButton_6.setText(_translate("MainWindow", "Logout"))
        self.pushButton_7.setText(_translate("MainWindow", "Settings"))
        self.pushButton_8.setText(_translate("MainWindow", "Search"))
        self.pushButton_9.setText(_translate("MainWindow", "Shopping"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_10.setText(_translate("MainWindow", "Home"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))

class HomePage(QtWidgets.QMainWindow):
    def __init__(self, username=None):
        super().__init__()
        self.username = username  # ✅ Store username from login
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Hide Settings buttons
        self.ui.pushButton_5.hide()
        self.ui.pushButton_7.hide()

        # Welcome label
        if username:
            self.ui.label_2.setText(f"Good morning, {username}")
            self.ui.label_2.setAlignment(QtCore.Qt.AlignCenter)

        # Connect buttons
        self.ui.pushButton_9.clicked.connect(self.open_searchpage)
        self.ui.pushButton_4.clicked.connect(self.open_searchpage)
        self.ui.pushButton.clicked.connect(self.logout)

    def open_searchpage(self):
        self.search_window = SearchPage(username=self.username)
        self.search_window.show()
        self.close()

    def logout(self):
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = HomePage()
    window.show()
    sys.exit(app.exec_())