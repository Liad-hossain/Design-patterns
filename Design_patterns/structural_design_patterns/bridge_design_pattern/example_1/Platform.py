from abc import ABC, abstractmethod
from Design_patterns.structural_design_patterns.bridge_design_pattern.example_1.Notification import Notification


class Platform(ABC):
    def __init__(self, notification: Notification) -> None:
        self.notification = notification

    @abstractmethod
    def deliver(self, message: str) -> str:
        pass
