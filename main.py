__author__ = "Benjamin Klein"
__maintainer__ = "Benjamin Klein"
__email__ = "hackbard23@gmail.com"
__copyright__ = "Copyright 2018"
__license__ = "GNU GPL v3"
__version__ = "0.0.1"

import configparser
import logging
from Modules.MqttClient import MqttClient
from Modules.Heater import Heater
from Modules.Light import Light
from Modules.OpenHABProxy import OpenHABProxy
import json


def main():
    # Load config data
    config = configparser.ConfigParser()
    config.read('./config/config.ini')

    # Set Loglevel
    logging.getLevelName(config.get('LOG', 'LEVEL'))
    log_level = logging.getLevelName(config.get('LOG', 'LEVEL'))

    log_file = config.get('LOG', 'FILE')
    logging.basicConfig(level=log_level, format='%(asctime)s %(levelname)s %(message)s',
                        filename=log_file, )  # filename=log_file,

    logging.info("Start Service")

    mqtt_client = MqttClient.getInstance()
    mqtt_client.setConfig(hostname=config.get('MQTT', 'HOST'), port=config.get('MQTT', 'PORT'),
                          keep_alive=config.get('MQTT', 'PORT'), client_name=config.get('MQTT', 'CLIENT_NAME'))
    mqtt_client.init_mqtt_connection()

    with open('./config/devices_rooms.json') as json_data_file:
        data = json.load(json_data_file)

    openhab_proxy = OpenHABProxy.getInstance(base_url=config.get("OPENHAB", "BASE_URL"))
    openhab_proxy.setConfig(data)

    light = Light()
    heater = Heater()

    mqtt_client.startLoop()


if __name__ == '__main__':
    main()
