import umqtt.robust
import time
import random

easymqtt_session = "ng01vt";
easymqtt_client = umqtt.robust.MQTTClient("umqtt_client", server = "bipes.net.br", port = 1883, user = "bipes", password = "m8YLUr5uW3T");
easymqtt_client.connect()
print("EasyMQTT connected")
while(True):
  value = random.randint(0,10)
  easymqtt_client.publish(easymqtt_session + "/" + 'teste', str(value))
  print("EasyMQTT Publish - Session:",easymqtt_session,"Topic:",'teste',"Value:",str(value))
  time.sleep(1)