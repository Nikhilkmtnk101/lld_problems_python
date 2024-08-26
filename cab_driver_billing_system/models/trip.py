class Trip:
    def __init__(self, trip_id, driver_id, distance, start_time, end_time, trip_type, status):
        self.trip_id = trip_id
        self.driver_id = driver_id
        self.distance = distance
        self.start_time = start_time
        self.end_time = end_time
        self.trip_type = trip_type
        self.status = status

    def set_trip_id(self, trip_id):
        self.trip_id = trip_id

    def get_trip_id(self):
        return self.trip_id

    def set_driver_id(self, driver_id):
        self.driver_id = driver_id

    def get_driver_id(self):
        return self.driver_id

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_start_time(self):
        return self.start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def get_end_time(self):
        return self.end_time

    def set_trip_type(self, trip_type):
        self.trip_type = trip_type

    def get_trip_type(self):
        return self.trip_type

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
