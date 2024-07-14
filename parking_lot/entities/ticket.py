
class Ticket:
    def __init__(self, ticket_id: str, vehicle_reg_no: str, slot_id: int):
        self.ticket_id = ticket_id
        self.vehicle_reg_no = vehicle_reg_no
        self.slot_id = slot_id

    def get_ticket_id(self) -> str:
        return self.ticket_id

    def set_ticket_id(self, ticket_id: str):
        self.ticket_id = ticket_id

    def get_vehicle_reg_no(self) -> str:
        return self.vehicle_reg_no

    def set_vehicle_reg_no(self, vehicle_reg_no: str):
        self.vehicle_reg_no = vehicle_reg_no

    def get_slot_id(self) -> int:
        return self.slot_id

    def set_slot_id(self, slot_id: int):
        self.slot_id = slot_id
