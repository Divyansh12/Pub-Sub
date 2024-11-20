from models.topic import Topic
from typing import Dict

class TopicRepository:
    _instance=None

    def __new__(cls) -> Topic:
        if not cls._instance:
            cls._instance=super(TopicRepository, cls).__new__(cls)
            # cls._instance.topics: Dict[str, Topic]={}
        return cls._instance
    
    def __init__(self) -> None:
        self.topics: Dict[str, Topic]={}
        
    def create_topic(self, name: str)->Topic:
        if name not in self.topics:
            self.topics[name]=Topic(name)

        return self.topics[name]
    
    def get_topic(self, name: str):
        return self.topics[name]
    
    def get_all_topics(self):
        return list(self.topics.values())

    #Additional
    def delete_topic(self):
        pass

