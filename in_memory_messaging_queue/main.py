import time

from queue_service import QueueService

if __name__ == '__main__':
    queue_service = QueueService()
    topic1 = queue_service.create_topic("topic1")
    topic2 = queue_service.create_topic("topic2")
    producer1 = queue_service.create_producer()
    producer2 = queue_service.create_producer()
    consumer1 = queue_service.create_consumer("consumer1")
    consumer2 = queue_service.create_consumer("consumer2")
    consumer3 = queue_service.create_consumer("consumer3")
    consumer4 = queue_service.create_consumer("consumer4")
    consumer5 = queue_service.create_consumer("consumer5")
    consumer1.subscribe_to_topic("topic1")
    consumer2.subscribe_to_topic("topic1")
    consumer3.subscribe_to_topic("topic1")
    consumer4.subscribe_to_topic("topic1")
    consumer5.subscribe_to_topic("topic1")
    consumer1.subscribe_to_topic("topic2")
    consumer3.subscribe_to_topic("topic2")
    consumer5.subscribe_to_topic("topic2")
    producer1.publish_message_to_topic("topic1", "Message 1")
    producer1.publish_message_to_topic("topic1", "Message 2")
    producer1.publish_message_to_topic("topic2", "Message 4")
    producer2.publish_message_to_topic("topic1", "Message 3")
    producer2.publish_message_to_topic("topic2", "Message 5")
