from cab_driver_billing_system.models.trip import Trip
from cab_driver_billing_system.utils.trip_id_generator import TripIdGenerator


class TripRepository:
    def __init__(self):
        self.trips = {}
        self.trip_id_generator = TripIdGenerator()

    def create_driver(self, driver_id, distance, start_time, end_time, trip_type, trip_status):
        trip_id = self.trip_id_generator.get_next_trip_id()
        trip = Trip(trip_id, driver_id, distance, start_time, end_time, trip_type, trip_status)
        self.trips[trip_id] = trip

    def get_trips(self):
        return self.trips

    def get_trip_by_id(self, trip_id):
        return self.trips.get(trip_id, None)

    def get_trips_by_driver_id(self, driver_id):
        driver_trips = []
        for trip_id, trip in self.trips.items():
            if trip.get_driver_id() == driver_id:
                driver_trips.append(trip)

        return driver_trips
