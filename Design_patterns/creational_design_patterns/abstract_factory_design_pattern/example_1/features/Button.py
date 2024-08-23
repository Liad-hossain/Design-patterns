from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def create(self) -> None:
        pass
