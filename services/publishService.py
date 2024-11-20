from repository.topicsRepository import TopicRepository
from models.publisher import Publisher
from models.message import Message

class PublishService:
    def __init__(self) -> None:
        self.topic_repo=TopicRepository()
        self.publisher=Publisher()

    
    def publish_to_all(self, content:str):
        message = Message(content=content)

        results={}

        for topic in self.topic_repo.get_all_topics():
            try:
                topic.add_message(message)
                results[topic.name]=True
            except Exception as e:
                print(e)
                print(f"Error Publishing the message to topic: {topic.name}")
                results[topic.name]=False
        return results
    