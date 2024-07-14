from parking_lot.entities.vehicle import Vehicle


class VehicleDao:
    def __init__(self):
        self.vehicles = {}

    def get_vehicles(self) -> dict:
        return self.vehicles

    def set_vehicles(self, vehicles: dict):
        self.vehicles = vehicles

    def get_vehicle_by_reg_no(self, reg_no: str) -> Vehicle:
        return self.vehicles.get(reg_no, None)

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles[vehicle.get_reg_no()] = vehicle
