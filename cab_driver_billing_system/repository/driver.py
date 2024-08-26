from cab_driver_billing_system.models.driver import Driver
from cab_driver_billing_system.utils.driver_id_generator import DriverIdGenerator


class DriverRepository:
    def __init__(self):
        self.drivers = {}
        self.driver_id_generator = DriverIdGenerator()

    def create_driver(self, name, phone_no, dl_no):
        driver_id = self.driver_id_generator.get_next_driver_id()
        driver = Driver(driver_id, name, phone_no, dl_no)
        self.drivers[driver_id] = driver

    def get_drivers(self):
        return self.drivers

    def get_driver_by_id(self, driver_id):
        return self.drivers.get(driver_id, None)