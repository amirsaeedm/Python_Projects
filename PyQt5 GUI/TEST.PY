import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('Browse_excel_show_chart.ui', self)


app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())