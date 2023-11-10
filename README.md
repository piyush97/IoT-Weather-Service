# Weather Data MQTT Integration

This Python script collection enables the retrieval of weather data from OpenWeatherMap, publishing it to an MQTT broker, and subscribing to that data to perform specific actions based on weather conditions.

## Files

### 1. get_weather_data.py

#### Description
This script fetches weather data from OpenWeatherMap API based on latitude and longitude coordinates provided through environment variables.

#### Functions
- **get_env_vars():** Retrieves OpenWeatherMap API key, latitude, and longitude from environment variables.
- **get_weather_data():** Fetches weather data using OpenWeatherMap API.
- **parse_weather_data():** Parses the received weather data and formats it for further use.

### 2. subscriber.py

#### Description
This script subscribes to an MQTT topic and performs actions based on the received weather data.

#### Functions
- **on_connect():** Callback function when the subscriber connects to the MQTT broker.
- **on_message():** Callback function triggered when a message is received. It checks weather conditions and calls specific functions accordingly.
- **check_temperature_conditions(), check_wind_speed_conditions(), check_rain_conditions():** Functions to check specific weather conditions.
- **check_conditions():** Checks weather conditions based on the received data and calls relevant functions.
- **save_data_using_sys():** Saves received data to a file.
- **client_interface():** Initializes the MQTT client and handles the connection.

### 3. publisher.py

#### Description
This script publishes weather data to an MQTT broker at regular intervals.

#### Functions
- **get_ip_address():** Retrieves the IP address of the device.
- **on_connect(), on_message():** Callback functions for MQTT client connection and message handling.
- **client_interface():** Initializes the MQTT client for publishing.
- **publish_weather_info():** Publishes weather data to the MQTT broker.
- **publish():** Main function to publish weather data at regular intervals.
- **main():** Entry point of the script.

## Usage

1. Ensure you have the required Python libraries installed using `pip install -r requirements.txt`.
2. Set your OpenWeatherMap API key, latitude, and longitude as environment variables in a `.env` file.
3. Run `publisher.py` to start publishing weather data.
4. Run `subscriber.py <topic>` to subscribe to the specified MQTT topic and perform actions based on weather conditions.

Note: Make sure to replace `<topic>` with the desired MQTT topic.

## Dependencies
- `json`
- `requests`
- `os`
- `time`
- `dotenv`
- `paho.mqtt.client`

## Disclaimer
Make sure to handle sensitive information such as API keys securely and responsibly.
