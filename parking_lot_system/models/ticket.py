class Ticket:
    def __init__(self, parking_lot_id: str, floor_no: int, slot_no: int, vehicle_registration_no: str):
        self.parking_lot_id = parking_lot_id
        self.floor_no = floor_no
        self.slot_no = slot_no
        self.vehicle_registration_no = vehicle_registration_no
        self.ticket_id = f'{self.parking_lot_id}_{self.floor_no}_{self.slot_no}'

    def get_ticket_id(self) -> str:
        return self.ticket_id

    def get_floor_no(self) -> int:
        return self.floor_no

    def set_floor_no(self, floor_no: int):
        self.floor_no = floor_no

    def get_slot_no(self) -> int:
        return self.slot_no

    def set_slot_no(self, slot_no: int):
        self.slot_no = slot_no
