import Functions
import requests
import pandas
import json
import sys
import webbrowser
import onemapsg
from onemapsg import OneMapClient
from scipy import spatial
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt

resource_id = "139a3035-e624-4f56-b63f-89ae28d4ae4c"
carparkinfo = "https://data.gov.sg/api/action/datastore_search?resource_id=" + resource_id + "&q="
carparkInfoJson = Functions.getOutput(carparkinfo)

global carparkType
carparkType = "ALL"
global freeparking
freeparking = False

class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tab_menu = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_menu.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.tab_menu.setObjectName("tab_menu")

        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tab_menu.addTab(self.tab_1, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_menu.addTab(self.tab_2, "")

        self.radioButton_1 = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton_1.setGeometry(QtCore.QRect(10, 10, 221, 31))

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)

        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_1")

        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 341, 31))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())

        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")

        self.ok_button = QtWidgets.QDialogButtonBox(self.tab_1)
        self.ok_button.setGeometry(QtCore.QRect(30, 200, 81, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)
        self.ok_button.setOrientation(QtCore.Qt.Vertical)
        self.ok_button.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.ok_button.setObjectName("ok_button")

        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 10, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")

        font2 = QtGui.QFont()
        font2.setPointSize(10)

        self.radioButton_4 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 70, 211, 17))
        self.radioButton_4.setFont(font2)
        self.radioButton_4.setObjectName("radioButton_4")

        self.radioButton_5 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 40, 191, 17))
        self.radioButton_5.setFont(font2)
        self.radioButton_5.setObjectName("radioButton_5")

        self.text_box = QtWidgets.QPlainTextEdit(self.tab_2)
        self.text_box.setGeometry(QtCore.QRect(20, 120, 351, 111))
        self.text_box.setPlainText("")
        self.text_box.setObjectName("text_box")
        self.text_label = QtWidgets.QLabel(self.tab_2)
        self.text_label.setGeometry(QtCore.QRect(20, 100, 400, 16))
        self.text_label.setObjectName("text_label")

        self.default_button = QtWidgets.QDialogButtonBox(self.tab_2)
        self.default_button.setGeometry(QtCore.QRect(20, 240, 81, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.default_button.sizePolicy().hasHeightForWidth())
        self.default_button.setSizePolicy(sizePolicy)
        self.default_button.setOrientation(QtCore.Qt.Vertical)
        self.default_button.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.default_button.setObjectName("default_button")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_menu.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.radioButton_1.toggled.connect(self.radio1_clicked)
        self.radioButton_2.toggled.connect(self.radio2_clicked)
        self.radioButton_3.toggled.connect(self.radio3_clicked)
        self.radioButton_4.toggled.connect(self.radio4_clicked)
        self.radioButton_5.toggled.connect(self.radio5_clicked)
        self.ok_button.clicked.connect(self.accept)
        #self.default_button.clicked.connect(self.searchbyonemap)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_1.setText(_translate("MainWindow", "Display all carparks"))
        self.radioButton_2.setText(_translate("MainWindow", "Display all carkparks that are free"))
        self.tab_menu.setTabText(self.tab_menu.indexOf(self.tab_1), _translate("MainWindow", "Load Carpark Tables"))
        self.radioButton_3.setText(_translate("MainWindow", "Display all carparks"))
        self.radioButton_4.setText(_translate("MainWindow", "Display only multi-storey carparks"))
        self.radioButton_5.setText(_translate("MainWindow", "Display only surface carparks"))
        self.text_label.setText(_translate("MainWindow", "Filter by keywords instead:"))
        self.tab_menu.setTabText(self.tab_menu.indexOf(self.tab_2), _translate("MainWindow", "Refine search"))

    def radio1_clicked(self):
        if self.radioButton_1.isChecked():
            global freeparking
            freeparking = False

    def radio2_clicked(self):
        if self.radioButton_2.isChecked():
            global freeparking
            freeparking = True

    def radio3_clicked(self):
        if self.radioButton_3.isChecked():
            global carparkType
            carparkType="ALL"

    def radio4_clicked(self):
        if self.radioButton_4.isChecked():
            global carparkType
            carparkType="MULTI-STOREY CAR PARK"

    def radio5_clicked(self):
        if self.radioButton_5.isChecked():
            global carparkType
            carparkType="SURFACE CAR PARK"

    # Will read user input
    #def searchbyonemap(self):
    #area = (self.text_box.toPlainText())


    def accept(self):

        filter_type = False
        filter_free = False
        listOfCarparkData = Functions.getAllCarparkAvail()
        result = carparkInfoJson['result']
        recordList = result['records']

        if len(carparkType) > 4:
            filter_type = True
        if freeparking:
            filter_free = True

        if filter_type or filter_free:
            filterList = []

            for carpark in recordList:
                cpType = carpark["car_park_type"]
                cpFree = carpark["free_parking"]
                # print ("cptype %s and %s"%(cpType,carparkType))

                if filter_type and filter_free:
                    if (freeparking and cpFree != "NO") and (len(carparkType) > 4 and carparkType == cpType):
                        filterList.append(carpark)

                elif filter_type:
                    if len(carparkType) > 4 and carparkType == cpType:
                        filterList.append(carpark)

                elif filter_free:
                    if freeparking and cpFree != "NO":
                        filterList.append(carpark)

            recordList = filterList

        for carpark in recordList:

            cpNo = carpark['car_park_no']
            availStatus = Functions.getCarparkAvail(listOfCarparkData, cpNo)
            if (availStatus != None):
                carpark['Total Lots'] = availStatus[0]['total_lots']
                carpark['Lot Type'] = availStatus[0]['lot_type']
                carpark['Lot Available'] = availStatus[0]['lots_available']

        dataframe = pandas.json_normalize(recordList)
        dataframe = dataframe.set_axis(['Short Term Parking','Carpark Type', 'Y Coordinates', 'X Coordinates', 'Free Parking', 'Gantry Height', 'Carpark Basement', 'Night Parking', 'Address', 'Carpark Decks', 'ID', 'Carpark No.', 'Type of Parking System', 'Total Lots', 'Lot Type', 'Lots Available'], axis=1)
        model = pandasModel(dataframe)

        global view
        view = QTableView()
        view.setModel(model)
        view.setWindowTitle("Carparks")
        view.resize(1920, 1080)
        # clicking on a table row returns Y and X coordinates of that row
        view.clicked.connect(lambda:print(((view.selectionModel().currentIndex()).sibling(view.selectionModel().currentIndex().row(), 2).data()), ((view.selectionModel().currentIndex()).sibling(view.selectionModel().currentIndex().row(), 3).data())))
        header = view.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        view.show()

