class DriverVSVehicleMap:
    def __init__(self, driver_id, vehicle_id):
        self.driver_id = driver_id
        self.vehicle_id = vehicle_id

    def set_driver_id(self, driver_id):
        self.driver_id = driver_id

    def get_driver_id(self):
        return self.driver_id

    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def get_vehicle_id(self):
        return self.vehicle_id
