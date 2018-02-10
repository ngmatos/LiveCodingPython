import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with code " + str(rc))

    client.subscribe("test")

def on_message(client, userdata, msg):
    print(msg.payload.decode('utf-8', 'ignore'))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)

client.loop_forever()