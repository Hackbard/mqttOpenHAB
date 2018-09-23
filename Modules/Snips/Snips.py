class Snip:
    input = None
    intent = None
    slots = None

    def getSlotByName(self, name):
        if self.slots:
            for slot in self.slots:
                if name == slot.slotName:
                    return slot
        return None

    def getSlotValueByName(self, name):
        slot = self.getSlotByName(name)
        if not slot:
            return None

        return slot.value.get('value')


class Slot:
    rawValue = None
    value = None
    range = None
    entity = None
    slotName = None
