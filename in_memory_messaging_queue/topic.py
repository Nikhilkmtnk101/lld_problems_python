from abc import ABC, abstractmethod
from threading import Lock
from in_memory_messaging_queue.message import Message


class ITopic(ABC):
    @abstractmethod
    def publish_message(self, msg: str):
        pass

    @abstractmethod
    def read_message(self, offset: int) -> str:
        pass


class Topic(ITopic):
    def __init__(self):
        self.__messages = []
        self.__lock = Lock()

    def __get_messages(self) -> list[str]:
        return self.__messages

    def __get_lock(self) -> Lock:
        return self.__lock

    def publish_message(self, msg: Message):
        self.__get_lock().acquire()
        self.__messages.append(msg)
        self.__get_lock().release()

    def read_message(self, offset: int) -> Message:
        message = None
        self.__get_lock().acquire()

        if offset < len(self.__messages):
            message = self.__messages[offset]

        self.__get_lock().release()
        return message
