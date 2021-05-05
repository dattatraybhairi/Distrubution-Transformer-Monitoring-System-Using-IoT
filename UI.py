from Adafruit_IO import MQTTClient
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore, QtGui, QtWidgets

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = '846e3070c6f144efa0d3b62d5b583775'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'chota_scientists'

TEMPERATURE = 'temprature'  # topic for temperature
HUMIDITY = 'humidity'  # topic for humidity
v = 'voltage'
CURRENT = 'current'
OIL = 'oil'
VIBRATION = 'vibration'


# Define callback functions which will be called when certain events happen.
def connected(client):
    """Connected function will be called when the client is connected to
    Adafruit IO.This is a good place to subscribe to feed changes.  The client
    parameter passed to this function is the Adafruit IO MQTT client so you
    can make calls against it easily.
    """
    # Subscribe to changes on a feed named Counter.
    ui.ClicktoConnect.setText("Connecting to the server...")
    print('Subscribing to Feed {0}'.format(TEMPERATURE))
    client.subscribe(TEMPERATURE)
    print('Subscribing to Feed {0}'.format(HUMIDITY))
    client.subscribe(HUMIDITY)
    print('Subscribing to Feed {0}'.format(v))
    client.subscribe(v)
    print('Subscribing to Feed {0}'.format(CURRENT))
    client.subscribe(CURRENT)
    print('Subscribing to Feed {0}'.format(OIL))
    client.subscribe(OIL)
    print('Subscribing to Feed {0}'.format(VIBRATION))
    client.subscribe(VIBRATION)
    ui.ClicktoConnect.setText("        Loading Data ")


def disconnected(client):
    """Disconnected function will be called when the client disconnects."""
    ui.ConnectButton.setText("Disconnected")
    # sys.exit(1)


class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.setWindowIcon(QIcon("./logo.ico"))
        Dashboard.resize(541, 315)
        font = QtGui.QFont()
        font.setPointSize(18)
        Dashboard.setFont(font)
        Dashboard.setStyleSheet("QWidget{\n"
                                "\n"
                                "background-color:rgb(240, 240, 240)\n"
                                "}")
        self.Headline = QtWidgets.QLabel(Dashboard)
        self.timer = QTimer(Dashboard)
        self.Headline.setGeometry(QtCore.QRect(40, 30, 471, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Headline.setFont(font)
        self.Headline.setObjectName("Headline")

        self.ConnectButton = QtWidgets.QPushButton(Dashboard)
        self.ConnectButton.setGeometry(QtCore.QRect(230, 265, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ConnectButton.setFont(font)
        self.ConnectButton.setObjectName("ConnectButton")
        self.ConnectButton.clicked.connect(self.connect_clicked)
        self.ClicktoConnect = QtWidgets.QLabel(Dashboard)
        self.ClicktoConnect.setGeometry(QtCore.QRect(211, 241, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ClicktoConnect.setFont(font)
        self.ClicktoConnect.setObjectName("ClicktoConnect")
        self.layoutWidget = QtWidgets.QWidget(Dashboard)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 90, 511, 121))
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

        # self.timer.timeout.connect(self.update)
        # self.timer.setInterval(5)
        # self.timer.start()

        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)

    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        # self.Dashboard.setObjectName("Registration")
        self.Headline.setText("Distrubution Transformer Moniter Dashboard")
        self.ConnectButton.setText(_translate("Dashboard", "Connect "))
        self.ClicktoConnect.setText(_translate("Dashboard", "Click to Connect Device"))
        self.Voltag_head.setText(_translate("Dashboard", "Voltage :"))
        self.voltage_label.setText(_translate("Dashboard", """"""))
        self.Temp_head.setText(_translate("Dashboard", "Temperature :"))
        self.temp_label.setText(_translate("Dashboard", """"""))
        self.oil_head.setText(_translate("Dashboard", "Oil Level :"))
        self.oil_lable.setText(_translate("Dashboard", """"""))
        self.Current_head.setText(_translate("Dashboard", "Current :"))
        self.Current_label.setText(_translate("Dashboard", ""))
        self.Humi_head.setText(_translate("Dashboard", "Humidity :"))
        self.humidity_label.setText(_translate("Dashboard", ""))
        self.vibration_head.setText(_translate("Dashboard", "Vibration :"))
        self.vibration_label.setText(_translate("Dashboard", ""))

    def connect_clicked(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        self.ConnectButton.setText(_translate("Dashboard", "Connected "))
        self.ClicktoConnect.setText(_translate("Dashboard", "Wait for few Seconds"))
        client.connect(keepalive=60)
        client.loop_background()

    def update(self, feed_id):
        # self.voltage_label.setText(str(self.count+1))
        # self.Current_label.setText("1a")

        self.temp_label.setText()
        self.humidity_label.setText()
        # self.vibration_label.setText( "Stable")
        # self.oil_lable.setText("full")


def message(client, feed_id, payload):
    """Message function will be called when a subscribed feed has a new value.
    The feed_id parameter identifies the feed, and the payload parameter has
    the new value.
    """
    ui.ClicktoConnect.setText("")
    if feed_id == TEMPERATURE:
        print(payload)
        ui.temp_label.setText(payload + " °C")

    if feed_id == HUMIDITY:
        print(payload)
        ui.humidity_label.setText(payload + " %")

    if feed_id == OIL:
        print(payload)
        ui.oil_lable.setText(payload + " %")

    if feed_id == v:
        print(payload)
        ui.voltage_label.setText(payload + " Volts")

    if feed_id == CURRENT:
        print(payload)
        ui.Current_label.setText(payload + " mAmps")

    if feed_id == VIBRATION:
        if int(payload) >= 100:
            print("Slight Movement")
            ui.vibration_label.setText("Slight Vibration")
        else:
            print("Stable")
            ui.vibration_label.setText("Stable")


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
# Setup the callback functions defined above.
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message

# Connect to the Adafruit IO server.


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dashboard = QtWidgets.QWidget()
    ui = Ui_Dashboard()
    ui.setupUi(Dashboard)
    Dashboard.show()
    sys.exit(app.exec())
