"""
Problem Statement: https://workat.tech/machine-coding/practice/design-parking-lot-qm6hwq4wkhp8
"""
from parking_lot_system.enums import VehicleType
from parking_lot_system.parking_lot_manager import ParkingLotManager
from parking_lot_system.parking_startegy import NaturalOrderParkingStrategy

if __name__ == '__main__':
   parking_lot_manager = ParkingLotManager()
   parking_lot_manager.create_parking_lot("PR1234", 2, 6)
   parking_lot_manager.set_parking_strategy(NaturalOrderParkingStrategy(2, 6, parking_lot_manager.parking_lot.get_slots()))
   parking_lot_manager.park_vehicle("KA-01-DB-1234", VehicleType.CAR, "black")
   parking_lot_manager.park_vehicle("KA-02-CB-1334", VehicleType.CAR, "red")
   parking_lot_manager.park_vehicle("KA-01-DB-1133", VehicleType.CAR, "black")
   parking_lot_manager.park_vehicle("KA-05-HJ-8432", VehicleType.CAR, "white")
   parking_lot_manager.park_vehicle("WB-45-HO-9032", VehicleType.CAR, "white")
   parking_lot_manager.park_vehicle("KA-01-DF-8230", VehicleType.CAR, "black")
   parking_lot_manager.park_vehicle("KA-21-HS-2347", VehicleType.CAR, "red")
   parking_lot_manager.unpark_vehicle("PR1234_2_5")
   parking_lot_manager.unpark_vehicle("PR1234_2_5")
   parking_lot_manager.unpark_vehicle("PR1234_2_7")

