from abc import abstractmethod, ABC
from collections import OrderedDict
from threading import Lock

from message import Message
from topic import Topic


class IQueueMediator(ABC):
    @abstractmethod
    def add_topic(self, topic_name: str):
        pass

    @abstractmethod
    def publish_message_to_topic(self, topic_name: str, msg: Message):
        pass

    @abstractmethod
    def read_message_from_topic_if_present(self, topic_name: str, offset:int) -> Message:
        pass


class QueueMediator(IQueueMediator):
    __instance = None
    __lock = Lock()

    def __new__(cls, *args, **kwargs):
        cls.__lock.acquire()
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        cls.__lock.release()
        return cls.__instance

    def __init__(self):
        self.__topics = OrderedDict()

    def add_topic(self, topic_name: str):
        if not self.__topics.get(topic_name, False):
            self.__topics[topic_name] = Topic()

    def publish_message_to_topic(self, topic_name: str, msg: Message):
        self.add_topic(topic_name)
        self.__topics[topic_name].publish_message(msg)

    def read_message_from_topic_if_present(self, topic_name: str, offset: int) -> Message:
        return self.__topics[topic_name].read_message(offset)
