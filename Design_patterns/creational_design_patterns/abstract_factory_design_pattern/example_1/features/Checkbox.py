from abc import ABC, abstractmethod


class Checkbox(ABC):
    @abstractmethod
    def create(self) -> None:
        pass
