from abc import ABC, abstractmethod

from parking_lot_system.enums import SlotType
from parking_lot_system.models.slot import Slot


class ParkingStrategy(ABC):
    @abstractmethod
    def get_first_available_slot(self, slot_type: SlotType) -> Slot:
        pass


class NaturalOrderParkingStrategy(ParkingStrategy):
    def __init__(self, no_of_floor: int, slots_per_floor: int, slots: list[list[Slot]]):
        self.no_of_floor = no_of_floor
        self.slots_per_floor = slots_per_floor
        self.slots = slots

    def get_first_available_slot(self, slot_type: SlotType) -> Slot:
        for i in range(0, self.no_of_floor):
            for j in range(0, self.slots_per_floor):
                slot = self.slots[i][j]
                if slot.is_slot_available() and slot.get_slot_type().value == slot_type.value:
                    return slot

        return None


