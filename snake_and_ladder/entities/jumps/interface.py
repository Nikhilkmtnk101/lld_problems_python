from abc import ABC, abstractmethod


class IJumps(ABC):
    @abstractmethod
    def get_start_position(self):
        pass

    @abstractmethod
    def get_end_position(self):
        pass
