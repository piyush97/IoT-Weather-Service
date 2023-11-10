import paho.mqtt.client as mqtt
import sys
import json

def on_connect(client, userdata, flags, rc):
    print("Subscriber connected with result code "+str(rc))
    client.subscribe(sys.argv[1])
    print('Subscribed to topic ' + sys.argv[1])

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload.decode("utf-8")))
    save_data_using_sys(msg)
    check_conditions(msg)

def check_temperature_conditions(msg):
    print("Warning: Temperature below 10 degrees for 30 consecutive minutes.")

def check_wind_speed_conditions(msg):
    print("Warning: Wind speed more than 20 km/hour for the last 10 minutes.")

def check_rain_conditions(msg):
    print("Warning: Rain continues for more than 45 hours.")

def check_conditions(msg):
    try:
        payload_data = json.loads(msg.payload.decode("utf-8"))

        temperature = payload_data.get("temperature", None)
        wind_speed = payload_data.get("wind_speed", None)
        rain_duration = payload_data.get("rain_duration", None)

        if temperature is not None and temperature < 10:
            check_temperature_conditions(msg)

        if wind_speed is not None and wind_speed > 20:
            check_wind_speed_conditions(msg)

        if rain_duration is not None and rain_duration > 45:
            check_rain_conditions(msg)

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except KeyError as e:
        print(f"KeyError: {e}. Make sure the payload has all required fields.")

def save_data_using_sys(msg):
    try:
        payload_data = json.loads(msg.payload.decode("utf-8"))

        time = payload_data["time"]
        ip = payload_data["ip"]
        devicename = payload_data["devicename"]
        value = payload_data["value"]

        formatted_data = f"{time} {value}"

        topic = sys.argv[1]
        file_name = topic + ".txt"

        with open(file_name, "a") as f:
            f.write(formatted_data + "\n")
            print("Data saved to file " + file_name)

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except KeyError as e:
        print(f"KeyError: {e}. Make sure the payload has all required fields.")

def client_interface():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mqtt.eclipseprojects.io", 1883)

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("Disconnecting gracefully...")
        client.disconnect()

if __name__ == "__main__":
    client_interface()
