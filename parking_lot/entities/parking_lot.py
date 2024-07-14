from parking_lot.entities.slot import Slot


class ParkingLot:
    def __init__(self, parking_lot_id: str, no_floor: int, no_slots_per_floor: int):
        self.parking_lot_id = parking_lot_id
        self.no_floor = no_floor
        self.no_slots_per_floor = no_slots_per_floor
        self.total_no_of_slots = self.no_floor * self.no_slots_per_floor
        self.slots = [Slot(i) for i in range(0, self.total_no_of_slots)]

    def get_parking_lot_id(self) -> str:
        return self.parking_lot_id

    def set_parking_lot_id(self, parking_lot_id: str):
        self.parking_lot_id = parking_lot_id

    def get_no_floor(self) -> int:
        return self.no_floor

    def set_no_floor(self, no_floor: int):
        self.no_floor = no_floor

    def get_no_slots_per_floor(self) -> int:
        return self.no_slots_per_floor

    def set_no_slots_per_floor(self, no_slots_per_floor: int):
        self.no_slots_per_floor = no_slots_per_floor

    def get_total_no_of_slots(self) -> int:
        return self.total_no_of_slots

    def set_total_no_of_slots(self, total_no_of_slots: int):
        self.total_no_of_slots = total_no_of_slots

    def get_slots(self) -> list[Slot]:
        return self.slots

    def set_slots(self, slots: list[Slot]):
        self.slots = slots
