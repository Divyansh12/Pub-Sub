import uuid

class Message:
    def __init__(self, content: str, message_id:str = None) -> None:
        self.id=message_id or str(uuid.uuid4())
        self.content=content
        
        #Additional
        self.metadata={}

    def get_content(self):
        return self.content

        