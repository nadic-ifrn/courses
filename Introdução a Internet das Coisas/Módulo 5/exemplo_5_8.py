import network
import time
from machine import Pin
import dht
import ujson
from umqtt.simple import MQTTClient

#MQTT Server Parameters
MQTT_CLIENT_ID = "micropython-weather-demo"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC     = "wokwi-weather-cepedi"

sensor = dht.DHT22(Pin(15))

print("Connectando ao WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
 print(".", end="")
 time.sleep(0.1)
print(" Conectado!")

print("Conectando ao servidor MQTT... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.connect()

print("Conectado!")

prev_weather = ""
while True:
 print("Medindo condições climáticas... ", end="")
 sensor.measure()
 message = ujson.dumps({
   "temp": sensor.temperature(),
   "humidity": sensor.humidity(),
 })
 if message != prev_weather:
   print("Atualizando!")
   print("Enviando para tópico MQTT {}: {}".format(MQTT_TOPIC, message))
   client.publish(MQTT_TOPIC, message)
   prev_weather = message
 else:
   print("Sem mudanças!")
 time.sleep(1)