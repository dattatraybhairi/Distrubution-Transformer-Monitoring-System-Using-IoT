#include <ESP8266WiFi.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"
#include "DHT.h"
/************************* WiFi Access Point *********************************/
#define WLAN_SSID       "Elonmusk"
#define WLAN_PASS       "Flamenco"
/************************* Adafruit.io Setup *********************************/
#define AIO_SERVER      "io.adafruit.com"
#define AIO_SERVERPORT  1883                   // use 8883 for SSL
#define AIO_USERNAME    "chota_scientists"
#define AIO_KEY         "846e3070c6f144efa0d3b62d5b583775"
/************* DHT11 Setup ********************************************/
#define DHTPIN D4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);
/************ Global State (you don't need to change this!) ******************/
// Create an ESP8266 WiFiClient class to connect to the MQTT server.
WiFiClient client;
// or... use WiFiFlientSecure for SSL
//WiFiClientSecure client;
// Setup the MQTT client class by passing in the WiFi client and MQTT server and login details.
Adafruit_MQTT_Client mqtt(&client, AIO_SERVER, AIO_SERVERPORT, AIO_USERNAME, AIO_KEY);
/****************************** Feeds ***************************************/
// Setup a feed called 'photocell' for publishing.
// Notice MQTT paths for AIO follow the form: <username>/feeds/<feedname>
Adafruit_MQTT_Publish temperature = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/Temprature");
Adafruit_MQTT_Publish humidity = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/Humidity");
Adafruit_MQTT_Publish oil = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/oil");
Adafruit_MQTT_Publish current = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/current");
Adafruit_MQTT_Publish vibration = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/vibration");
Adafruit_MQTT_Publish voltage = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/voltage");

/****************************ultra-sonic**************************************/
#define echoPin D5 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin D6 //attach pin D3 Arduino to pin Trig of HC-SR04
// defines variables
long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement
/***************************Vibration Sensor*********************************/
int vibr_Pin = D0;
long measurement = 0;
/***************************Current Sensor***********************************/
const int currentPin = A0;
int sensitivity = 66;
int adcValue = 0;
int offsetVoltage = 2500;
double adcVoltage = 0;
double currentValue = 0;
/*************************** Sketch Code ************************************/

void MQTT_connect();
void oil_level();
void temp();

void setup() {
  Serial.begin(115200);
  dht.begin();
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  Serial.println(F("Adafruit MQTT demo"));
  // Connect to WiFi access point.
  Serial.println(); Serial.println();
  Serial.print("Connecting to ");
  Serial.println(WLAN_SSID);
  WiFi.begin(WLAN_SSID, WLAN_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.println("WiFi connected");
  Serial.println("IP address: "); Serial.println(WiFi.localIP());
}




void loop() {
  // Ensure the connection to the MQTT server is alive (this will make the first
  // connection and automatically reconnect when disconnected).  See the MQTT_connect
  // function definition further below.
  MQTT_connect();
  get_temp();
  get_curent();
  get_oil_level();
  get_vibration();
  delay(15000);
}



void get_temp() {
  // Read humidity
  float h = dht.readHumidity();
  // Read temperature as Celsius
  float t = dht.readTemperature();
  //publish temperature and humidity
  Serial.print(F("\nTemperature: "));
  Serial.print(t);
  Serial.print(F("\nHumidity: "));
  Serial.println(h);
  temperature.publish(t);
  humidity.publish(h);
}

void get_oil_level()
{
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  oil.publish(distance);
}

void get_vibration() {
  long currentmillis = 0;
  measurement=0;
  currentmillis = millis();
  while (millis() - currentmillis < 100) {
    for (int i = 0; i < 10; i++) {
      measurement += pulseIn (vibr_Pin, HIGH); //wait for the pin to get HIGH and returns measurement
    }
  }
  Serial.print("Vibration : ");
  Serial.println(measurement / 5);
  vibration.publish(int(measurement / 5));
}

void get_curent()
{
  adcValue = analogRead(currentPin);
  adcVoltage = (adcValue / 1024.0) * 5000;
  currentValue = ((adcVoltage - offsetVoltage) / sensitivity);
  Serial.print("current : ");
  Serial.print(currentValue);
  Serial.println(" mA");
  Serial.print("Voltage: ");
  Serial.print(adcVoltage);
  Serial.println(" Volts");
  current.publish(currentValue);
  voltage.publish(adcVoltage);
}

void MQTT_connect() {
  int8_t ret;
  // Stop if already connected.
  if (mqtt.connected()) {
    return;
  }
  Serial.print("Connecting to MQTT... ");
  uint8_t retries = 3;
  while ((ret = mqtt.connect()) != 0) { // connect will return 0 for connected
    Serial.println(mqtt.connectErrorString(ret));
    Serial.println("Retrying MQTT connection in 5 seconds...");
    mqtt.disconnect();
    delay(5000);  // wait 5 seconds
    retries--;
    if (retries == 0) {
      // basically die and wait for WDT to reset me
      while (1);
    }
  }
  Serial.println("MQTT Connected!");
}
