from enum import Enum


class VehicleType(Enum):
    CAR = "CAR"
    BIKE = "BIKE"
    TRUCK = "TRUCK"


class SlotType(Enum):
    CAR_SLOT = "CAR_SLOT"
    BIKE_SLOT = "BIKE_SLOT"
    TRUCK_SLOT = "TRUCK_SLOT"


def get_slot_type_from_vehicle_type(vehicle_type: VehicleType) -> SlotType:
    if vehicle_type == VehicleType.CAR:
        return SlotType.CAR_SLOT
    elif vehicle_type == VehicleType.TRUCK:
        return SlotType.TRUCK_SLOT
    else:
        return SlotType.BIKE_SLOT
    