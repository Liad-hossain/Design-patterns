from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self, indent: str = "") -> None:
        pass
