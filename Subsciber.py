# 
# Install
# - sudo pip3 install adafruit-blinka
# - sudo pip3 install adafruit-io
# 

# Import standard python modules.
import sys
import time

# This example uses the MQTTClient instead of the REST client
from Adafruit_IO import MQTTClient

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = '846e3070c6f144efa0d3b62d5b583775'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'chota_scientists'

TEMPERATURE = 'Temprature'  # topic for temperature
HUMIDITY = 'Humidity'  # topic for humidity


# Define callback functions which will be called when certain events happen.
def connected(client):
    """Connected function will be called when the client is connected to
    Adafruit IO.This is a good place to subscribe to feed changes.  The client
    parameter passed to this function is the Adafruit IO MQTT client so you
    can make calls against it easily.
    """
    # Subscribe to changes on a feed named Counter.
    print('Subscribing to Feed {0}'.format(TEMPERATURE))
    client.subscribe(TEMPERATURE)
    print('Subscribing to Feed {0}'.format(HUMIDITY))
    client.subscribe(HUMIDITY)


def disconnected(client):
    """Disconnected function will be called when the client disconnects."""
    sys.exit(1)


def message(client, feed_id, payload):
    """Message function will be called when a subscribed feed has a new value.
    The feed_id parameter identifies the feed, and the payload parameter has
    the new value.
    """
    if feed_id == TEMPERATURE:
        print(payload)
    if feed_id == HUMIDITY:
        print(payload)



# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message

# Connect to the Adafruit IO server.
client.connect(keepalive=60)

# The first option is to run a thread in the background so you can continue
# doing things in your program.
client.loop_background()
# client.loop_start()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dashboard = QtWidgets.QWidget()
    ui = Ui_Dashboard()
    # timer1 = QtCore.QTimer()
    # timer1.timeout.connect(ui.update)
    # timer1.setInterval(1000)
    # timer1.start()
    ui.setupUi(Dashboard)
    Dashboard.show()
    sys.exit(app.exec())
