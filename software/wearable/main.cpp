#include <Wire.h>
#include <I2Cdev.h>
#include <MPU6050.h>

MPU6050 mpu;
int16_t ax, ay, az;
int16_t gx, gy, gz;

int valMotor1;
int valMotor2;

void setup() {
  Wire.begin();
  Serial.begin(9600);
  Serial.println("Initialize MPU");
  mpu.initialize();
  Serial.println(mpu.testConnection() ? "Connected" : "Connection failed");
}

void loop() {
  // Read the accelerometer and gyroscope values
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

  // Map the accelerometer x-axis reading to a value between -125 and 125
  ax = map(ax, -17000, 17000, -125, 125);

  // Calculate the motor values based on the x-axis accelerometer value
  valMotor1 = 125 + ax; // Equivalent to the previous speed for motor1
  valMotor2 = 125 - ax; // Equivalent to the previous speed for motor2

  // Print the calculated values to the serial monitor
  Serial.print("Motor 1 Speed: ");
  Serial.println(valMotor1);
  Serial.print("Motor 2 Speed: ");
  Serial.println(valMotor2);

  // The rest of the code that deals with the motor control has been removed
  // as you have requested to use the values for display purposes instead.

  delay(200); // A short delay before the next loop iteration
}
