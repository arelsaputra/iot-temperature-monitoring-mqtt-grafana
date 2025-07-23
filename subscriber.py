import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "iot/edge/suhu"

def on_connect(client, userdata, flags, rc):
    print("Terhubung ke broker")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Suhu diterima: {msg.payload.decode()} °C")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.loop_forever()
