from abc import ABC, abstractmethod

from cab_driver_billing_system.enums import VehicleType


class VehicleModelBillService(ABC):
    @abstractmethod
    def get_per_km_price(self):
        pass


class EconomyVehicleModelBillService(ABC):
    def __init__(self):
        self.price_per_km = 5

    def get_per_km_price(self):
        return self.price_per_km


class PremiumVehicleModelBillService(ABC):
    def __init__(self):
        self.price_per_km = 12

    def get_per_km_price(self):
        return self.price_per_km


class LuxuryVehicleModelBillService(ABC):
    def __init__(self):
        self.price_per_km = 15

    def get_per_km_price(self):
        return self.price_per_km


class VehicleModelBillServiceFactory:
    @staticmethod
    def get_vehicle_model_bill_service(vehicle_type):
        vehicle_model_bill_service = None
        if vehicle_type == VehicleType.Economy.value:
            vehicle_model_bill_service = EconomyVehicleModelBillService()
        elif vehicle_type == VehicleType.Premium.value:
            vehicle_model_bill_service = PremiumVehicleModelBillService()
        elif vehicle_type == VehicleType.Luxury.value:
            vehicle_model_bill_service = LuxuryVehicleModelBillService()

        return vehicle_model_bill_service