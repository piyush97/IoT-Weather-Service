import paho.mqtt.client as mqtt

def client_interface():
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mqtt.eclipseprojects.io", 1883)
    return client
def subscribe():
    client = client_interface()
    client.subscribe("weather")
    client.loop_forever()
    
subscribe()