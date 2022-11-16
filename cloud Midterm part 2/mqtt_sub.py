import json
import time
import paho.mqtt.client as paho

broker="10.20.1.95"
def on_message(client, userdata, message):
    time.sleep(1)
    topic=message.topic
    m_decode = str(message.payload.decode("utf-8","ignore"))
    m_in=json.loads(m_decode)
    print("received message =",m_in)
    
client= paho.Client() #create client object 
client.on_message=on_message
#####
print("connecting to broker ",broker)
# client.connect(broker,1883,60)#connect
if (client.connect(broker,1883,60) == 0):
	print ("Connected succesfully to "+broker)
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("se443/midterm2")#subscribe
while(True):
	client.on_message=on_message