class Driver:
    def __init__(self, driver_id, name, phone_no, driving_licence_no):
        self.driver_id = driver_id
        self.name = name
        self.phone_no = phone_no
        self.driving_licence_no = driving_licence_no

    def set_driver_id(self, driver_id):
        self.driver_id = driver_id

    def get_driver_id(self):
        return self.driver_id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_phone_no(self, phone_no):
        self.phone_no = phone_no

    def get_phone_no(self):
        return self.phone_no

    def set_driving_licence_no(self, driving_licence_no):
        self.driving_licence_no = driving_licence_no

    def get_driving_licence_no(self):
        return self.driving_licence_no
