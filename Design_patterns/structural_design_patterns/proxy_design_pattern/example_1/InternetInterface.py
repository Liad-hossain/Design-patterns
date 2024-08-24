from abc import ABC, abstractmethod


class Internet(ABC):
    @abstractmethod
    def connect_to(self, server_host: str) -> None:
        pass
