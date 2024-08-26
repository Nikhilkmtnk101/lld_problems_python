class TripIdGenerator:
    trip_id = 0

    @classmethod
    def get_next_trip_id(cls):
        cls.trip_id += 1
        return cls.trip_id
