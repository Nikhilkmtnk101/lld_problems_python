from abc import ABC, abstractmethod
from parking_lot_system.enums import SlotType


class Slot(ABC):
    def __init__(self, slot_id: int, floor_no: int, slot_no: int):
        self.slot_id = slot_id
        self.floor_no = floor_no
        self.slot_no = slot_no
        self.is_available = True

    def get_slot_id(self) -> int:
        return self.slot_id

    def set_slot_id(self, slot_id: int):
        self.slot_id = slot_id

    def get_floor_id(self) -> int:
        return self.floor_no

    def set_floor_id(self, floor_no: int):
        self.floor_no = floor_no

    def is_slot_available(self) -> bool:
        return self.is_available

    def book_slot(self):
        self.is_available = False

    def free_slot(self):
        self.is_available = True

    @abstractmethod
    def get_slot_type(self) -> SlotType:
        pass


class CarSlot(Slot):
    def __init__(self, slot_id: int, floor_no: int, slot_no: int):
        super(CarSlot, self).__init__(slot_id, floor_no, slot_no)

    def get_slot_type(self) -> SlotType:
        return SlotType.CAR_SLOT


class BikeSlot(Slot):
    def __init__(self, slot_id: int, floor_no: int, slot_no: int):
        super(BikeSlot, self).__init__(slot_id, floor_no, slot_no)

    def get_slot_type(self) -> SlotType:
        return SlotType.BIKE_SLOT


class TruckSlot(Slot):
    def __init__(self, slot_id: int, floor_no: int, slot_no: int):
        super(TruckSlot, self).__init__(slot_id, floor_no, slot_no)

    def get_slot_type(self) -> SlotType:
        return SlotType.TRUCK_SLOT


class SlotFactory:

    def get_slot(self, slot_type: SlotType, slot_id: int, floor_no: int, slot_no: int):
        slot = None

        if slot_type == SlotType.BIKE_SLOT:
            slot = BikeSlot(slot_id, floor_no, slot_no)
        elif slot_type == SlotType.CAR_SLOT:
            slot = CarSlot(slot_id, floor_no, slot_no)
        elif slot_type == SlotType.TRUCK_SLOT:
            slot = TruckSlot(slot_id, floor_no, slot_no)
        else:
            raise Exception("Slot Type Not Supported")

        return slot
