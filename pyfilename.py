# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore, QtGui, QtWidgets
class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(565, 282)
        Dashboard.setMinimumSize(QtCore.QSize(565, 282))
        Dashboard.setMaximumSize(QtCore.QSize(565, 282))
        font = QtGui.QFont()
        font.setPointSize(18)
        Dashboard.setFont(font)
        Dashboard.setStyleSheet("QWidget{\n"
                                "\n"
                                "background-color:rgb(240, 240, 240)\n"
                                "}")
        self.Headline = QtWidgets.QLabel(Dashboard)
        self.Headline.setGeometry(QtCore.QRect(40, 10, 471, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Headline.setFont(font)
        self.Headline.setObjectName("Headline")
        self.ConnectButton = QtWidgets.QPushButton(Dashboard)
        self.ConnectButton.setGeometry(QtCore.QRect(239, 234, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ConnectButton.setFont(font)
        self.ConnectButton.setObjectName("ConnectButton")
        self.ClicktoConnect = QtWidgets.QLabel(Dashboard)
        self.ClicktoConnect.setGeometry(QtCore.QRect(220, 210, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ClicktoConnect.setFont(font)
        self.ClicktoConnect.setObjectName("ClicktoConnect")
        self.layoutWidget = QtWidgets.QWidget(Dashboard)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 60, 511, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Voltag_head = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Voltag_head.setFont(font)
        self.Voltag_head.setObjectName("Voltag_head")
        self.horizontalLayout_4.addWidget(self.Voltag_head)
        self.voltage_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.voltage_label.setFont(font)
        self.voltage_label.setObjectName("voltage_label")
        self.horizontalLayout_4.addWidget(self.voltage_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Temp_head = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Temp_head.setFont(font)
        self.Temp_head.setObjectName("Temp_head")
        self.horizontalLayout_5.addWidget(self.Temp_head)
        self.temp_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.temp_label.setFont(font)
        self.temp_label.setObjectName("temp_label")
        self.horizontalLayout_5.addWidget(self.temp_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.oil_head = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.oil_head.setFont(font)
        self.oil_head.setObjectName("oil_head")
        self.horizontalLayout_6.addWidget(self.oil_head)
        self.oil_lable = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.oil_lable.setFont(font)
        self.oil_lable.setObjectName("oil_lable")
        self.horizontalLayout_6.addWidget(self.oil_lable)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Current_head = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Current_head.setFont(font)
        self.Current_head.setObjectName("Current_head")
        self.horizontalLayout_3.addWidget(self.Current_head)
        self.Current_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Current_label.setFont(font)
        self.Current_label.setObjectName("Current_label")
        self.horizontalLayout_3.addWidget(self.Current_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Humi_head = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Humi_head.setFont(font)
        self.Humi_head.setObjectName("Humi_head")
        self.horizontalLayout_2.addWidget(self.Humi_head)
        self.humidity_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.humidity_label.setFont(font)
        self.humidity_label.setObjectName("humidity_label")
        self.horizontalLayout_2.addWidget(self.humidity_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vibration_head = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vibration_head.setFont(font)
        self.vibration_head.setObjectName("vibration_head")
        self.horizontalLayout.addWidget(self.vibration_head)
        self.vibration_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vibration_label.setFont(font)
        self.vibration_label.setObjectName("vibration_label")
        self.horizontalLayout.addWidget(self.vibration_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)

    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dashboard.setWindowTitle(_translate("Dashboard", "Dashboard"))
        self.Headline.setText(_translate("Dashboard", "Distrubution Transformer Monitoring Dashboard"))
        self.ConnectButton.setText(_translate("Dashboard", "Connect "))
        self.ClicktoConnect.setText(_translate("Dashboard", "Click to Connect Device"))
        self.Voltag_head.setText(_translate("Dashboard", "Voltage :"))
        self.voltage_label.setText(_translate("Dashboard", "TextLabel"))
        self.Temp_head.setText(_translate("Dashboard", "Temperature :"))
        self.temp_label.setText(_translate("Dashboard", "TextLabel"))
        self.oil_head.setText(_translate("Dashboard", "Oil Level :"))
        self.oil_lable.setText(_translate("Dashboard", "TextLabel"))
        self.Current_head.setText(_translate("Dashboard", "Current :"))
        self.Current_label.setText(_translate("Dashboard", "TextLabel"))
        self.Humi_head.setText(_translate("Dashboard", "Humidity :"))
        self.humidity_label.setText(_translate("Dashboard", "TextLabel"))
        self.vibration_head.setText(_translate("Dashboard", "Vibration :"))
        self.vibration_label.setText(_translate("Dashboard", "TextLabel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QWidget()
    ui = Ui_Dashboard()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec())
