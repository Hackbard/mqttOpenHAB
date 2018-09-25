import logging
import json
from Modules.Snips.Snips import Slot, Snip


class SnipsParser:
    @staticmethod
    def convertFromJson(payload):
        logging.debug("Slot.give_slots_from_string " + str(payload))
        data = json.loads(payload.decode("utf-8"))
        parser = SnipsParser()
        return parser.generateObject(data)

    def generateObject(self, data):
        snips = Snip()
        snips.input = data.get('input')
        snips.intent = data.get('intent')
        snips.slots = self.generateSlots(data.get('slots'))

        return snips

    def generateSlots(self, slotData):
        slots = []
        for val in slotData:
            slot = Slot()
            slot.rawValue = val.get('rawValue')
            slot.value = val.get('value')
            slot.range = val.get('range')
            slot.entity = val.get('entity')
            slot.slotName = val.get('slotName')
            slots.append(slot)

        return slots
