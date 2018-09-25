import logging
from Modules.MqttClient import MqttClient
from Modules.Snips.SnipsParser import SnipsParser
from Modules.OpenHABProxy import OpenHABProxy


class Light:
    __mqtt_client = None
    __openHAB_proxy = None
    __channel_on_off = "hermes/intent/hackbard:LichtAnAus"

    def __init__(self):
        logging.debug("Init Module: Light")
        logging.debug("Init Module: Heater")

        self.__mqtt_client = MqttClient.getInstance()
        self.__openHAB_proxy = OpenHABProxy.getInstance()
        self.trackChannels()

    def trackChannels(self):
        logging.debug("Module.Light track Channels")
        self.__mqtt_client.subscribe(self.__channel_on_off, self.onPowerChange)

    def onPowerChange(self, client, userdata, msg):
        logging.info("Receive light.onPowerChange")

        snip = SnipsParser.convertFromJson(msg.payload)
        action = snip.getSlotValueByName("action")
        room = snip.getSlotValueByName("room")
        light = snip.getSlotValueByName("light")

        logging.debug("Room: " + str(room))
        logging.debug("Action: " + str(action))
        logging.debug("Licht: " + str(light))

        try:
            lighter = self.__openHAB_proxy.getLight(room=room, source=light)
            if action and action == "Einschalten":
                for light in lighter:
                    light.command('ON')

            if action and action == "Ausschalten":
                for light in lighter:
                    light.command('OFF')
        except RuntimeError as error:
            logging.error(str(error))