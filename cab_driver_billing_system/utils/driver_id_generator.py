class DriverIdGenerator:
    driver_id = 0

    @classmethod
    def get_next_driver_id(cls):
        cls.driver_id += 1
        return cls.driver_id
