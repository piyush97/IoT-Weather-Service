
# Import the necessary libraries
from get_weather_data import parse_weather_data
import paho.mqtt.client as mqtt
import json
import time
import requests

# Get the IP address of the device
def get_ip_address():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    return ip_address

# Handle the connection to the MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Publisher Connected with result code " + str(rc))

# Handle the receipt of a message
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

# Connect to the MQTT broker
def client_interface():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mqtt.eclipseprojects.io", 1883)
    return client

# Publish the weather data to the MQTT broker
def publish_weather_info(client, topic, value):
    # Get IP address and device name
    ip_address = get_ip_address()
    device_name = "piyush-pi"

    # Format the time
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    # Create MQTT message
    mqtt_message = {
        "time": current_time,
        "ip": ip_address,
        "devicename": device_name,
        "value": value
    }

    payload = json.dumps(mqtt_message)
    client.publish(topic, payload)
    print(f"Published new weather data to topic '{topic}'")
    
def publish():
    client = client_interface()
    api_response = parse_weather_data()
    publish_weather_info(client, "temperature", api_response["temperature"])
    publish_weather_info(client, "humidity", api_response["humidity"])
    publish_weather_info(client, "rain_status", api_response["raining"])
    publish_weather_info(client, "wind_speed", api_response["windspeed"])
    
def main():
    while True:
        time.sleep(300)  # Sleep for 5 minutes
        publish()
    
if __name__ == "__main__":
    main()
