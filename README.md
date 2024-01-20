# MQTT.py

This is a Python script (`mqtt.py`) that implements a simple MQTT (Message Queuing Telemetry Transport) listener using the Paho MQTT client library. MQTT is a lightweight messaging protocol often used in IoT (Internet of Things) applications for communication between devices.

## Prerequisites

Before running this script, ensure that you have the necessary dependencies installed. You can install them using the following:

```bash
pip install paho-mqtt
```

# How to Run and Test


Open a terminal and run the MQTT listener:


```bash
python3 listener.py
```


Open another terminal and run the MQTT script:


 ```bash
python3 mqtt.py
```


To test the MQTT communication, open a new terminal and publish a message to the "notification_topic" using mosquitto_pub:


```bash
mosquitto_pub -t notification_topic -m '{"message": "your_message"}'
```


 Ensure that you replace "your_message" with the actual message you want to send.
