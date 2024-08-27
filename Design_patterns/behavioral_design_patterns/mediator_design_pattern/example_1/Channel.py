from abc import ABC, abstractmethod


class Channel(ABC):
    def __init__(self, name: str):
        self.name = name
        self.users = []

    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def remove_user(self, user):
        pass

    @abstractmethod
    def send_message(self, sender, message):
        pass
