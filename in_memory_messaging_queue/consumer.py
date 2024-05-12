import time
from abc import ABC, abstractmethod
from threading import Thread
from message import Message
from queue_mediator import IQueueMediator


class IConsumer(ABC):
    @abstractmethod
    def subscribe_to_topic(self, topic_name: str):
        pass


class Consumer(IConsumer):
    def __init__(self, consumer_name: str, queue_mediator: IQueueMediator):
        self.consumer_name = consumer_name
        self.topics = []
        self.queue_mediator = queue_mediator
        self.topics_vs_offset = {}
        self.__init_thread()

    def __init_thread(self):
        thread = Thread(target=self.__consumer_runner)
        thread.start()

    def subscribe_to_topic(self, topic_name: str):
        self.queue_mediator.add_topic(topic_name)
        self.topics.append(topic_name)
        self.topics_vs_offset[topic_name] = -1

    def consume_message(self, msg: Message):
        print(f"{self.consumer_name} received message {msg.get_message()}" )

    def __consumer_runner(self):
        while True:
            for topic in self.topics:
                offset = self.topics_vs_offset.get(topic, -1)
                msg = self.queue_mediator.read_message_from_topic_if_present(topic, offset+1)
                if msg:
                    self.consume_message(msg)
                    self.topics_vs_offset[topic] = offset +1
            try:
                time.sleep(0.1)

            except Exception as e:
                print(f"Exception {e}")

