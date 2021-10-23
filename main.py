import Functions
import normanFunc
import pandas
import json
import sys
import requests
import MainWindow
from MainWindow import Ui_MainWindow
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

# Load menu
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("Menu")
window.show()
sys.exit(app.exec_())