#include <Adafruit_ILI9341.h>
#define TFT_DC 2
#define TFT_CS 15
Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC);
void setup() {
 tft.begin();
 tft.setRotation(1);
 tft.setTextColor(ILI9341_WHITE);
 tft.setTextSize(2);
 tft.print("Hello IoT");
}


void loop() {}