# MQTT.py

This is a Python script (`mqtt.py`) that implements a simple MQTT (Message Queuing Telemetry Transport) listener using the Paho MQTT client library. MQTT is a lightweight messaging protocol often used in IoT (Internet of Things) applications for communication between devices.

## Prerequisites

Before running this script, ensure that you have the necessary dependencies installed. You can install them using the following:

```bash
pip install paho-mqtt


## To run and test 

```bash
python3 listner.py
```bash
python3 mqtt.py
```bash
mosquitto_pub -t notification_topic -m '{"message": "your_message"}' 
