from abc import ABC, abstractmethod

from parking_lot.entities.slot import Slot


class ParkingStrategy(ABC):
    @abstractmethod
    def get_free_slot(self, slots: list[Slot], vehicle_type: str) -> Slot:
        pass

