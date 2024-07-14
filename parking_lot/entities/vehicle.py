
class Vehicle:
    def __init__(self, vehicle_type: str, reg_no: str, color: str):
        self.vehicle_type = vehicle_type
        self.reg_no = reg_no
        self.color = color

    def get_vehicle_type(self) -> str:
        return self.vehicle_type

    def set_vehicle_type(self, vehicle_type: str):
        self.vehicle_type = vehicle_type

    def get_reg_no(self) -> str:
        return  self.reg_no

    def set_reg_no(self, reg_no: str):
        self.reg_no = reg_no

    def get_color(self) -> str:
        return self.color

    def set_color(self, color: str):
        self.color = color
