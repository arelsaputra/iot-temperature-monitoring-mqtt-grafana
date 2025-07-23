import paho.mqtt.client as mqtt
import time
import random

broker = "broker.hivemq.com"
port = 1883
topic = "iot/edge/suhu"

client = mqtt.Client()
client.connect(broker, port)

try:
    while True:
        suhu = round(random.uniform(20.0, 40.0), 2)
        client.publish(topic, str(suhu))
        print(f"Data suhu dikirim: {suhu} °C")
        time.sleep(5)
except KeyboardInterrupt:
    print("Publisher dihentikan.")
