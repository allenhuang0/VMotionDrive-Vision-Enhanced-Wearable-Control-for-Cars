#include <WiFi.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

// Replace with your network credentials
const char* ssid = "NETGEAR47";
const char* password = "littlebolt654";

// Replace with the Raspberry Pi's IP address and the port number
const char* host = "10.0.0.20";
const int port = 65124;

WiFiClient client;
Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  Wire.begin();
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("WiFi connected");

  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }

  // Connect to Raspberry Pi
  if (!client.connect(host, port)) {
    Serial.println("Connection to host failed");
    delay(1000);
    ESP.restart();
  }
}

void loop() {
  /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  if (client.connected()) {
    client.print("Accel X: "); client.print(a.acceleration.x); client.print(" ");
    client.print("Y: "); client.print(a.acceleration.y); client.print(" ");
    client.print("Z: "); client.println(a.acceleration.z);

    client.print("Gyro X: "); client.print(g.gyro.x); client.print(" ");
    client.print("Y: "); client.print(g.gyro.y); client.print(" ");
    client.print("Z: "); client.println(g.gyro.z);

    client.print("Temp: "); client.println(temp.temperature);
  } else { Serial.println("Lost connection. Attempting to reconnect...");
    client.connect(host, port);
  }

  delay(1000); // Adjust based on how often you want to send data
}

