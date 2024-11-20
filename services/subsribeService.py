from repository.topicsRepository import TopicRepository
from models.subscriber import Subscriber
from models.topic import Topic

class SubscribeService:
    def __init__(self) -> None:
        self.topic_repo = TopicRepository()

    
    def subscribe(self, subscriber: Subscriber , topic_name: str)->bool:
        topic: Topic=self.topic_repo.get_topic(topic_name)

        if not topic:
            return False
        
        subscriber.add_topic(topic)
        topic.add_subsriber(subscriber)
        return True
    
    def unsubscribe(self, subscriber: Subscriber , topic_name: str)->bool:
        topic: Topic=self.topic_repo.get_topic(topic_name)

        if not topic:
            return False
        
        subscriber.remove_topic(topic)
        topic.remove_subscriber(subscriber)
        return True
    
    def read_all_message(self, subscriber: Subscriber, topic_name: str):
        topic: Topic=self.topic_repo.get_topic(topic_name)
        if not topic:
            return []
        sub_topic, counter = subscriber.get_topic(topic_name)

        if sub_topic==None:
            return []

        messages=[]

    
        for message in topic.get_message_queue():
            messages.append(message.get_content())
        
        return list(messages)
    
    def read_last_message(self, subscriber: Subscriber, topic_name: str):

        topic: Topic=self.topic_repo.get_topic(topic_name)
        if not topic:
            return []
        
        sub_topic, counter = subscriber.get_topic(topic_name)


        new_counter=counter+1
        subscriber.update_topic_counter(topic_name, new_counter)
        
        if sub_topic==None:
            return []
        message_queue=topic.get_message_queue()
        
        return message_queue[counter].get_content() if len(message_queue)>counter else None
    


