from machine import Pin, Timer
from time import sleep_ms
import ubluetooth #biblioteca para utilização do BLE

class BLE():
    def __init__(self, name):   
        self.name = name
        #Instanciando a classe BLE do ubluetooth
        self.ble = ubluetooth.BLE()
        #Ativando o BLE
        self.ble.active(True)

        #Definição do LED e dos Timers
        self.led = Pin(2, Pin.OUT)
        self.timer1 = Timer(0)
        self.timer2 = Timer(1)
        
        #Atribuição das possíveis estágios da app
        self.disconnected()
        self.ble.irq(self.ble_irq)
        self.register()
        self.advertiser()

    def register(self):        
        # Nordic UART Service (NUS)
        NUS_UUID = '6E400001-B5A3-F393-E0A9-E50E24DCCA9E'
        RX_UUID = '6E400002-B5A3-F393-E0A9-E50E24DCCA9E'
        TX_UUID = '6E400003-B5A3-F393-E0A9-E50E24DCCA9E'
        
        # Definição do UUID do serviço
        BLE_NUS = ubluetooth.UUID(NUS_UUID)

        # Definição da característica RX
        BLE_RX = (ubluetooth.UUID(RX_UUID), ubluetooth.FLAG_WRITE)

        # Definição da característica TX
        BLE_TX = (ubluetooth.UUID(TX_UUID), ubluetooth.FLAG_NOTIFY)
        
        # Definição do serviço    
        BLE_UART = (BLE_NUS, (BLE_TX, BLE_RX,))

        # Lista de serviços, no nosso caso apenas um
        SERVICES = (BLE_UART, )

        # Registro dos serviços no perfil
        ((self.tx, self.rx,), ) = self.ble.gatts_register_services(SERVICES)
    
        #Método para envio de dados
    def send(self, data):
        self.ble.gatts_notify(0, self.tx, data + '\n')

    #Método para entra no modo de 'advertise'
    def advertiser(self):
        name = bytes(self.name, 'UTF-8')
        self.ble.gap_advertise(100, bytearray('\x02\x01\x02') + bytearray((len(name) + 1, 0x09)) + name)
    
    #Método para resetar os timers (temporizadores)
    def connected(self):        
        self.timer1.deinit()
        self.timer2.deinit()

    #Método que inicializa os temporizadores para indicação luminosa dos LEDs
    def disconnected(self):        
        self.timer1.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: self.led(1))
        sleep_ms(200)
        self.timer2.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: self.led(0))   

    #Método de interrupção para verificação dos estágios do BLE
    def ble_irq(self, event, data):
        # Dispositivo conectado
        if event == 1:
            self.connected()
            self.led(1)

        # Dispositivo desconectado
        elif event == 2:
            '''Central disconnected'''
            self.advertiser()
            self.disconnected()

        # Nova mensagem recebida
        elif event == 3:            
            buffer = self.ble.gatts_read(self.rx)
            message = buffer.decode('UTF-8').strip()
            print(message)            
            if message == 'red_led':
                red_led.value(not red_led.value())
                print('red_led', red_led.value())
                ble.send('red_led' + str(red_led.value()))