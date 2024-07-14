from parking_lot.dao.ticket_dao import TicketDao
from parking_lot.dao.vehicle_dao import VehicleDao
from parking_lot.entities.parking_lot import ParkingLot
from parking_lot.entities.ticket import Ticket
from parking_lot.entities.vehicle import Vehicle
from parking_lot.enum import VehicleType
from parking_lot.parking_strategy.natural_order_parking_stategy import NaturalParkingStrategy


class ParkingLotService:
    def __init__(self):
        self.parking_strategy = NaturalParkingStrategy()
        self.ticket_dao = TicketDao()
        self.vehicle_dao = VehicleDao()
        self.parking_lot = None

    @staticmethod
    def __get_ticket_id(parking_lot_id: str, slot_id: int, slot_per_floor: int) -> str:
        floor_no = int((slot_id / slot_per_floor)) + 1
        slot_no = int((slot_id % slot_per_floor)) + 1
        ticket_id = f'{parking_lot_id}_{floor_no}_{slot_no}'
        return ticket_id

    "Public Methods"

    def create_parking_lot(self, parking_lot_id: str, no_of_floors: int, slot_per_floor: int):
        self.parking_lot = ParkingLot(parking_lot_id, no_of_floors, slot_per_floor)
        slot_id = 0
        slots = self.parking_lot.get_slots()
        for i in range(0, no_of_floors):
            for j in range(0, slot_per_floor):
                if j < 1:
                    slots[slot_id].set_supported_vehicle_type(VehicleType.TRUCK.value)
                elif j < 3:
                    slots[slot_id].set_supported_vehicle_type(VehicleType.BIKE.value)
                else:
                    slots[slot_id].set_supported_vehicle_type(VehicleType.CAR.value)
                slot_id += 1


        print(f'Created parking lot with {no_of_floors} floors and {slot_per_floor} slots per floor')

    def park_vehicle(self, vehicle_type: str, reg_no: str, color: str):
        vehicle = Vehicle(vehicle_type, reg_no, color)
        slots = self.parking_lot.get_slots()
        free_slot = self.parking_strategy.get_free_slot(slots, vehicle_type)
        if not free_slot:
            print("Parking Lot Full")
            return
        else:
            ticket_id = self.__get_ticket_id(
                self.parking_lot.get_parking_lot_id(),
                free_slot.get_slot_id(),
                self.parking_lot.get_no_slots_per_floor()
            )
            ticket = Ticket(ticket_id, vehicle.get_reg_no(), free_slot.get_slot_id())
            free_slot.book_slot()
            self.vehicle_dao.add_vehicle(vehicle)
            self.ticket_dao.add_ticket(ticket)
            print(f"Ticket ID: {ticket_id}")
            return ticket_id

    def unpark_vehicle(self, ticket_id: str):
        ticket = self.ticket_dao.get_ticket_by_id(ticket_id)
        if not ticket:
            print('Invalid Ticket')
            return

        vehicle = self.vehicle_dao.get_vehicle_by_reg_no(ticket.get_vehicle_reg_no())
        print(f'Unparked vehicle with Registration Number: {vehicle.get_reg_no()} and Color: {vehicle.get_color()}')
