from cab_driver_billing_system.models.driver_vs_vehicle import DriverVSVehicleMap


class DriverVSVehicleMapRepository:
    def __init__(self):
        self.driver_vs_vehicle_maps = {}

    def create_vehicle(self, driver_id, vehicle_id):
        driver_vs_vehicle_map = DriverVSVehicleMap(driver_id, vehicle_id)
        self.driver_vs_vehicle_maps[driver_id] = driver_vs_vehicle_map

    def get_driver_vs_vehicle_maps(self):
        return self.driver_vs_vehicle_maps

    def get_driver_vs_vehicle_map_by_driver_id(self, driver_id):
        return self.driver_vs_vehicle_maps.get(driver_id, None)

