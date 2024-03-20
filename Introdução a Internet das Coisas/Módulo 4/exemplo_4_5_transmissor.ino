#include <SoftwareSerial.h>
 
#define BTN1  4
 
SoftwareSerial loraSerial(2, 3); // TX, RX
 
String turnOn = "on";
String turnOff = "off";
 
 
void setup() {
 pinMode(BTN1, INPUT_PULLUP);
 Serial.begin(9600);
 Serial.print("Lora-Test");
 loraSerial.begin(9600);
 
}
void loop() {
Serial.println(digitalRead(BTN1));
 if(digitalRead(BTN1) == 0) {
   loraSerial.print(turnOn);
   while(digitalRead(BTN1) == 0);
   delay(50);
 }else{
   loraSerial.print(turnOff);
   while(digitalRead(BTN1) == 1);
 }
 delay(1000);
}