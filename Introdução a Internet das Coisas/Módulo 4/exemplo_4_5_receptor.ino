#include <SoftwareSerial.h>
 
#define buzzer  4 
 
SoftwareSerial loraSerial(2, 3); // TX, RX
 
void setup() {
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
  loraSerial.begin(9600); 
}
 
void loop() {
  if(loraSerial.available() > 1){
    String input = loraSerial.readString();
    Serial.println(input); 
    if(input == "on") {
      digitalWrite(buzzer, HIGH); 
    }
    if(input == "off") {
      digitalWrite(buzzer, LOW);
    }
  }
  delay(20);
}