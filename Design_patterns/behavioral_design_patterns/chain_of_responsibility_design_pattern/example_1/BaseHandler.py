from abc import ABC, abstractmethod


class SupportHandler(ABC):
    def __init__(self, next_handler=None) -> None:
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, request) -> str:
        pass
