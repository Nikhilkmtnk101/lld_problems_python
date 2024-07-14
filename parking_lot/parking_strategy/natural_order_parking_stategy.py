from parking_lot.entities.slot import Slot
from parking_lot.parking_strategy.parking_startegy_interface import ParkingStrategy


class NaturalParkingStrategy(ParkingStrategy):

    def get_free_slot(self, slots: list[Slot], vehicle_type: str) -> Slot:
        result = None
        for slot in slots:
            if (slot.get_is_available()) and (slot.get_supported_vehicle_type() == vehicle_type):
                result = slot
        return result
