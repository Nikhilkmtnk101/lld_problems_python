from parking_lot.enum import VehicleType
from parking_lot.parking_lot_service import ParkingLotService

if __name__ == '__main__':
    parking_lot_service = ParkingLotService()
    parking_lot_service.create_parking_lot("PR1234", 2, 6)
    parking_lot_service.park_vehicle(VehicleType.TRUCK.value, "reg1", "Col1")
    ticket_id = parking_lot_service.park_vehicle(VehicleType.TRUCK.value, "reg2", "Col1")
    parking_lot_service.unpark_vehicle(ticket_id)
    parking_lot_service.park_vehicle(VehicleType.TRUCK.value, "reg3", "Col1")
    pass