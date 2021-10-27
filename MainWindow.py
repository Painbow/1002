import Functions
import requests
import pandas
import json
import sys
import webbrowser
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QMessageBox

resource_id = "139a3035-e624-4f56-b63f-89ae28d4ae4c"
carparkinfo = "https://data.gov.sg/api/action/datastore_search?resource_id=" + resource_id + "&q="
carparkInfoJson = Functions.getOutput(carparkinfo)

global carparkType
carparkType = "ALL"

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
        MainWindow.resize(400, 298)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_menu = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_menu.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.tab_menu.setObjectName("tab_menu")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tab_1.setObjectName("tab_1")
        self.text_label_1 = QtWidgets.QLabel(self.tab_1)
        self.text_label_1.setGeometry(QtCore.QRect(20, 140, 281, 16))
        self.text_label_1.setObjectName("text_label_1")
        self.check_box_1 = QtWidgets.QCheckBox(self.tab_1)
        self.check_box_1.setGeometry(QtCore.QRect(20, 100, 241, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.check_box_1.setFont(font)
        self.check_box_1.setObjectName("check_box_1")
        self.ok_button_1 = QtWidgets.QDialogButtonBox(self.tab_1)
        self.ok_button_1.setGeometry(QtCore.QRect(20, 230, 81, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_button_1.sizePolicy().hasHeightForWidth())
        self.ok_button_1.setSizePolicy(sizePolicy)
        self.ok_button_1.setOrientation(QtCore.Qt.Vertical)
        self.ok_button_1.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.ok_button_1.setObjectName("ok_button_1")
        self.radioButton_1 = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton_1.setGeometry(QtCore.QRect(20, 10, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 30, 211, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 50, 291, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.text_box_1 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.text_box_1.setGeometry(QtCore.QRect(20, 160, 351, 31))
        self.text_box_1.setObjectName("text_box_1")
        self.tab_menu.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.text_label_2 = QtWidgets.QLabel(self.tab_2)
        self.text_label_2.setGeometry(QtCore.QRect(30, 60, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_label_2.setFont(font)
        self.text_label_2.setObjectName("text_label_2")
        self.text_label_3 = QtWidgets.QLabel(self.tab_2)
        self.text_label_3.setGeometry(QtCore.QRect(280, 70, 31, 16))
        self.text_label_3.setObjectName("text_label_3")
        self.text_label_4 = QtWidgets.QLabel(self.tab_2)
        self.text_label_4.setGeometry(QtCore.QRect(20, 100, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_label_4.setFont(font)
        self.text_label_4.setObjectName("text_label_4")
        self.ok_button_2 = QtWidgets.QDialogButtonBox(self.tab_2)
        self.ok_button_2.setGeometry(QtCore.QRect(20, 230, 81, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_button_2.sizePolicy().hasHeightForWidth())
        self.ok_button_2.setSizePolicy(sizePolicy)
        self.ok_button_2.setOrientation(QtCore.Qt.Vertical)
        self.ok_button_2.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.ok_button_2.setObjectName("ok_button_2")
        self.text_box_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.text_box_2.setGeometry(QtCore.QRect(200, 60, 71, 31))
        self.text_box_2.setObjectName("text_box_2")
        self.text_box_3 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.text_box_3.setGeometry(QtCore.QRect(200, 100, 71, 31))
        self.text_box_3.setObjectName("text_box_3")
        self.tab_menu.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_menu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.radioButton_1.toggled.connect(self.radio1_clicked)
        self.radioButton_2.toggled.connect(self.radio2_clicked)
        self.radioButton_3.toggled.connect(self.radio3_clicked)
        self.ok_button_1.clicked.connect(self.accept)
        self.ok_button_2.clicked.connect(self.accept2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_label_1.setText(_translate("MainWindow", "Filter by keywords (separate each keyword with spaces):"))
        self.check_box_1.setText(_translate("MainWindow", "Only display carparks with free parking"))
        self.radioButton_1.setText(_translate("MainWindow", "Display only surface carparks"))
        self.radioButton_2.setText(_translate("MainWindow", "Display only multi-storey carparks"))
        self.radioButton_3.setText(_translate("MainWindow", "Display both surface and multi-storey carparks"))
        self.tab_menu.setTabText(self.tab_menu.indexOf(self.tab_1), _translate("MainWindow", "Display Carpark Information"))
        self.text_label_2.setText(_translate("MainWindow", "Retrieve data from the past: "))
        self.text_label_3.setText(_translate("MainWindow", "days"))
        self.text_label_4.setText(_translate("MainWindow", "Carpark to retrieve data from:"))
        self.text_box_2.setPlainText(_translate("MainWindow", "5"))
        self.text_box_3.setPlainText(_translate("MainWindow", "HE12"))
        self.tab_menu.setTabText(self.tab_menu.indexOf(self.tab_2), _translate("MainWindow", "Carpark Availability Graph"))

    def radio1_clicked(self):
        if self.radioButton_1.isChecked():
            global carparkType
            carparkType="SURFACE CAR PARK"

    def radio2_clicked(self):
        if self.radioButton_2.isChecked():
            global carparkType
            carparkType="MULTI-STOREY CAR PARK"

    def radio3_clicked(self):
        if self.radioButton_3.isChecked():
            global carparkType
            carparkType="ALL"

    def accept(self):
        try:
            area = str(self.text_box_1.toPlainText())
            result = carparkInfoJson['result']
            recordList = result['records']

            if area != "":
                carparkinfo2 = "https://data.gov.sg/api/action/datastore_search?resource_id=" + resource_id + "&q="+area
                carparkInfoJson2 = Functions.getOutput(carparkinfo2)
                result = carparkInfoJson2['result']
                recordList = result['records']

            filter_type = False

            if self.check_box_1.isChecked():
                filter_free = True
            else:
                filter_free = False

            listOfCarparkData = Functions.getAllCarparkAvail()

            if len(carparkType) > 4:
                filter_type = True


            if filter_type or filter_free:
                filterList = []

                for carpark in recordList:
                    cpType = carpark["car_park_type"]
                    cpFree = carpark["free_parking"]

                    if filter_type and filter_free:
                        if (filter_free and cpFree != "NO") and (len(carparkType) > 4 and carparkType == cpType):
                            filterList.append(carpark)

                    elif filter_type:
                        if len(carparkType) > 4 and carparkType == cpType:
                            filterList.append(carpark)

                    elif filter_free:
                        if filter_free and cpFree != "NO":
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

            if area != "":
                dataframe = dataframe.set_axis(
                    ['Full Count', 'Short Term Parking', 'Carpark Type', 'Y Coordinates', 'X Coordinates', 'Rank', 'Free Parking',
                     'Gantry Height', 'Carpark Basement', 'Night Parking', 'Address', 'Carpark Decks', 'ID', 'Carpark No.',
                     'Type of Parking System', 'Total Lots', 'Lot Type', 'Lots Available'], axis=1)
            else:
                dataframe = dataframe.set_axis(
                ['Short Term Parking', 'Carpark Type', 'Y Coordinates', 'X Coordinates', 'Free Parking',
                 'Gantry Height', 'Carpark Basement', 'Night Parking', 'Address', 'Carpark Decks', 'ID', 'Carpark No.',
                 'Type of Parking System', 'Total Lots', 'Lot Type', 'Lots Available'], axis=1)

            model = pandasModel(dataframe)

            global view
            view = QTableView()
            view.setModel(model)
            view.setWindowTitle("Carparks")
            view.resize(1920, 1080)

            if area !="":
                view.doubleClicked.connect(lambda: Functions.openlink(
                    ((view.selectionModel().currentIndex()).sibling(view.selectionModel().currentIndex().row(), 3).data()),
                    ((view.selectionModel().currentIndex()).sibling(view.selectionModel().currentIndex().row(), 4).data())))

            else:
                view.doubleClicked.connect(lambda: Functions.openlink(
                    ((view.selectionModel().currentIndex()).sibling(view.selectionModel().currentIndex().row(), 2).data()),
                    ((view.selectionModel().currentIndex()).sibling(view.selectionModel().currentIndex().row(), 3).data())))

            header = view.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            view.show()

        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Invalid Input')
            msg.setWindowTitle("Error")
            msg.exec_()

    def accept2(self):
        try:
            timeStamps = Functions.getPastDays(int(self.text_box_2.toPlainText()))
            availTime = Functions.getCarparkAvailAtTime(timeStamps, self.text_box_3.toPlainText())
            Functions.plotGraph(("Carpark Availability for the past {} days".format(self.text_box_2.toPlainText())), "Time" ,"Carpark Avail", timeStamps, availTime)

        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Invalid Input')
            msg.setWindowTitle("Error")
            msg.exec_()
