from abc import ABC, abstractmethod

from cab_driver_billing_system.enums import VehicleType, TripType
from cab_driver_billing_system.service.bill_service.vehilce_model_bill_service import VehicleModelBillServiceFactory


class TripTypeBillService(ABC):
    @abstractmethod
    def get_per_km_price(self):
        pass


class IntraCityBillService(ABC):
    def __init__(self, vehicle_type):
        self.factor = 1
        print(vehicle_type)
        self.vehicle_model_bill_service = VehicleModelBillServiceFactory.get_vehicle_model_bill_service(vehicle_type)

    def get_per_km_price(self):
        return self.factor * self.vehicle_model_bill_service.get_per_km_price()


class OutStationCityBillService(ABC):
    def __init__(self, vehicle_type):
        self.factor = 2
        self.vehicle_model_bill_service = VehicleModelBillServiceFactory.get_vehicle_model_bill_service(vehicle_type)

    def get_per_km_price(self):
        return self.factor * self.vehicle_model_bill_service.get_per_km_price()


class TripTypeBillServiceFactory:
    @staticmethod
    def get_trip_type_bill_service(trip_type, vehicle_type):
        trip_type_bill_service = None
        if trip_type == TripType.IntraCity.value:
            trip_type_bill_service = IntraCityBillService(vehicle_type)
        elif trip_type == TripType.OutStation.value:
            trip_type_bill_service = OutStationCityBillService(vehicle_type)

        return trip_type_bill_service
