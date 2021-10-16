from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import sys
import MySQLdb as mdb
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(687, 885)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Check = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Check.setGeometry(QtCore.QRect(60, 10, 131, 28))
        self.pushButton_Check.setObjectName("pushButton_Check")
        self.pushButton_Browse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Browse.setGeometry(QtCore.QRect(60, 70, 93, 28))
        self.pushButton_Browse.setObjectName("pushButton_Browse")
        self.pushButton_Chart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Chart.setGeometry(QtCore.QRect(60, 170, 93, 28))
        self.pushButton_Chart.setObjectName("pushButton_Chart")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 20, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 110, 611, 31))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        



        self.pushButton_Chart.clicked.connect(self.MyUI)
        self.pushButton_Check.clicked.connect(self.Connect_MySqlDb)
        self.pushButton_Browse.clicked.connect(self.pushButton_handler)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Check.setText(_translate("MainWindow", "Check DB Connection"))
        self.pushButton_Browse.setText(_translate("MainWindow", "Browse"))
        self.pushButton_Chart.setText(_translate("MainWindow", "Show Chart"))
        self.label_1.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "3"))

    def Connect_MySqlDb(self):
        try:
            db = mdb.connect('localhost', 'root', 'Brother123', 'pyqt5')
            QMessageBox.about(self, 'Connection', 'Database Connected Successfully')
 
        except mdb.Error as e:
            QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
            sys.exit(1)

    def pushButton_handler(self):
        print("Button pressed")
        self.open_dialog_box()
        
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)

        with open(path, "r") as f:
            print(f.readline())

    def MyUI(self):
        canvas = Canvas(self, width=6, height=6)
        canvas.move(60,220)
 
class Canvas(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)
 
        self.plot()
 
    def plot(self):
        x = np.array([50, 30,40])
        labels = ["Apples", "Bananas", "Melons"]
        ax = self.figure.add_subplot(111)
        ax.pie(x, labels=labels)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())