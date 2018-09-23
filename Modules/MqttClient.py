__author__ = "Benjamin Klein"
__maintainer__ = "Benjamin Klein"
__email__ = "hackbard23@gmail.com"
__copyright__ = "Copyright 2018"
__license__ = "GNU GPL v3"
__version__ = "0.0.1"

import paho.mqtt.client as mqtt
import logging


class MqttClient:
    __instance = None
    hostname = False
    port = False
    keep_alive = False
    client_name = False
    client = False

    @staticmethod
    def getInstance():
        if not MqttClient.__instance:
            MqttClient()
        return MqttClient.__instance

    def __init__(self):
        if MqttClient.__instance != None:
            raise Exception("This class is a Singleton!")
        else:
            MqttClient.__instance = self

    def getClient(self):
        return self.client

    def setConfig(self, hostname, port, keep_alive, client_name):
        self.hostname = hostname
        self.port = int(port)
        self.keep_alive = int(keep_alive)
        self.client_name = client_name

    def on_connect(self, client, userdata, flags, rc):
        self.client.subscribe("$SYS/#")
        logging.debug("Connected MQTT-Client on " + self.hostname + ":" + self.port)

    def on_message(client, userdata, msg):
        logging.debug(str(msg))

    def on_subscribe(client, userdata, mid, granted_qos):
        logging.debug(str(mid))

    def init_mqtt_connection(self):
        logging.debug("Create MQTT - Client")
        self.client = mqtt.Client(self.client_name)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe

        try:
            self.client.connect(self.hostname, self.port, self.keep_alive)
            self.client.subscribe("$SYS/#", 0)
        except ConnectionRefusedError as error:
            logging.critical("Connection refused to %s on port %d", self.hostname, self.port)

    def subscribe(self, topic, callback):
        self.client.message_callback_add(topic, callback)
        self.client.subscribe(topic)

    def startLoop(self):
        try:
            logging.debug("Start the Loop")
            self.client.loop_forever()
        except KeyboardInterrupt:
            logging.debug("Shutdown by Keyboard Interrupt")
