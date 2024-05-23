from parking_lot_system.enums import VehicleType


class Vehicle:
    def __init__(self, registration_number: str, vehicle_type: VehicleType, color: str):
        self.registration_number = registration_number
        self.vehicle_type = vehicle_type
        self.color = color

    def get_registration_number(self) -> str:
        return self.registration_number

    def set_registration_number(self, registration_number: str):
        self.registration_number = registration_number

    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type

    def set_vehicle_type(self, vehicle_type: VehicleType):
        self.vehicle_type = vehicle_type

    def get_color(self) -> str:
        return self.color

    def set_color(self, color: str):
        self.color = color
