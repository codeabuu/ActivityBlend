'''
Shceduling Software

............................
The code below is written entierly in python using the PyQt5 Module.
The majority of the UI for this project has been generated using 
the software: QtDesigner.
'''
import automate-install-reqs
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pprint
import random
import time
from word import make_word_doc


class Ui_MainWindow(object):
    '''
    UI functions class
    '''

    def setupUi(self, MainWindow):
        '''
        setting variables and drawing our main UI
        (remember we are using Qtdesigner app for our UI design)
        '''

        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(640, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.morning.setGeometry(QtCore.QRect(0, 320, 201, 281))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.morning.setFont(font)
        self.morning.setObjectName("morning")
        self.m1 = QtWidgets.QCheckBox(self.morning)
        self.m1.setGeometry(QtCore.QRect(10, 30, 181, 25))
        self.m1.setObjectName("m1")
        self.m2 = QtWidgets.QCheckBox(self.morning)
        self.m2.setGeometry(QtCore.QRect(10, 50, 181, 25))
        self.m2.setObjectName("m2")
        self.m3 = QtWidgets.QCheckBox(self.morning)
        self.m3.setGeometry(QtCore.QRect(10, 70, 181, 25))
        self.m3.setObjectName("m3")
        self.m4 = QtWidgets.QCheckBox(self.morning)
        self.m4.setGeometry(QtCore.QRect(10, 90, 181, 25))
        self.m4.setObjectName("m4")
        self.m5 = QtWidgets.QCheckBox(self.morning)
        self.m5.setGeometry(QtCore.QRect(10, 110, 181, 25))
        self.m5.setObjectName("m5")
        self.m6 = QtWidgets.QCheckBox(self.morning)
        self.m6.setGeometry(QtCore.QRect(10, 130, 181, 25))
        self.m6.setObjectName("m6")
        self.m7 = QtWidgets.QCheckBox(self.morning)
        self.m7.setGeometry(QtCore.QRect(10, 150, 181, 25))
        self.m7.setObjectName("m7")
        self.m8 = QtWidgets.QCheckBox(self.morning)
        self.m8.setGeometry(QtCore.QRect(10, 170, 181, 25))
        self.m8.setObjectName("m8")
        self.m9 = QtWidgets.QCheckBox(self.morning)
        self.m9.setGeometry(QtCore.QRect(10, 190, 181, 25))
        self.m9.setObjectName("m9")
        self.m10 = QtWidgets.QCheckBox(self.morning)
        self.m10.setGeometry(QtCore.QRect(10, 210, 181, 25))
        self.m10.setObjectName("m10")
        self.mOther = QtWidgets.QCheckBox(self.morning)
        self.mOther.setGeometry(QtCore.QRect(10, 240, 16, 25))
        self.mOther.setObjectName("mOther")
        self.m_lineEdit = QtWidgets.QLineEdit(self.morning)
        self.m_lineEdit.setGeometry(QtCore.QRect(30, 240, 91, 20))
        self.m_lineEdit.setText("")
        self.m_lineEdit.setObjectName("m_lineEdit")

        self.afternoon = QtWidgets.QGroupBox(self.centralwidget)
        self.afternoon.setGeometry(QtCore.QRect(200, 320, 201, 281))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.afternoon.setFont(font)
        self.afternoon.setObjectName("afternoon")
        self.a1 = QtWidgets.QCheckBox(self.afternoon)
        self.a1.setGeometry(QtCore.QRect(10, 30, 181, 25))
        self.a1.setObjectName("a1")
        self.a2 = QtWidgets.QCheckBox(self.afternoon)
        self.a2.setGeometry(QtCore.QRect(10, 50, 181, 25))
        self.a2.setObjectName("a2")
        self.a3 = QtWidgets.QCheckBox(self.afternoon)
        self.a3.setGeometry(QtCore.QRect(10, 70, 181, 25))
        self.a3.setObjectName("a3")
        self.a4 = QtWidgets.QCheckBox(self.afternoon)
        self.a4.setGeometry(QtCore.QRect(10, 90, 181, 25))
        self.a4.setObjectName("a4")
        self.a5 = QtWidgets.QCheckBox(self.afternoon)
        self.a5.setGeometry(QtCore.QRect(10, 110, 181, 25))
        self.a5.setObjectName("a5")
        self.a6 = QtWidgets.QCheckBox(self.afternoon)
        self.a6.setGeometry(QtCore.QRect(10, 130, 181, 25))
        self.a6.setObjectName("a6")
        self.a7 = QtWidgets.QCheckBox(self.afternoon)
        self.a7.setGeometry(QtCore.QRect(10, 150, 181, 25))
        self.a7.setObjectName("a7")
        self.a8 = QtWidgets.QCheckBox(self.afternoon)
        self.a8.setGeometry(QtCore.QRect(10, 170, 181, 25))
        self.a8.setObjectName("a8")
        self.a9 = QtWidgets.QCheckBox(self.afternoon)
        self.a9.setGeometry(QtCore.QRect(10, 190, 181, 25))
        self.a9.setObjectName("a9")
        self.a10 = QtWidgets.QCheckBox(self.afternoon)
        self.a10.setGeometry(QtCore.QRect(10, 210, 181, 25))
        self.a10.setObjectName("a10")
        self.aOther = QtWidgets.QCheckBox(self.afternoon)
        self.aOther.setGeometry(QtCore.QRect(10, 240, 16, 17))
        self.aOther.setObjectName("aOther")
        self.a_lineEdit = QtWidgets.QLineEdit(self.afternoon)
        self.a_lineEdit.setGeometry(QtCore.QRect(30, 240, 91, 20))
        self.a_lineEdit.setText("")
        self.a_lineEdit.setObjectName("a_lineEdit")

        self.g2 = QtWidgets.QGroupBox(self.centralwidget)
        self.g2.setGeometry(QtCore.QRect(0, 0, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.g2.setFont(font)
        self.g2.setObjectName("g2")
        self.label_2 = QtWidgets.QLabel(self.g2)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 61, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.g2)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 61, 41))
        self.label_3.setObjectName("label_3")
        self.g2_lunch = QtWidgets.QComboBox(self.g2)
        self.g2_lunch.setGeometry(QtCore.QRect(18, 60, 100, 22))
        self.g2_lunch.setCurrentText("")
        self.g2_lunch.setObjectName("g2_lunch")
        self.g2_swim = QtWidgets.QComboBox(self.g2)
        self.g2_swim.setGeometry(QtCore.QRect(18, 120, 100, 22))
        self.g2_swim.setCurrentText("")
        self.g2_swim.setObjectName("g2_swim")

        self.groups = QtWidgets.QGroupBox(self.centralwidget)
        self.groups.setGeometry(QtCore.QRect(400, 320, 231, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groups.setFont(font)
        self.groups.setObjectName("groups")
        self.label = QtWidgets.QLabel(self.groups)
        self.label.setGeometry(QtCore.QRect(10, 30, 230, 31))
        self.label.setObjectName("label")

        self.num_groups = QtWidgets.QLineEdit(self.groups)
        self.num_groups.setGeometry(QtCore.QRect(10, 70, 201, 20))
        self.num_groups.setObjectName("num_groups")
        self.done = QtWidgets.QPushButton(self.centralwidget)
        self.done.setGeometry(QtCore.QRect(400, 430, 231, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.done.setFont(font)
        self.done.setObjectName("done")
        self.g3 = QtWidgets.QGroupBox(self.centralwidget)
        self.g3.setGeometry(QtCore.QRect(120, 0, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.g3.setFont(font)
        self.g3.setObjectName("g3")
        self.label_6 = QtWidgets.QLabel(self.g3)
        self.label_6.setGeometry(QtCore.QRect(40, 20, 61, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.g3)
        self.label_7.setGeometry(QtCore.QRect(40, 80, 61, 41))
        self.label_7.setObjectName("label_7")
        self.g3_lunch = QtWidgets.QComboBox(self.g3)
        self.g3_lunch.setGeometry(QtCore.QRect(18, 60, 100, 22))
        self.g3_lunch.setCurrentText("")
        self.g3_lunch.setObjectName("g3_lunch")
        self.g3_swim = QtWidgets.QComboBox(self.g3)
        self.g3_swim.setGeometry(QtCore.QRect(18, 120, 100, 22))
        self.g3_swim.setCurrentText("")
        self.g3_swim.setObjectName("g3_swim")

        self.g4 = QtWidgets.QGroupBox(self.centralwidget)
        self.g4.setGeometry(QtCore.QRect(240, 0, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.g4.setFont(font)
        self.g4.setObjectName("g4")
        self.label_8 = QtWidgets.QLabel(self.g4)
        self.label_8.setGeometry(QtCore.QRect(40, 20, 61, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.g4)
        self.label_9.setGeometry(QtCore.QRect(40, 80, 61, 41))
        self.label_9.setObjectName("label_9")
        self.g4_lunch = QtWidgets.QComboBox(self.g4)
        self.g4_lunch.setGeometry(QtCore.QRect(18, 60, 100, 22))
        self.g4_lunch.setCurrentText("")
        self.g4_lunch.setObjectName("g4_lunch")
        self.g4_swim = QtWidgets.QComboBox(self.g4)
        self.g4_swim.setGeometry(QtCore.QRect(18, 120, 100, 22))
        self.g4_swim.setCurrentText("")
        self.g4_swim.setObjectName("g4_swim")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 0, 131, 161))
        
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(40, 20, 61, 41))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(40, 80, 61, 41))
        self.label_11.setObjectName("label_11")
        self.g5_lunch = QtWidgets.QComboBox(self.groupBox_2)
        self.g5_lunch.setGeometry(QtCore.QRect(18, 60, 100, 22))
        self.g5_lunch.setCurrentText("")
        self.g5_lunch.setObjectName("g5_lunch")
        self.g5_swim = QtWidgets.QComboBox(self.groupBox_2)
        self.g5_swim.setGeometry(QtCore.QRect(18, 120, 100, 22))
        self.g5_swim.setCurrentText("")
        self.g5_swim.setObjectName("g5_swim")

        self.g6 = QtWidgets.QGroupBox(self.centralwidget)
        self.g6.setGeometry(QtCore.QRect(490, 0, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.g6.setFont(font)
        self.g6.setObjectName("g6")
        self.label_14 = QtWidgets.QLabel(self.g6)
        self.label_14.setGeometry(QtCore.QRect(40, 20, 61, 41))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.g6)
        self.label_15.setGeometry(QtCore.QRect(40, 80, 61, 41))
        self.label_15.setObjectName("label_15")
        self.g6_lunch = QtWidgets.QComboBox(self.g6)
        self.g6_lunch.setGeometry(QtCore.QRect(18, 60, 100, 22))
        self.g6_lunch.setCurrentText("")
        self.g6_lunch.setObjectName("g6_lunch")
        self.g6_swim = QtWidgets.QComboBox(self.g6)
        self.g6_swim.setGeometry(QtCore.QRect(18, 120, 100, 22))
        self.g6_swim.setCurrentText("")
        self.g6_swim.setObjectName("g6_swim")

        self.g8 = QtWidgets.QGroupBox(self.centralwidget)
        self.g8.setGeometry(QtCore.QRect(120, 160, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.g8.setFont(font)
        self.g8.setObjectName("g8")
        self.label_26 = QtWidgets.QLabel(self.g8)
        self.label_26.setGeometry(QtCore.QRect(40, 20, 61, 41))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.g8)
        self.label_27.setGeometry(QtCore.QRect(40, 80, 61, 41))
        self.label_27.setObjectName("label_27")
        self.g8_lunch = QtWidgets.QComboBox(self.g8)
        self.g8_lunch.setGeometry(QtCore.QRect(18, 60, 100, 22))
        self.g8_lunch.setCurrentText("")
        self.g8_lunch.setObjectName("g8_lunch")
        self.g8_swim = QtWidgets.QComboBox(self.g8)
        self.g8_swim.setGeometry(QtCore.QRect(18, 120, 100, 22))
        self.g8_swim.setCurrentText("")
        self.g8_swim.setObjectName("g8_swim")

        self.g4_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.g4_2.setGeometry(QtCore.QRect(240, 160, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.g4_2.setFont(font)
        self.g4_2.setObjectName("g4_2")
        self.label_28 = QtWidgets.QLabel(self.g4_2)
        self.label_28.setGeometry(QtCore.QRect(40, 20, 61, 41))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.g4_2)
        self.label_29.setGeometry(QtCore.QRect(40, 80, 61, 41))
        self.label_29.setObjectName("label_29")

        self.g9_lunch = QtWidgets.QComboBox(self.g4_2)
        self.g9_lunch.setGeometry(QtCore.QRect(18, 60, 100, 22))
        self.g9_lunch.setCurrentText("")
        self.g9_lunch.setObjectName("g9_lunch")
        self.g9_swim = QtWidgets.QComboBox(self.g4_2)
        self.g9_swim.setGeometry(QtCore.QRect(18, 120, 100, 22))
        self.g9_swim.setCurrentText("")
        self.g9_swim.setObjectName("g9_swim")

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(360, 160, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_30 = QtWidgets.QLabel(self.groupBox_3)
        self.label_30.setGeometry(QtCore.QRect(40, 20, 61, 41))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.groupBox_3)
        self.label_31.setGeometry(QtCore.QRect(40, 80, 61, 41))
        self.label_31.setObjectName("label_31")

        self.g10_lunch = QtWidgets.QComboBox(self.groupBox_3)
        self.g10_lunch.setGeometry(QtCore.QRect(18, 60, 100, 22))
        self.g10_lunch.setCurrentText("")
        self.g10_lunch.setObjectName("g10_lunch")
        self.g10_swim = QtWidgets.QComboBox(self.groupBox_3)
        self.g10_swim.setGeometry(QtCore.QRect(18, 120, 100, 22))
        self.g10_swim.setCurrentText("")
        self.g10_swim.setObjectName("g10_swim")

        self.groupBox_set = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_set.setGeometry(QtCore.QRect(490, 160, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_set.setFont(font)
        self.groupBox_set.setObjectName("groupBox_set")

        self.week = QtWidgets.QComboBox(self.groupBox_set)
        self.week.setGeometry(QtCore.QRect(20, 110, 100, 22))
        self.week.setCurrentText("")
        self.week.setObjectName("week")
        self.set = QtWidgets.QCheckBox(self.groupBox_set)
        self.set.setGeometry(QtCore.QRect(10, 30, 181, 17))
        self.set.setObjectName("set")


        for x in range(1, 8):
            self.weel.addItem("Week " + str(x))

        self.week.setCurrentIndex(0)

        self.g7 = QtWidgets.QGroupBox(self.centralwidget)
        self.g7.setGeometry(QtCore.QRect(0, 160, 130, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.g7.setFont(font)
        self.g7.setObjectName("g7")
        self.label_32 = QtWidgets.QLabel(self.g7)
        self.label_32.setGeometry(QtCore.QRect(40, 20, 61, 41))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.g7)
        self.label_33.setGeometry(QtCore.QRect(40, 80, 61, 41))
        self.label_33.setObjectName("label_33")
        self.g7_lunch = QtWidgets.QComboBox(self.g7)
        self.g7_lunch.setGeometry(QtCore.QRect(18, 60, 100, 22))
        self.g7_lunch.setCurrentText("")
        self.g7_lunch.setObjectName("g7_lunch")
        self.g7_swim = QtWidgets.QComboBox(self.g7)
        self.g7_swim.setGeometry(QtCore.QRect(18, 120, 100, 22))
        self.g7_swim.setCurrentText("")
        self.g7_swim.setObjectName("g7_swim")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        '''
        creating list of all check buttons and comboboxes
        '''
        self.comboBoxLunches = [self.g2_lunch, self.g3_lunch, self.g4_lunch, self.g5_lunch, self.g6_lunch, self.g7_lunch, self.g8_lunch, self.g9_lunch, self.g10_lunch]
        self.comboBoxSwim = [self.g2_swim, self.g3_swim, self.g4_swim, self.g5_swim, self.g6_swim, self.g7_swim, self.g8_swim, self.g9_swim, self.g10_swim]

        self.morningCheckBoxes = [self.m1, self.m2, self.m3, self.m4, self.m5, self.m6, self.m7, self.m8, self.m9, self.m10, self.mOther]
        self.afternoonCheckBoxes = [self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8, self.a9, self.a10, self.aOther]


        '''
        setting combobox options
        '''
        for combo in self.comboBoxLunches:
            combo.addItem("Period 3")
            combo.addItem("Period 4")

        for combo in self.comboBoxSwim:
            combo.addItem("Period 3")
            combo.addItem("Period 4")
            combo.addItem("Period 5")
            combo.addItem("Period 6")


        '''
        setting default combo options, grp2
        '''
        index = self.comboBoxLunches[0].findText("Period 3", QtCore.Qt.MatchFixedString)
        self.comboBoxLunches[0].setCurrentIndex(index)

        index = self.comboBoxSwim[0].findText("Period 4", QtCore.Qt.MatchFixedString)
        self.comboBoxSwim[0].setCurrentIndex(index)

        '''grp 3'''
        index = self.comboBoxLunches[1].findText("Period 3", QtCore.Qt.MatchFixedString)
        self.comboBoxLunches[1].setCurrentIndex(index)

        index = self.comboBoxSwim[1].findText("Period 5", QtCore.Qt.MatchFixedString)
        self.comboBoxSwim[1].setCurrentIndex(index)

        '''grp 4'''
        index = self.comboBoxLunches[2].findText("Period 3", QtCore.Qt.MatchFixedString)
        self.comboBoxLunches[2].setCurrentIndex(index)

        index = self.comboBoxSwim[2].findText("Period 5", QtCore.Qt.MatchFixedString)
        self.comboBoxSwim[2].setCurrentIndex(index)

        '''grp5'''
        index = self.comboBoxLunches[3].findText("Period 3", QtCore.Qt.MatchFixedString)
        self.comboBoxLunches[3].setCurrentIndex(index)

        index = self.comboBoxSwim[3].findText("Period 5", QtCore.Qt.MatchFixedString)
        self.comboBoxSwim[3].setCurrentIndex(index)

        '''grp6'''
        index = self.comboBoxLunches[4].findText("Period 4", QtCore.Qt.MatchFixedString)
        self.comboBoxLunches[4].setCurrentIndex(index)

        index = self.comboBoxSwim[4].findText("Period 6", QtCore.Qt.MatchFixedString)
        self.comboBoxSwim[4].setCurrentIndex(index)

        '''grp 7'''
        index = self.comboBoxLunches[5].findText("Period 4", QtCore.Qt.MatchFixedString)
        self.comboBoxLunches[5].setCurrentIndex(index)

        index = self.comboBoxSwim[5].findText("Period 6", QtCore.Qt.MatchFixedString)
        self.comboBoxSwim[5].setCurrentIndex(index)

        '''grp8'''
        index = self.comboBoxLunches[6].findText("Period 4", QtCore.Qt.MatchFixedString)
        self.comboBoxLunches[6].setCurrentIndex(index)

        index = self.comboBoxSwim[6].findText("Period 6", QtCore.Qt.MatchFixedString)
        self.comboBoxSwim[6].setCurrentIndex(index)

        '''grp9'''
        index = self.comboBoxLunches[7].findText("Period 4", QtCore.Qt.MatchFixedString)
        self.comboBoxLunches[7].setCurrentIndex(index)

        index = self.comboBoxSwim[7].findText("Period 6", QtCore.Qt.MatchFixedString)
        self.comboBoxSwim[7].setCurrentIndex(index)

        '''grp10'''
        index = self.comboBoxLunches[8].findText("Period 4", QtCore.Qt.MatchFixedString)
        self.comboBoxLunches[8].setCurrentIndex(index)

        index = self.comboBoxSwim[8].findText("Period 6", QtCore.Qt.MatchFixedString)
        self.comboBoxSwim[8].setCurrentIndex(index)

        '''checking all boxes to start'''
        for box in self.morningCheckBoxes[:-1]:
            box.setChecked(True)

        for box in self.afternoonCheckBoxes[:-1]:
            box.setChecked(True)

        '''setting the check button default to checked'''
        self.set.setChecked(True)

        '''link pressed method to generate button'''
        self.done.clicked.connect(self.pressed)

        self.retranslateUi(self, MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self.MainWindow):
        '''
        adding all the text to labels, checkbuttons
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Group Activity Scheduler"))
        self.morning.setToolTip(_translate("MainWindow", "Select the available morning activities"))
        self.morning.setStatusTip(_translate("MainWindow", "Select the available morning activities"))
        self.morning.setTitle(_translate("MainWindow", "Morning Activities"))
        self.m1.setText(_translate("MainWindow", "Soccer"))
        self.m2.setText(_translate("MainWindow", "Basketball"))
        self.m3.setText(_translate("MainWindow", "Hockey"))
        self.m4.setText(_translate("MainWindow", "Tennis"))
        self.m5.setText(_translate("MainWindow", "Volleyball"))
        self.m6.setText(_translate("MainWindow", "Ultimate"))
        self.m7.setText(_translate("MainWindow", "Squash"))
        self.m8.setText(_translate("MainWindow", "Lacrosse"))
        self.m9.setText(_translate("MainWindow", "Football"))
        self.m10.setText(_translate("MainWindow", "Softball"))
        self.mOther.setText(_translate("MainWindow", "CheckBox"))
        self.afternoon.setToolTip(_translate("MainWindow", "Select the available afternoon activities"))
        self.afternoon.setStatusTip(_translate("MainWindow", "Select the available afternoon activities"))
        self.afternoon.setTitle(_translate("MainWindow", "Afternoon Activities"))
        self.a1.setText(_translate("MainWindow", "Soccer"))
        self.a2.setText(_translate("MainWindow", "Basketball"))
        self.a3.setText(_translate("MainWindow", "Hockey"))
        self.a4.setText(_translate("MainWindow", "Tennis"))
        self.a5.setText(_translate("MainWindow", "Volleyball"))
        self.a6.setText(_translate("MainWindow", "Ultimate"))
        self.a7.setText(_translate("MainWindow", "Squash"))
        self.a8.setText(_translate("MainWindow", "Lacrosse"))
        self.a9.setText(_translate("MainWindow", "Football"))
        self.a10.setText(_translate("MainWindow", "Softball"))
        self.aOther.setText(_translate("MainWindow", "CheckBox"))

        self.set.setText(_translate("MainWindow", "Best"))

        self.g2.setTitle(_translate("MainWindow", "Group 2"))
        self.label_2.setText(_translate("MainWindow", "Lunch"))
        self.label_3.setText(_translate("MainWindow", "Swim"))
        self.groups.setTitle(_translate("MainWindow", "Number of Groups"))
        self.label.setText(_translate("MainWindow", "Enter Number of Groups"))
        self.done.setText(_translate("MainWindow", "Generate Schedule"))
        self.g3.setTitle(_translate("MainWindow", "Group 3"))
        self.label_6.setText(_translate("MainWindow", "Lunch"))
        self.label_7.setText(_translate("MainWindow", "Swim"))
        self.g4.setTitle(_translate("MainWindow", "Group 4"))
        self.label_8.setText(_translate("MainWindow", "Lunch"))
        self.label_9.setText(_translate("MainWindow", "Swim"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Group 5"))
        self.label_10.setText(_translate("MainWindow", "Lunch"))
        self.label_11.setText(_translate("MainWindow", "Swim"))
        self.g6.setTitle(_translate("MainWindow", "Group 6"))
        self.label_14.setText(_translate("MainWindow", "Lunch"))
        self.label_15.setText(_translate("MainWindow", "Swim"))
        self.g8.setTitle(_translate("MainWindow", "Group 8"))
        self.label_26.setText(_translate("MainWindow", "Lunch"))
        self.label_27.setText(_translate("MainWindow", "Swim"))
        self.g4_2.setTitle(_translate("MainWindow", "Group 9"))
        self.label_28.setText(_translate("MainWindow", "Lunch"))
        self.label_29.setText(_translate("MainWindow", "Swim"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Group 10"))
        self.label_30.setText(_translate("MainWindow", "Lunch"))
        self.label_31.setText(_translate("MainWindow", "Swim"))
        self.g7.setTitle(_translate("MainWindow", "Group 7"))
        self.label_32.setText(_translate("MainWindow", "Lunch"))
        self.label_33.setText(_translate("MainWindow", "Swim"))
        self.groupBox_set.setTitle(_translate("MainWindow", "Constraints"))

        self.best = True

        def check_valid_lunch_swim(self, n):
            '''
            This check to make sure no group has same lunch and swim
            n: number of groups
            '''
            for i in range(n-1):
                if (self.comboBoxLunches[i].currentText() == self.comboBoxSwim[i].currentText()):
                    return False
            return True
        
        def pressed(self):
            '''
            Drives the generate button, it checks if everything in GUI is valid then runs the algo
            '''
            try:
                self.groups = int(self.num_groups.text())

                if not(2 < self.groups <= 10):
                    self.error_msg_box("The number if groups must be between 2 to 10")
                elif not(self.check_valid_lunch_swim(self.groups)):
                    self.error_msg_box("No groups can have the same swim and lunch period.", "Conflicting Values")
                else:
                    self.check_best()
                    self.matrix = self.generate_matrix(self.groups)
                    self.start_time = time.time()
                    self.solve()
                    self.display_matrix()

                    make_word_doc(self.matrix, self.week.currentText())

                    if time.time() - self.start_time > 5:
                        self.error_msg_box("Unable to generate a schedule that fits the constraints.", "Schedule NOT Created")
                    else:
                        self.info_msg_box("The schedule has been generated", "Schedule Created")

            except Exception as e:
                print(e)
                self.error_msg_box("Please enter a valid number of groups.", "Incomplete Form")

        def check_best(self):
            '''
            Check if the best checkbutton is clicked and set the attribute appropriatly.
            '''
            self.best = self.set.isChecked()

        def error_msg_box(self, text, title):
            '''
            display error msg
            '''
            msg = QMessageBox()
            msg.setIcon(QMessageBox.critical)
            msg.setWindowTitle(title)
            msg.setText(text)
            x = msg.exec_()

        def info_msg_box(self, text, title):
            '''
            disp info in msg box
            '''
            msg = QMessageBox()
            msg.setIcon(QMessageBox.information)
            msg.setWindowTitle(title)
            msg.setText(text)
            x = msg.exec_()

        def get_morning_events(self):
            '''
            get events occuring in morning
            '''
            events = []
            for check in self.morningCheckBoxes:
                if check.isChecked() and check.text() != "ChecBox":
                    events.append(check.text())

            if self.morningCheckBoxes[-1].isChecked():
                if self.m_lineEdit.text() != "":
                    events.append(self.m_lineEdit.text())

            return events
        
        def get_afternoon_events(self):
            '''
            get events in afternoon
            '''
            events = []
            for check in self.afternoonCheckBoxes:
                if check.isChecked() and check.text() != "":
                    events.append(check.text())

            if self.afternoonCheckBoxes[-1].isChecked():
                if self.a_lineEdit.text() != "":
                    events.append(self.a_lineEdit.text())

            return events
        
        def generate_matrix(self, n):
            '''
            generating 3d matrix
            '''
            pass









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())






