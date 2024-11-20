#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

// Pin definitions
#define DHTPIN 23       // GPIO pin connected to the DHT sensor (e.g., GPIO 21)
#define DHTTYPE DHT11    // DHT sensor type (DHT11, DHT22)

LiquidCrystal_I2C lcd(0x27, 16, 2);  // I2C address and LCD size
DHT dht(DHTPIN, DHTTYPE);            // Initialize DHT sensor

void setup() {
  // Start serial communication
  Serial.begin(115200);

  // Initialize DHT sensor
  dht.begin();

  // Initialize LCD
  lcd.begin();
  lcd.backlight();  // Turn on LCD backlight

  // Print welcome message to the serial monitor
  Serial.println("DHT11 Sensor with ESP32");

  // Print message on the LCD
  lcd.setCursor(0, 0);
  lcd.print("Reading...");
}

void loop() {
  // Read humidity and temperature from DHT sensor
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // Check if the readings are valid
  if (isnan(humidity) || isnan(temperature)) {
    // Error handling if reading failed
    lcd.setCursor(0, 0);
    lcd.print("Error Reading DHT");

    Serial.println("Failed to read from DHT sensor!");
  }
  else {
    // Display the readings on the LCD
    lcd.setCursor(0, 0);
    lcd.print("Humidity: ");
    lcd.print(humidity);
    lcd.print(" %");

    lcd.setCursor(0, 1);
    lcd.print("Temp: ");
    lcd.print(temperature);
    lcd.print(" C");

    // Output the readings to the Serial Monitor
    Serial.print("Humidity: ");
    Serial.print(humidity);
    Serial.print(" %\t");
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.println(" C");
  }

  // Wait 5 seconds before taking another reading
  delay(5000);
  lcd.clear();  // Clear the LCD for next reading
}
