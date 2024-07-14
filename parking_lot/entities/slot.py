
class Slot:
    def __init__(self, slot_id: int, supported_vehicle_type: str = None):
        self.slot_id = slot_id
        self.supported_vehicle_type = supported_vehicle_type
        self.is_available = True

    def get_slot_id(self) -> int:
        return self.slot_id

    def set_slot_id(self, slot_id: int):
        self.slot_id = slot_id

    def get_supported_vehicle_type(self) -> str:
        return self.supported_vehicle_type

    def set_supported_vehicle_type(self, supported_vehicle_type: str):
        self.supported_vehicle_type = supported_vehicle_type

    def get_is_available(self) -> bool:
        return self.is_available

    def book_slot(self):
        self.is_available = False

    def free_slot(self):
        self.is_available = True
