#importamos as bibliotecas machine e time
import Pin from machine
import time

#definimos o nosso pino de saída (onde o LED está ligado) 
led = Pin(2, Pin.OUT)
#definimos um laço de repetição infinito que funciona da mesma forma da função loop no c++
while True:
    #mudamos a porta para nível alto.
    led.on()
    #esperamos 1 segundo
    time.sleep(1)
    #mudamos a porta para nível baixo
    led.off()
    #esperamos 1 segundo
    time.sleep(1)