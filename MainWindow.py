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

checkLimit = "https://data.gov.sg/api/action/datastore_search?resource_id=" + resource_id + "&limit=1"
checkLimitJson = Functions.getOutput(checkLimit)
maxLimit = checkLimitJson["result"]["total"]

carparkinfo = "https://data.gov.sg/api/action/datastore_search?resource_id=" + resource_id + "&limit=" + str(maxLimit)
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
        self.tab_menu.setIconSize(QtCore.QSize(16, 16))
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
        self.radioButton_1.setGeometry(QtCore.QRect(20, 20, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 40, 211, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 60, 291, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.text_box_1 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.text_box_1.setGeometry(QtCore.QRect(20, 160, 351, 31))
        self.text_box_1.setPlainText("")
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
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.text_label_5 = QtWidgets.QLabel(self.tab_3)
        self.text_label_5.setGeometry(QtCore.QRect(20, 10, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_label_5.setFont(font)
        self.text_label_5.setObjectName("text_label_5")
        self.text_label_6 = QtWidgets.QLabel(self.tab_3)
        self.text_label_6.setGeometry(QtCore.QRect(20, 40, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_label_6.setFont(font)
        self.text_label_6.setObjectName("text_label_6")
        self.text_label_7 = QtWidgets.QLabel(self.tab_3)
        self.text_label_7.setGeometry(QtCore.QRect(20, 70, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_label_7.setFont(font)
        self.text_label_7.setObjectName("text_label_7")
        self.text_label_8 = QtWidgets.QLabel(self.tab_3)
        self.text_label_8.setGeometry(QtCore.QRect(20, 120, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_label_8.setFont(font)
        self.text_label_8.setObjectName("text_label_8")
        self.text_label_9 = QtWidgets.QLabel(self.tab_3)
        self.text_label_9.setGeometry(QtCore.QRect(20, 150, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_label_9.setFont(font)
        self.text_label_9.setObjectName("text_label_9")
        self.text_label_10 = QtWidgets.QLabel(self.tab_3)
        self.text_label_10.setGeometry(QtCore.QRect(20, 180, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_label_10.setFont(font)
        self.text_label_10.setObjectName("text_label_10")
        self.text_label_11 = QtWidgets.QLabel(self.tab_3)
        self.text_label_11.setGeometry(QtCore.QRect(330, 10, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_label_11.setFont(font)
        self.text_label_11.setObjectName("text_label_11")
        self.text_label_12 = QtWidgets.QLabel(self.tab_3)
        self.text_label_12.setGeometry(QtCore.QRect(330, 40, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_label_12.setFont(font)
        self.text_label_12.setObjectName("text_label_12")
        self.text_label_13 = QtWidgets.QLabel(self.tab_3)
        self.text_label_13.setGeometry(QtCore.QRect(330, 70, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_label_13.setFont(font)
        self.text_label_13.setObjectName("text_label_13")
        self.text_label_14 = QtWidgets.QLabel(self.tab_3)
        self.text_label_14.setGeometry(QtCore.QRect(330, 120, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_label_14.setFont(font)
        self.text_label_14.setObjectName("text_label_14")
        self.text_label_15 = QtWidgets.QLabel(self.tab_3)
        self.text_label_15.setGeometry(QtCore.QRect(330, 150, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_label_15.setFont(font)
        self.text_label_15.setObjectName("text_label_15")
        self.text_label_16 = QtWidgets.QLabel(self.tab_3)
        self.text_label_16.setGeometry(QtCore.QRect(330, 180, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_label_16.setFont(font)
        self.text_label_16.setObjectName("text_label_16")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tab_menu.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_menu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.radioButton_1.toggled.connect(self.radio1_clicked)
        self.radioButton_2.toggled.connect(self.radio2_clicked)
        self.radioButton_3.toggled.connect(self.radio3_clicked)
        self.ok_button_1.clicked.connect(self.accept)
        self.ok_button_2.clicked.connect(self.accept2)
        self.pushButton.clicked.connect(self.accept3)

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
        self.text_label_5.setText(_translate("MainWindow", "Number of surface carparks:"))
        self.text_label_6.setText(_translate("MainWindow", "Number of sheltered carparks:"))
        self.text_label_7.setText(_translate("MainWindow", "Percentage of sheltered carparks:"))
        self.text_label_8.setText(_translate("MainWindow", "Number of carparks that offer free parking:"))
        self.text_label_9.setText(_translate("MainWindow", "Number of carparks that do not offer free parking:"))
        self.text_label_10.setText(_translate("MainWindow", "Percentage of carparks that offer free parking:"))
        self.text_label_11.setText(_translate("MainWindow", "-"))
        self.text_label_12.setText(_translate("MainWindow", "-"))
        self.text_label_13.setText(_translate("MainWindow", "-%"))
        self.text_label_14.setText(_translate("MainWindow", "-"))
        self.text_label_15.setText(_translate("MainWindow", "-"))
        self.text_label_16.setText(_translate("MainWindow", "-%"))
        self.pushButton.setText(_translate("MainWindow", "Fetch"))
        self.tab_menu.setTabText(self.tab_menu.indexOf(self.tab_3), _translate("MainWindow", "Statistics"))

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
            result = carparkInfoJson['result']
            record_list = result['records']
            area = str(self.text_box_1.toPlainText()).replace(" ", "%20")

            if area != "":
                carparkinfo2 = "https://data.gov.sg/api/action/datastore_search?resource_id=" + resource_id + "&q="+area
                carparkInfoJson2 = Functions.getOutput(carparkinfo2)
                result = carparkInfoJson2['result']
                record_list = result['records']

            filter_type = False

            if self.check_box_1.isChecked():
                filter_free = True
            else:
                filter_free = False

            list_of_carpark_data = Functions.getAllCarparkAvail()

            if len(carparkType) > 4:
                filter_type = True


            if filter_type or filter_free:
                filter_list = []

                for carpark in record_list:
                    cp_type = carpark["car_park_type"]
                    cp_free = carpark["free_parking"]

                    if filter_type and filter_free:
                        if (filter_free and cp_free != "NO") and (len(carparkType) > 4 and carparkType == cp_type):
                            filter_list.append(carpark)

                    elif filter_type:
                        if len(carparkType) > 4 and carparkType == cp_type:
                            filter_list.append(carpark)

                    elif filter_free:
                        if filter_free and cp_free != "NO":
                            filter_list.append(carpark)

                record_list = filter_list

            for carpark in record_list:

                cpNo = carpark['car_park_no']
                avail_status = Functions.getCarparkAvail(list_of_carpark_data, cpNo)

                if avail_status != None:
                    carpark['Total Lots'] = avail_status[0]['total_lots']
                    carpark['Lot Type'] = avail_status[0]['lot_type']
                    carpark['Lot Available'] = avail_status[0]['lots_available']

            dataframe = pandas.json_normalize(record_list)

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
            if (self.text_box_1.toPlainText()).isalnum() is False:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Invalid Input')
                msg.setWindowTitle("Error")
                msg.exec_()

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('There are no carparks to display for this location, please try another location')
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

    def accept3(self):
        try:
            result = carparkInfoJson['result']
            recordList = result['records']

            surface_carparks = 0
            not_free_carparks = 0

            for carpark in recordList:
                cp_type = carpark["car_park_type"]
                cp_free = carpark["free_parking"]

                if cp_free == "NO":
                    not_free_carparks += 1

                if cp_type == "SURFACE CAR PARK":
                    surface_carparks += 1

            shelter_carparks = maxLimit - surface_carparks
            free_carparks = maxLimit - not_free_carparks

            sheltered_percentage = (shelter_carparks/maxLimit)* 100
            free_percentage = (free_carparks/maxLimit)* 100

            _translate = QtCore.QCoreApplication.translate
            self.text_label_11.setText(_translate("MainWindow", "{}".format(surface_carparks)))
            self.text_label_12.setText(_translate("MainWindow", "{}".format(shelter_carparks)))
            self.text_label_13.setText(_translate("MainWindow", "{0:.1f}%".format(sheltered_percentage)))
            self.text_label_14.setText(_translate("MainWindow", "{}".format(free_carparks)))
            self.text_label_15.setText(_translate("MainWindow", "{}".format(not_free_carparks)))
            self.text_label_16.setText(_translate("MainWindow", "{0:.1f}%".format(free_percentage)))

        except:

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Error retrieving results')
            msg.setWindowTitle("Error")
            msg.exec_()


