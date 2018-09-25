import logging
import string
from openhab import OpenHAB


class OpenHABProxy:
    __instance = None
    __raw_config = None
    openHab = None
    openhab_items = None

    __light = []
    __heater = []

    @staticmethod
    def getInstance(base_url=None):
        if OpenHABProxy.__instance == None:
            OpenHABProxy(base_url)
        return OpenHABProxy.__instance

    def __init__(self, base_url):
        if OpenHABProxy.__instance != None:
            raise Exception("This class is a Singleton!")
        else:
            OpenHABProxy.__instance = self
            self.openHab = OpenHAB(base_url)
            self.reloadItem()
            logging.debug("Retrive openHAB item")

    def reloadItem(self):
        self.openhab_items = self.openHab.fetch_all_items()

    def setConfig(self, config):
        self.__raw_config = config
        for key in self.__raw_config:
            config_item = self.__raw_config.get(key)
            if config_item.get('type') == "light":
                self.__light.append(config_item)
            if config_item.get('type') == "heater":
                self.__heater.append(config_item)
        logging.debug(self)

    def getHeaterByRoom(self, room):
        return self.__getItems(self.__heater, room)

    def getLight(self, room, source):
        return self.__getItems(self.__light, room=room, source=source)

    def getItemByName(self, name):
        return self.openhab_items.get(name)

    def getHeaterConfigByRoom(self, room):
        return_data = [];
        for item in self.__heater:
            if item.get('room').lower() == room.lower():
                return_data.append(item)
        return return_data

    def __getItems(self, data, room, source=None):
        return_data = []
        for item in data:
            openhab_item = None
            if item.get('room').lower() == room.lower():
                if (source is None) or (source is not None and item.get('source').lower() == source):
                    openhab_item = self.openhab_items.get(item.get('name'))

                if openhab_item:
                    return_data.append(openhab_item)

        return return_data
