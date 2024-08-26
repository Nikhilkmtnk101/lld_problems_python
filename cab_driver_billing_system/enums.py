from enum import Enum


class VehicleType(Enum):
    Economy = "Economy"
    Premium = "Premium"
    Luxury = "Luxury"


class TripType(Enum):
    IntraCity = "IntraCity"
    OutStation = "OutStation"


class TripStatus(Enum):
    Completed = "Completed"
    CancelledDriver = "CancelledDriver"
    CancelledCustomer = "CancelledCustomer"
