from abc import ABC, abstractmethod

from message import Message
from queue_mediator import IQueueMediator


class IProducer(ABC):
    @abstractmethod
    def publish_message_to_topic(self, topic_name: str, msg: str):
        pass


class Producer(IProducer):
    def __init__(self, queue_mediator: IQueueMediator):
        self.__queue_mediator = queue_mediator

    def publish_message_to_topic(self, topic_name: str, msg: str):
        message = Message(msg)
        self.__queue_mediator.publish_message_to_topic(topic_name, message)

