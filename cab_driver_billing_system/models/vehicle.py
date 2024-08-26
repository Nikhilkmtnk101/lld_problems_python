class Vehicle:
    def __init__(self, vehicle_id, name, vehicle_type):
        self.vehicle_id = vehicle_id
        self.name = name
        self.vehicle_type = vehicle_type

    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def get_vehicle_id(self):
        return self.vehicle_id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def get_vehicle_type(self):
        return self.vehicle_type
