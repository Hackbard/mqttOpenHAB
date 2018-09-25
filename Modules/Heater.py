import logging
from Modules.MqttClient import MqttClient
from Modules.Snips.SnipsParser import SnipsParser
from Modules.OpenHABProxy import OpenHABProxy


class Heater:
    __channel_manuel_degree = "hermes/intent/hackbard:HeizungToTemperature"
    __channel_boost = "hermes/intent/hackbard:HeizungBoost"

    __mqtt_client = None
    __openHAB_proxy = None

    def __init__(self):
        logging.debug("Init Module: Heater")
        self.__mqtt_client = MqttClient.getInstance()
        self.__openHAB_proxy = OpenHABProxy.getInstance()
        self.trackChannels()

    def trackChannels(self):
        logging.debug("Module.Heater track Channels")
        self.__mqtt_client.subscribe(self.__channel_manuel_degree, self.onTemperatureChange)
        self.__mqtt_client.subscribe(self.__channel_boost, self.onBoost)

    def onTemperatureChange(self, client, userdata, msg):
        logging.info("Receive heater.onTemperatureChange")

        snip = SnipsParser.convertFromJson(msg.payload)
        room = snip.getSlotValueByName("room")
        temperature = snip.getSlotValueByName("temperature")

        if temperature is None:
            logging.info("No Temperature")
            return None

        logging.debug("Room: " + room)
        logging.debug("Temperature: " + str(temperature))

        heater_config = self.__openHAB_proxy.getHeaterConfigByRoom(room=room)

        for heater in heater_config:
            name = heater.get('name')
            homematic_mode = self.__openHAB_proxy.getItemByName(name + "_MODE")
            homematic_temperature = self.__openHAB_proxy.getItemByName(name + "_TEMPERATURE_SETTER")

            homematic_mode.state = "MANU-MODE"
            homematic_temperature.command(float(temperature))

    def onBoost(self, client, userdata, msg):
        logging.info("Receive heater.onBoost")
        snip = SnipsParser.convertFromJson(msg.payload)
