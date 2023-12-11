#include <Arduino.h>

const int buttonPin = 15; // the number of the pushbutton pin
const int ledPin =  18;   // the number of the LED pin

void setup() {
  pinMode(buttonPin, INPUT_PULLUP); // Initialize the button pin as a pull-up input
  pinMode(ledPin, OUTPUT);          // Initialize the LED pin as an output
}

void loop() {
  // Check if button is pressed.
  // If the button is pressed (buttonPin reads LOW because of INPUT_PULLUP configuration),
  // turn on the LED. Otherwise, turn it off.
  if (digitalRead(buttonPin) == LOW) {
    // Turn on the LED
    digitalWrite(ledPin, HIGH);
  } else {
    // Turn off the LED
    digitalWrite(ledPin, LOW);
  }
}


