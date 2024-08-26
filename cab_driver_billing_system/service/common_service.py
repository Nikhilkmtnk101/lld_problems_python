from cab_driver_billing_system.repository.driver import DriverRepository
from cab_driver_billing_system.repository.driver_vs_vehicle import DriverVSVehicleMapRepository
from cab_driver_billing_system.repository.trip import TripRepository
from cab_driver_billing_system.repository.vehicle import VehicleRepository
from cab_driver_billing_system.service.bill_service.bill_service import BillServiceFactory


class CommonService:
    def __init__(self):
        self.driver_repository = DriverRepository()
        self.vehicle_repository = VehicleRepository()
        self.driver_vs_vehicle_map_repository = DriverVSVehicleMapRepository()
        self.trip_repository = TripRepository()

    def create_driver(self, name, phone_no, dl_no):
        self.driver_repository.create_driver(name, phone_no, dl_no)

    def create_vehicle(self, vehicle_id, name, vehicle_type):
        self.vehicle_repository.create_vehicle(vehicle_id, name, vehicle_type)

    def create_driver_to_vehicle_map(self, driver_id, vehicle_id):
        self.driver_vs_vehicle_map_repository.create_vehicle(driver_id, vehicle_id)

    def add_trip(self, driver_id, distance, start_time, end_time, trip_type, status):
        self.trip_repository.create_driver(driver_id, distance, start_time, end_time, trip_type, status)

    def get_bill(self, driver_id):
        total_bill = 0
        driver_trips = self.trip_repository.get_trips_by_driver_id(driver_id)
        driver_vs_vehilce_map = self.driver_vs_vehicle_map_repository.get_driver_vs_vehicle_map_by_driver_id(driver_id)
        vehicle = self.vehicle_repository.get_vehicle_by_id(driver_vs_vehilce_map.get_vehicle_id())
        vehicle_type = vehicle.get_vehicle_type()
        for trip in driver_trips:
            trip_bill_service = BillServiceFactory.get_vehicle_model_bill_service(trip.get_status(), trip.get_trip_type(), vehicle_type)
            total_bill += trip_bill_service.get_bill(trip.get_distance())

        return total_bill
