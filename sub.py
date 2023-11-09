import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Subscriber connected with result code "+str(rc))


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    
def client_interface():
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mqtt.eclipseprojects.io", 1883)
    client.subscribe("weather")
    print("Subscribed to topic 'weather'")
    client.loop_forever()
    return client
    

    
client_interface()