from abc import ABC, abstractmethod


class Glyph(ABC):
    @abstractmethod
    def render(self, position: tuple) -> None:
        pass
