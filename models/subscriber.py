class Subscriber:
    
    def __init__(self, subsriber_name: str) -> None:
        self.subsriber_name=subsriber_name
        self.subsribed_topics={}
    

    def get_topic(self, topic):
        if topic in self.subsribed_topics:
            return topic, self.subsribed_topics[topic]
        return None, None
        

    def add_topic(self, topic):
        if topic.get_name() not in self.subsribed_topics: 
            self.subsribed_topics[topic.get_name()] = 0
            return True
        return False
    
    def add_topic_counter(self, topic, counter):
        if topic not in self.subsribed_topics: 
            self.subsribed_topics[topic] = counter
            return True
        return False
    
    def update_topic_counter(self, topic, counter):
        if topic in self.subsribed_topics:
            self.subsribed_topics[topic] = counter
        else:
            self.add_topic_counter(topic, counter)
        
    def remove_topic(self, topic):
        if topic in self.subsribed_topics:
            del self.subsribed_topics[topic]
            return True
        return False