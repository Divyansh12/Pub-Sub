#Singleton Publisher
class Publisher:
    _instance=None
    _name: str=None
    def __new__(cls):
        if not cls._instance:
            cls._instance=super(Publisher, cls).__new__(cls)
            cls._name="Publisher"
        return cls._instance