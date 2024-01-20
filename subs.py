# mqtt.py
import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("notification_topic")

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    print(f"Received message: {payload}")

    process_received_message(client, payload)

def process_received_message(client, payload):
    print(f"Custom processing: {payload}")

    response_payload = {'response': payload}
    client.publish('response_topic', json.dumps(response_payload), qos=0, retain=False)

def start_mqtt_listener():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost", 1883, 60)

    client.loop_forever()  #client_loop_start() if using in django

if __name__ == "__main__":
    start_mqtt_listener()
