import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("response_topic")

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    print(f"Received message in Backend 2: {payload}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()