from abc import ABC, abstractmethod


class Observer(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def update(self, temperature: float, humidity: float) -> None:
        pass
