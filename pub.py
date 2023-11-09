from get_weather_data import parse_weather_data
import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883)


# client.loop_forever()


def publish():
    api_response = parse_weather_data()
    client.publish("weather", json.dumps(api_response))
    print("Published new weather data to topic 'weather'")

publish()