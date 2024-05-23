from parking_lot_system.models.slot import Slot


class ParkingLot:
    def __init__(self, parking_lot_id: str, no_of_floor: int, slot_per_floor: int):
        self.parking_lot_id = parking_lot_id
        self.no_of_floor = no_of_floor
        self.slot_per_floor = slot_per_floor
        self.slots = []

    def get_parking_lot_id(self) -> str:
        return self.parking_lot_id

    def set_parking_lot_id(self, parking_lot_id: str):
        self.parking_lot_id = parking_lot_id

    def get_no_of_floor(self) -> int:
        return self.no_of_floor

    def set_no_of_floor(self, no_of_floor: int):
        self.no_of_floor = no_of_floor

    def get_slot_per_floor(self) -> int:
        return self.slot_per_floor

    def set_slot_per_floor(self, slot_per_floor: int):
        self.slot_per_floor = slot_per_floor

    def get_slots(self) -> list[list[Slot]]:
        return self.slots

    def set_slots(self, slots: list[list[Slot]]):
        self.slots = slots

    def get_free_slots_count_per_floor(self) -> list[int]:
        free_slots = []
        for i in range(0, self.no_of_floor):
            count = 0
            for j in range(0, self.slot_per_floor):
                if self.slots[i][j].is_slot_available():
                    count = count+1

            free_slots.append(count)

        return free_slots
