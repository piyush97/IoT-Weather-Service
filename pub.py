from get_weather_data import parse_weather_data
import paho.mqtt.client as mqtt
import json
import time

def on_connect(client, userdata, flags, rc):
    print("Publisher Connected with result code " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

def client_interface():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mqtt.eclipseprojects.io", 1883)
    return client

def publish():
    client = client_interface()
    api_response = parse_weather_data()
    client.publish("weather", json.dumps(api_response))
    print("Published new weather data to topic 'weather'")
    client.loop_forever()

def main():
    while True:
        publish()
        time.sleep(300)  # Sleep for 5 minutes

if __name__ == "__main__":
    main()
