#include <WiFi.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

// Network credentials
const char* ssid = "NETGEAR38";
const char* password = "12345678";

// Raspberry Pi's IP address and port
const char* host = "192.168.1.8";
const int port = 65000;

WiFiClient client;
Adafruit_MPU6050 mpu;

void connectToWiFi() {
  Serial.print("Connecting to WiFi");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");
}

void connectToHost() {
  if (!client.connect(host, port)) {
    Serial.println("Connection to host failed, retrying...");
    delay(1000);
    ESP.restart();
  }
  Serial.println("Connected to host");
}

void setup() {
  Serial.begin(9600);
  Wire.begin();
  connectToWiFi();

  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }

  connectToHost();
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  
  Serial.print("Accel: ");
  Serial.print(a.acceleration.x);
  Serial.print(", ");
  Serial.print(a.acceleration.y);
  Serial.print(", ");
  Serial.println(a.acceleration.z);

  Serial.print("Gyro: ");
  Serial.print(g.gyro.x);
  Serial.print(", ");
  Serial.print(g.gyro.y);
  Serial.print(", ");
  Serial.println(g.gyro.z);




  if (client.connected()) {
    char data[256];
snprintf(data, sizeof(data), "%.3f,%.3f,%.3f,%.3f,%.3f,%.3f",
         a.acceleration.x, a.acceleration.y, a.acceleration.z,
         g.gyro.x, g.gyro.y, g.gyro.z);

client.print(data);

  } else {
    Serial.println("Lost connection to host");
    connectToHost();
  }

  delay(10); // Adjust the delay as needed
}