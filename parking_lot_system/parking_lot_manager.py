from parking_lot_system.enums import VehicleType, get_slot_type_from_vehicle_type
from parking_lot_system.models.parking_lot import ParkingLot
from parking_lot_system.models.slot import TruckSlot, BikeSlot, CarSlot
from parking_lot_system.models.ticket import Ticket
from parking_lot_system.models.vehicle import Vehicle
from parking_lot_system.parking_startegy import ParkingStrategy


class ParkingLotManager:
    def __init__(self):
        self.parking_lot = None
        self.parking_strategy = None
        self.tickets = {}
        self.vehicles = {}

    def get_parking_strategy(self) -> ParkingStrategy:
        return self.parking_strategy

    def set_parking_strategy(self, parking_strategy: ParkingStrategy):
        self.parking_strategy = parking_strategy

    def create_vehicle(self, registration_no: str, vehicle_type: VehicleType, color: str):
        self.vehicles[registration_no] = Vehicle(registration_no, vehicle_type, color)
        return self.vehicles[registration_no]

    def create_parking_lot(self, parking_lot_id: str, no_of_floor: int, slots_per_floor: int):
        self.parking_lot = ParkingLot(parking_lot_id, no_of_floor, slots_per_floor)
        slots = []
        count = 0

        for i in range(1, no_of_floor+1):
            floor_slots = []

            for j in range(1, slots_per_floor+1):
                count = count + 1
                if j <= 1:
                    slot = TruckSlot(count, i, j)
                elif j <= 3:
                    slot = BikeSlot(count, i, j)
                else:
                    slot = CarSlot(count, i, j)

                floor_slots.append(slot)

            slots.append(floor_slots)

        self.parking_lot.set_slots(slots)

        print(f'Created parking lot with {no_of_floor} floors and {slots_per_floor} slots per floor')

    def park_vehicle(self, registration_no: str, vehicle_type: VehicleType, color: str):

        if not self.vehicles.get(registration_no, None):
            self.create_vehicle(registration_no, vehicle_type, color)

        parking_strategy = self.get_parking_strategy()
        slot = parking_strategy.get_first_available_slot(get_slot_type_from_vehicle_type(vehicle_type))
        no_of_floor = self.parking_lot.get_no_of_floor()
        slots_per_count = self.parking_lot.get_slot_per_floor()

        if slot is None:
            print(f"Parking Lot Full")
            return

        slot.book_slot()
        ticket = Ticket(self.parking_lot.parking_lot_id, slot.floor_no, slot.slot_no, registration_no)
        self.tickets[ticket.get_ticket_id()] = ticket
        print(f"Parked vehicle. Ticket ID: {ticket.get_ticket_id()}")

    def unpark_vehicle(self, ticket_id: str):
        slots = self.parking_lot.get_slots()
        ticket = self.tickets.get(ticket_id, None)

        if (not ticket) or slots[ticket.floor_no-1][ticket.slot_no-1].is_slot_available():
            print("Invalid Ticket")
            return

        slots[ticket.floor_no-1][ticket.slot_no-1].free_slot()
        vehicle = self.vehicles[ticket.vehicle_registration_no]

        print(f'Unparked vehicle with Registration Number: {vehicle.get_registration_number()} '
              f'and Color: {vehicle.get_color()}')
