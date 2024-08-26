from cab_driver_billing_system.controller.common_controller import CommonController
from cab_driver_billing_system.enums import TripType, TripStatus

if __name__ == '__main__':
    cab_controller = CommonController()

    "Add Drivers"
    cab_controller.add_driver("Sachin", "+91-9936673000", "DL_01")
    cab_controller.add_driver("Ramesh", "+91-9936673001", "DL_02")
    cab_controller.add_driver("Manjuntha", "+91-9936673002", "DL_03")

    "Add Vehicle"
    cab_controller.add_vehicle("KA-01", "Maruti", "Economy")
    cab_controller.add_vehicle("KA-02", "BMW", "Premium")

    "Map Driver to vehicle"
    cab_controller.map_driver_to_vehicle(1, "KA-01")
    cab_controller.map_driver_to_vehicle(3, "KA-02")

    "ADD Trips"
    cab_controller.add_trip(50, 1, 0, 100, TripType.IntraCity.value, TripStatus.Completed.value)
    cab_controller.add_trip(1050, 1, 101, 200, TripType.OutStation.value, TripStatus.Completed.value)
    cab_controller.add_trip(50, 1, 201, 300, TripType.IntraCity.value, TripStatus.CancelledCustomer.value)
    cab_controller.add_trip(50, 3, 0, 100, TripType.OutStation.value, TripStatus.CancelledDriver.value)
    cab_controller.add_trip(70, 3, 101, 200, TripType.OutStation.value, TripStatus.Completed.value)

    "Bill"
    cab_controller.get_bill(1)
    cab_controller.get_bill(3)
