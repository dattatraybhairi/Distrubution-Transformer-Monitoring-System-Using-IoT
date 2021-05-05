#include <WiFi.h>

#include "EmonLib.h"
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"
#include "DHT.h"

#include <LiquidCrystal_I2C.h>
/************************* WiFi Access Point *********************************/
#define WLAN_SSID       "Elonmusk"
#define WLAN_PASS       "Flamenco"
/************************* Adafruit.io Setup *********************************/
#define AIO_SERVER      "io.adafruit.com"
#define AIO_SERVERPORT  1883                   // use 8883 for SSL
#define AIO_USERNAME    "sadf"
#define AIO_KEY         "fda"
// Create an ESP8266 WiFiClient class to connect to the MQTT server.
WiFiClient client;
// Setup the MQTT client class by passing in the WiFi client and MQTT server and login details.
Adafruit_MQTT_Client mqtt(&client, AIO_SERVER, AIO_SERVERPORT, AIO_USERNAME, AIO_KEY);
// Setup a feed called 'photocell' for publishing.
// Notice MQTT paths for AIO follow the form: <username>/feeds/<feedname>
Adafruit_MQTT_Publish temperature = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/Temprature");
Adafruit_MQTT_Publish humidity = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/Humidity");
Adafruit_MQTT_Publish oil = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/oil");
Adafruit_MQTT_Publish current = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/current");
Adafruit_MQTT_Publish vibration = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/vibration");
Adafruit_MQTT_Publish voltage = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/voltage");
Adafruit_MQTT_Publish body = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/relay1");
Adafruit_MQTT_Subscribe Light1 = Adafruit_MQTT_Subscribe(&mqtt, AIO_USERNAME"/feeds/relay2"); // FeedName
/************* DHT11 Setup ********************************************/
#define DHTPIN 23
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
float h = 0;
float t = 0;
/***************************LM35*************************************/
const int analogIn = 36;
int RawValue = 0;
double Voltage = 0;
double tempC = 0;
double tempF = 0;
/*****************************Voltage And Current********************/
#define VOLT_CAL 440
#define CURRENT_CAL 18
EnergyMonitor emon1;             // Create an instance
float currentDraw = 0;
float supplyVoltage = 0;
/*************************************************************************/
// set the LCD number of columns and rows
int lcdColumns = 20;
int lcdRows = 4;
// set LCD address, number of columns and rows
// if you don't know your display address, run an I2C scanner sketch
LiquidCrystal_I2C lcd(0x27, lcdColumns, lcdRows);
/****************************ultra-sonic**************************************/
#define echoPin 19 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 18 //attach pin D3 Arduino to pin Trig of HC-SR04
// defines variables
long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement
int finalvalue = 0;
/***************************Vibration Sensor*********************************/
int vibr_Pin = 04;
long measurement = 0;
const int Relay1 = 02;
int Light1_State = 0;
/**************************************************************************/
void get_temp();
void MQTT_connect();
void get_vibration();
void get_body_temp();
void get_voltage_current();
void display();
/**************************************************************************/
void setup() {
  Serial.begin(115200);
  dht.begin();
  // initialize LCD
  lcd.init();
  // turn on LCD backlight
  lcd.backlight();

  lcd.setCursor(0, 0);
  lcd.print("    Distribution  ");
  lcd.setCursor(0, 1);
  lcd.print("    Transformer  ");
  lcd.setCursor(0, 2);
  lcd.print("     Monitoring  ");
  lcd.setCursor(0, 3);
  lcd.print("       System  ");
  delay(3000);
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  pinMode(Relay1, OUTPUT);
  Serial.println(F("Adafruit MQTT demo"));
  // Connect to WiFi access point.
  Serial.println(); Serial.println();
  Serial.print("Connecting to ");
  Serial.println(WLAN_SSID);
  WiFi.begin(WLAN_SSID, WLAN_PASS);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Connecting to");
  lcd.setCursor(0, 1);
  lcd.print(" Internet....");
  while (WiFi.status() != WL_CONNECTED) {

    delay(500);
    Serial.print(".");
  }
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(" Connected ...");
  Serial.println();
  Serial.println("WiFi connected");
  lcd.setCursor(0, 0);
  lcd.print("IP Address: ");
  lcd.setCursor(0, 1);
  lcd.print(WiFi.localIP());
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  emon1.voltage(39, VOLT_CAL, 1.7);   // Voltage: input pin, calibration, phase_shift
  emon1.current(34, CURRENT_CAL);     // Current: input pin, calibration.
  mqtt.subscribe(&Light1);
  delay(1000);
  lcd.setCursor(0, 0);
  lcd.clear();
  lcd.print(" Calibrating Sensors...");
  delay(1000);
  lcd.setCursor(0, 0);
  lcd.clear();
  lcd.print("     Wait for");
  lcd.setCursor(0, 1);
  lcd.print("       20 Seconds.");
}

void loop() {

  MQTT_connect();
  get_temp();
  get_oil_level();
  get_body_temp();
  get_voltage_current();
  get_vibration();
  display();
  get_relay();


}

void get_temp() {
  // Read humidity
  h = dht.readHumidity();
  // Read temperature as Celsius
  t = dht.readTemperature();
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
  if (distance <= 50) {
    distance = map(distance, 0, 50, 100, 0);
    Serial.print("Distance modified: ");
    Serial.print(distance);
    Serial.println(" %");
    oil.publish(distance);
    finalvalue = distance;
  }
  else {
    oil.publish("Empty");
    Serial.println("Oil Tank Empty");
    finalvalue = 0;
  }

}


void get_vibration() {
  long currentmillis = 0;
  measurement = 0;
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

void get_body_temp() {
  RawValue = analogRead(analogIn);
  Voltage = (RawValue / 2048.0) * 3300; // 5000 to get millivots.
  tempC = Voltage * 0.1;
  tempF = (tempC * 1.8) + 32; // conver to F
  Serial.print("Temperature in C = ");
  Serial.print(tempC, 1);
  Serial.print("\t Temperature in F = ");
  Serial.println(tempF, 1);
  body.publish(tempC);


}


void get_voltage_current() {

  for (int i = 0; i < 8; i++) {
    emon1.calcVI(50, 1500);        // Calculate all. No.of half wavelengths (crossings), time-out
    currentDraw     = emon1.Irms;             //extract Irms into Variable
    supplyVoltage   = emon1.Vrms;                    //extract Vrms into Variable
    Serial.print("Voltage: ");
    Serial.println(supplyVoltage);
    Serial.print("Current: ");
    Serial.println(currentDraw);
    Serial.print("Watts: ");
    Serial.println(currentDraw * supplyVoltage);
  }
  voltage.publish(supplyVoltage);
  current.publish(currentDraw);

}

void get_relay() {
  MQTT_connect();
  //  Adafruit_MQTT_Subscribe Light1 = Adafruit_MQTT_Subscribe(&mqtt, AIO_USERNAME"/feeds/relay2"); // FeedName

  Adafruit_MQTT_Subscribe *subscription;
  while ((subscription = mqtt.readSubscription(6000))) {
    if (subscription == &Light1) {
      Serial.print(F("Got: "));
      Serial.println((char *)Light1.lastread);
      Light1_State = atoi((char *)Light1.lastread);
      digitalWrite(Relay1, !(Light1_State));
    }
  }
}


void display() {

  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("Voltage:");
  lcd.setCursor(8, 0);
  lcd.print(supplyVoltage);
  lcd.setCursor(13, 0);
  lcd.print("V");
  lcd.setCursor(0, 1);
  lcd.print("Current:");
  lcd.setCursor(8, 1);
  lcd.print(currentDraw);
  lcd.setCursor(13, 1);
  lcd.print("A");


  lcd.setCursor(0, 2);
  lcd.print("TF Temp:");
  lcd.setCursor(8, 2);
  lcd.print(tempC);
  lcd.setCursor(12, 2);
  lcd.print("C");

  lcd.setCursor(0, 3);
  lcd.print("Oil Level:");
  lcd.setCursor(10, 3);
  lcd.print(finalvalue);
  lcd.setCursor(15, 3);
  lcd.print("%");

  delay(3000);

  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("EV Temp:");
  lcd.setCursor(8, 0);
  lcd.print(t);
  lcd.setCursor(12, 0);
  lcd.print("C");

  lcd.setCursor(0, 1);
  lcd.print("Humidity:");
  lcd.setCursor(9, 1);
  lcd.print(h);
  lcd.setCursor(13, 1);
  lcd.print("%");

  lcd.setCursor(0, 2);
  lcd.print("Vibration:");
  lcd.setCursor(10, 2);
  if (measurement > 100) {
    lcd.print(" Slight Humming");
  }
  else {
    lcd.print("Stable");
  }

  lcd.setCursor(0, 3);
  lcd.print("Load:");
  lcd.setCursor(6, 3);
  if (Light1_State) {
    lcd.print("OFF");
  }
  else {
    lcd.print("ON");
  }

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
