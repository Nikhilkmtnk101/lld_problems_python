from abc import ABC, abstractmethod
from threading import Lock

from consumer import Consumer
from producer import Producer
from queue_mediator import QueueMediator


class IQueueService(ABC):
    @abstractmethod
    def create_topic(self, topic_name: str):
        pass

    @abstractmethod
    def create_consumer(self, consumer_name: str):
        pass

    @abstractmethod
    def create_producer(self):
        pass


class QueueService(IQueueService):
    __instance = None
    __lock = Lock()

    def __new__(cls, *args, **kwargs):
        cls.__lock.acquire()
        if cls.__instance is None:
            cls.__instance = super().__new__(cls ,*args, **kwargs)
        cls.__lock.release()
        return cls.__instance

    def __init__(self):
        self.queue_mediator = QueueMediator()

    def create_topic(self, topic_name: str):
        self.queue_mediator.add_topic(topic_name)

    def create_consumer(self, consumer_name: str):
        return Consumer(consumer_name, self.queue_mediator)

    def create_producer(self):
        return Producer(self.queue_mediator)
