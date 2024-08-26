from cab_driver_billing_system.models.vehicle import Vehicle


class VehicleRepository:
    def __init__(self):
        self.vehicles = {}

    def create_vehicle(self, vehicle_id, name, vehicle_type):
        vehicle = Vehicle(vehicle_id, name, vehicle_type)
        self.vehicles[vehicle_id] = vehicle

    def get_vehicles(self):
        return self.vehicles

    def get_vehicle_by_id(self, vehicle_id):
        return self.vehicles.get(vehicle_id, None)
