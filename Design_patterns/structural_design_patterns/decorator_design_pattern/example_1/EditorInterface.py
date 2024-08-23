from abc import ABC, abstractmethod


class TextEditor(ABC):
    @abstractmethod
    def set_text(self, text: str) -> None:
        pass

    @abstractmethod
    def get_text(self) -> str:
        pass

    @abstractmethod
    def display(self) -> str:
        pass
