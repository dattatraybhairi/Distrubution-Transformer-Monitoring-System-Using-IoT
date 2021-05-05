import PyQt6.sip
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon
from Help import Ui_Help
from Delete_succes import Ui_Delete_window
from Eported import Ui_Eported_window
import re, csv
import os
import getpass

# taking the username
uName = getpass.getuser()

# defining the file path and name
pathPy = "C:/Users/" + uName + "/Documents/data.csv"

fields = ['asset_Id', 'physical_Id']
with open(pathPy, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(fields)


class Ui_Registration(object):
    def __init__(self):
        self.Help_button = QtWidgets.QPushButton(Registration)
        self.Asset_mac_line_edit = QtWidgets.QLineEdit(Registration)
        self.physical_id_line_edit = QtWidgets.QLineEdit(Registration)
        self.physical_id_save_button = QtWidgets.QPushButton(Registration)
        self.delete_entries_button = QtWidgets.QPushButton(Registration)
        self.export_data = QtWidgets.QPushButton(Registration)
        self.help_ui = Ui_Help()
        self.delete_ui = Ui_Delete_window()
        self.exported_ui = Ui_Eported_window()
        self.help_view = QtWidgets.QMainWindow()
        self.delete_view = QtWidgets.QMainWindow()
        self.export_view = QtWidgets.QMainWindow()
        self.Main_titile = QtWidgets.QLabel(Registration)
        self.physical_hidden_label = QtWidgets.QLabel(Registration)
        self.physical_id_label = QtWidgets.QLabel(Registration)
        self.asse_mac_label = QtWidgets.QLabel(Registration)
        self.LOGO = QtWidgets.QLabel(Registration)
        self.timer = QTimer(Registration)

    def help_window(self):
        self.help_ui.setupUi(self.help_view)
        self.help_view.show()

    def delete_window(self):
        self.delete_ui.setupUi(self.delete_view)
        self.delete_view.show()
        self.delete_entries()

    def exported_window(self):
        self.exported_ui.setupUi(self.export_view)
        self.export_view.show()

    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.setWindowIcon(QIcon("./blue.ico"))
        Registration.setEnabled(True)
        Registration.resize(440, 308)
        Registration.setStyleSheet("QWidget{\n"
                                   "\n"
                                   "    background-color: rrgb(240, 240, 240)\n"
                                   "}")
        self.Main_titile.setGeometry(QtCore.QRect(10, 10, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Main_titile.setFont(font)
        self.Main_titile.setStyleSheet("QLabel{\n"
                                       "    background-color: rgba(0, 0, 0, 0.0);\n"
                                       "}\n"
                                       "")
        self.Main_titile.setObjectName("Main_titile")
        self.Help_button.setGeometry(QtCore.QRect(350, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(8)
        self.Help_button.setFont(font)
        self.Help_button.setStyleSheet("QPushButton{\n"
                                       "background-color: \"#006287\";\n"
                                       "color:rgb(255, 255, 255)\n"
                                       "}\n"
                                       "")
        self.Help_button.setObjectName("Help_button")
        self.Help_button.clicked.connect(self.help_window)
        self.LOGO.setGeometry(QtCore.QRect(30, 260, 121, 31))
        self.LOGO.setStyleSheet("image:url(:/newPrefix/Logo_Blue.png)")
        self.LOGO.setText("")
        self.LOGO.setObjectName("LOGO")
        self.Asset_mac_line_edit.setGeometry(QtCore.QRect(40, 80, 341, 31))
        self.Asset_mac_line_edit.setObjectName("Asset_mac_line_edit")
        self.physical_id_line_edit.setGeometry(QtCore.QRect(40, 140, 341, 31))
        self.physical_id_line_edit.setObjectName("physical_id_line_edit")
        self.physical_id_save_button.setGeometry(QtCore.QRect(40, 210, 61, 23))
        self.physical_id_save_button.setObjectName("physical_id_save_button")
        self.physical_id_save_button.clicked.connect(self.asset_save_clicked)
        self.asse_mac_label.setGeometry(QtCore.QRect(40, 60, 261, 16))
        self.asse_mac_label.setObjectName("asse_mac_label")
        self.physical_id_label.setGeometry(QtCore.QRect(40, 120, 261, 16))
        self.physical_id_label.setObjectName("physical_id_label")
        self.delete_entries_button.setGeometry(QtCore.QRect(240, 260, 81, 23))
        self.delete_entries_button.setObjectName("delete_entries_button")
        self.delete_entries_button.clicked.connect(self.delete_window)
        self.export_data.setGeometry(QtCore.QRect(340, 260, 75, 23))
        self.export_data.setObjectName("export_data")
        self.export_data.clicked.connect(self.exported_window)
        self.physical_hidden_label.setGeometry(QtCore.QRect(40, 180, 261, 16))
        self.physical_hidden_label.setText("")
        self.physical_hidden_label.setObjectName("physical_hidden_label")
        self.timer.timeout.connect(self.clear_hidden_text)

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def asset_save_clicked(self):
        textInput1 = self.Asset_mac_line_edit.text()
        textInput2 = self.physical_id_line_edit.text()
        # check = re.search(
        #     "^[a-z A-Z 0-9]{2}-[a-z A-Z 0-9]{2}-[a-z A-Z 0-9]{2}-[a-z A-Z 0-9]{2}-[a-z A-Z 0-9]{2}-[a-z A-Z 0-9]{2}",
        #     textInput1)
        # #print(check)
        if len(textInput1) and len(textInput2):
            self.physical_hidden_label.setStyleSheet("color:rgb(0, 0, 0)")
            self.physical_hidden_label.setText("Saved :" + textInput1)
            self.Asset_mac_line_edit.clear()
            self.physical_id_line_edit.clear()
            # print(textInput1)
            self.timer.start(1000)
            fields = [textInput1, textInput2]
            with open(pathPy, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(fields)
        else:
            self.physical_hidden_label.setStyleSheet("color:rgb(255, 0, 0)")
            self.physical_hidden_label.setText("Please Enter Data Fields")
            self.Asset_mac_line_edit.clear()
            self.physical_id_line_edit.clear()

    def clear_hidden_text(self):
        self.physical_hidden_label.setText("")

    def delete_entries(self):
        fields = ['asset_Id', 'physical_Id']
        with open(pathPy, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Registration "))
        self.Main_titile.setText(_translate("Registration", "Asset Registration Window"))
        self.Help_button.setText(_translate("Registration", "Help"))
        self.physical_id_save_button.setText(_translate("Registration", "Save"))
        self.asse_mac_label.setText(_translate("Registration", "Enter/Scan Asset ID:"))
        self.physical_id_label.setText(_translate("Registration", "Enter/Scan Physical Asset ID:"))
        self.delete_entries_button.setText(_translate("Registration", "Delete Entries"))
        self.export_data.setText(_translate("Registration", "Export Data"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QWidget()
    ui = Ui_Registration()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec())
