from cab_driver_billing_system.repository.driver import DriverRepository
from cab_driver_billing_system.service.common_service import CommonService


class CommonController:
    def __init__(self):
        self.common_service = CommonService()
        self.driver_repository = self.common_service.driver_repository

    def add_driver(self, name, phone_no, dl_no):
        self.common_service.create_driver(name, phone_no, dl_no)

    def add_vehicle(self, vehicle_id, name, vehicle_type):
        self.common_service.create_vehicle(vehicle_id, name, vehicle_type)

    def map_driver_to_vehicle(self, driver_id, vehicle_id):
        self.common_service.create_driver_to_vehicle_map(driver_id, vehicle_id)

    def add_trip(self, distance, driver_id, start_time, end_time, trip_type, status):
        self.common_service.add_trip(driver_id, distance, start_time, end_time, trip_type, status)

    def get_bill(self, driver_id):
        total_bill = self.common_service.get_bill(driver_id)
        driver_name = self.driver_repository.get_driver_by_id(driver_id).get_name()

        print(f"{driver_name}: {total_bill}")
