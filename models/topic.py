from collections import deque

class Topic:
    def __init__(self, name: str) -> None:
        self.name=name
        self.messages=deque()
        self.subscribers=set()

    def get_name(self):
        return self.name

    
    def add_message(self, message):
        self.messages.append(message)
    
    def add_subsriber(self, subscriber):
        
        if subscriber not in self.subscribers:
            self.subscribers.add(subscriber)

    def remove_subscriber(self, subscriber):
        if subscriber in self.subscriber:
            self.subscribers.remove(subscriber)

    def get_subsribers(self):
        return self.subscribers

    def get_message_queue(self):
        return self.messages
        
    
    # def __str__(self) -> str:
    #     return self.name
    
    def __repr__(self) -> str:
        return f"{self.name}"
        