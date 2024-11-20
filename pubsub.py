from services.publishService import PublishService
from services.subsribeService import SubscribeService
from repository.topicsRepository import TopicRepository
from models.subscriber import Subscriber

def pubsub():
    publish_service = PublishService()
    subscribe_service = SubscribeService()

    topic_repo = TopicRepository()

    # Create multiple topics for testing
    topic_repo.create_topic("topic1")
    topic_repo.create_topic("topic2")
    topic_repo.create_topic("topic3")
    topic_repo.create_topic("topic4")  # New topic for testing
    topic_repo.create_topic("topic5")  # New topic for testing

    subscriber1 = Subscriber('sub1')
    subscriber2 = Subscriber('sub2')
    subscriber3 = Subscriber('sub3')  # New subscriber for testing

    # Subscribe subscribers to various topics
    subscribe_service.subscribe(subscriber1, 'topic1')
    subscribe_service.subscribe(subscriber1, 'topic2')
    subscribe_service.subscribe(subscriber1, 'topic3')

    subscribe_service.subscribe(subscriber2, 'topic2')
    subscribe_service.subscribe(subscriber2, 'topic3')
    subscribe_service.subscribe(subscriber2, 'topic4')  # New subscription for testing

    subscribe_service.subscribe(subscriber3, 'topic1')  # New subscription for testing
    subscribe_service.subscribe(subscriber3, 'topic5')  # New subscription for testing

    # Publish messages to all topics
    publish_service.publish_to_all("Message1")
    publish_service.publish_to_all("Message2")  # New message for testing

    messages_sub1 = subscribe_service.read_all_message(subscriber1, 'topic1')
    messages_sub2 = subscribe_service.read_all_message(subscriber2, 'topic1')
    messages_sub3 = subscribe_service.read_all_message(subscriber3, 'topic1')  # New message read for testing

    messages_sub2_last = subscribe_service.read_last_message(subscriber2, 'topic2')
    messages_sub3_last = subscribe_service.read_last_message(subscriber3, 'topic5')  # New last message read for testing

    print("Subscriber 1 message for topic 1 : ", messages_sub1)
    print("Subscriber 2 message for topic 1 : ", messages_sub2)
    print("Subscriber 3 message for topic 1 : ", messages_sub3)  # New print for testing

    print("Subscriber 2 last message for topic 2 : ", messages_sub2_last)
    print("Subscriber 3 last message for topic 5 : ", messages_sub3_last)  # New print for testing

if __name__ == "__main__":
    pubsub()