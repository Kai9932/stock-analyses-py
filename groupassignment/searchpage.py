# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
import yfinance as yf
import warnings
import os
warnings.filterwarnings("ignore")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 10, 141, 41))
        self.pushButton.setObjectName("pushButton")

        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 10, 621, 41))
        self.textEdit_4.setObjectName("textEdit_4")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

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

        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(10, 540, 141, 41))
        self.backButton.setText("Back")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock Predictor"))
        self.pushButton.setText(_translate("MainWindow", "Predict"))
        self.textEdit_4.setPlaceholderText(_translate("MainWindow", "Enter company ticker (e.g., AAPL)"))


class SearchPage(QtWidgets.QMainWindow):
    def __init__(self, username=None):
        super().__init__()
        self.username = username
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.run_prediction)

        self.ui.backButton.clicked.connect(self.go_back)

    def go_back(self):
        from homepage import HomePage
        self.home = HomePage(username=self.username)
        self.home.show()
        self.close()

    #ideas and method from https://www.geeksforgeeks.org/nlp/stock-price-prediction-project-using-tensorflow/
    #ideas and method from https://medium.com/@deepml1818/predicting-stock-prices-using-lstm-and-yahoo-finance-data-0e2534b269a1

    def run_prediction(self):
        user_input = self.ui.textEdit_4.toPlainText().strip().upper()
        if not user_input:
            QMessageBox.warning(self, "Input Error", "Please enter a company ticker like AAPL")
            return

        self.ui.pushButton.setEnabled(False)

        try:
            import os
            from sklearn.metrics import mean_squared_error
            import math

            # Download 5 years of data using yfinance
            company = yf.download(user_input, period="5y")
            if company.empty:
                QMessageBox.warning(self, "Data Error", f"No data found for ticker {user_input}")
                self.ui.pushButton.setEnabled(True)
                return

            company.reset_index(inplace=True)
            close_data = company[['Close']]
            dataset = close_data.values
            training_data_len = int(len(dataset) * 0.95)

            scaler = MinMaxScaler(feature_range=(0, 1))
            scaled_data = scaler.fit_transform(dataset)

            train_data = scaled_data[0:training_data_len, :]
            x_train = []
            y_train = []

            for i in range(60, len(train_data)):
                x_train.append(train_data[i - 60:i, 0])
                y_train.append(train_data[i, 0])

            x_train, y_train = np.array(x_train), np.array(y_train)
            x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

            model_filename = f"{user_input}_model.h5"
            if os.path.exists(model_filename):
                model = keras.models.load_model(model_filename)
            else:
                model = keras.models.Sequential()
                model.add(keras.layers.LSTM(units=64, return_sequences=True, input_shape=(x_train.shape[1], 1)))
                model.add(keras.layers.LSTM(units=64))
                model.add(keras.layers.Dense(32))
                model.add(keras.layers.Dropout(0.5))
                model.add(keras.layers.Dense(1))

                model.compile(optimizer='adam', loss='mean_squared_error')
                model.fit(x_train, y_train, epochs=5, verbose=0)
                model.save(model_filename)

            test_data = scaled_data[training_data_len - 60:, :]
            x_test = []
            for i in range(60, len(test_data)):
                x_test.append(test_data[i - 60:i, 0])
            x_test = np.array(x_test)
            if len(x_test) == 0:
                QMessageBox.warning(self, "Prediction Error",
                                    "Not enough data to make a prediction. Try another company.")
                self.ui.pushButton.setEnabled(True)
                return

            x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

            predictions = model.predict(x_test)
            predictions = scaler.inverse_transform(predictions)

            train = company[:training_data_len]
            test = company[training_data_len:].copy()
            test['Predictions'] = predictions

            # Calculate RMSE
            rmse = math.sqrt(mean_squared_error(test['Close'], predictions))

            # Plot the result
            plt.figure(figsize=(10, 6))
            plt.plot(train['Date'], train['Close'], label="Train")
            plt.plot(test['Date'], test['Close'], label="Test")
            plt.plot(test['Date'], test['Predictions'], label="Predicted")

            last_date = test['Date'].iloc[-1]
            last_price = test['Predictions'].iloc[-1]
            plt.annotate(
                f'Expected\n{last_price:.2f} RM',
                xy=(last_date, last_price),
                xytext=(last_date, last_price + 2),
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=9,
                ha='center',
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white')
            )

            plt.title(f"{user_input} Stock Price Prediction\nRMSE: {rmse:.2f}")
            plt.xlabel("Date")
            plt.ylabel("Price")
            plt.legend()
            plt.tight_layout()
            plt.show()

            QMessageBox.information(self, "Prediction Complete",
                                    f"Prediction finished for {user_input}.\nRMSE: {rmse:.2f}")

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        finally:
            self.ui.pushButton.setEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = SearchPage(username="testuser")
    MainWindow.show()
    sys.exit(app.exec_())
