#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>
#define DHTPIN A2
#define DHTTYPE DHT11

LiquidCrystal_I2C lcd(0x27, 16, 2);
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  dht.begin();
  lcd.begin();         // initialize the lcd
  lcd.backlight();  
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)){
    lcd.setCursor(0, 0);
    lcd.print("FUCK YOU!!");
  }
  else{
    lcd.setCursor(0, 0);
    lcd.print("Humidity: ");
    lcd.print(humidity);
    lcd.setCursor(0, 1);
    lcd.print("Temp: ");
    lcd.print(temperature);
    lcd.print(" ");
    lcd.print("(C)");
  }

  delay(5000);
  lcd.clear();
}
