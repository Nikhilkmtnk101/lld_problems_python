from abc import ABC, abstractmethod
from cab_driver_billing_system.enums import VehicleType, TripStatus
from cab_driver_billing_system.service.bill_service.trip_type_bill_service import TripTypeBillServiceFactory


class BillService(ABC):
    @abstractmethod
    def get_bill(self, trip_type, vehicle_type):
        pass


class CompletedStatusBillService(ABC):
    def __init__(self, trip_type, vehicle_type):
        self.trip_type_bill_service = TripTypeBillServiceFactory.get_trip_type_bill_service(trip_type, vehicle_type)

    def get_bill(self, distance):
        price_per_km = self.trip_type_bill_service.get_per_km_price()
        return distance * price_per_km


class DriverCancelledStatusBillService(ABC):
    def __init__(self, trip_type, vehicle_type):
        self.trip_type_bill_service = TripTypeBillServiceFactory.get_trip_type_bill_service(trip_type, vehicle_type)

    def get_bill(self, distance):
        return -10


class CustomerCancelledStatusBillService(ABC):
    def __init__(self, trip_type, vehicle_type):
        self.trip_type_bill_service = TripTypeBillServiceFactory.get_trip_type_bill_service(trip_type, vehicle_type)

    def get_bill(self, distance):
        return 10


class BillServiceFactory:
    @staticmethod
    def get_vehicle_model_bill_service(trip_status, trip_type, vehicle_type):
        bill_service = None
        if trip_status == TripStatus.Completed.value:
            bill_service = CompletedStatusBillService(trip_type, vehicle_type)
        elif trip_status == TripStatus.CancelledDriver.value:
            bill_service = DriverCancelledStatusBillService(trip_type, vehicle_type)
        elif trip_status == TripStatus.CancelledCustomer.value:
            bill_service = CustomerCancelledStatusBillService(trip_type, vehicle_type)

        return bill_service
