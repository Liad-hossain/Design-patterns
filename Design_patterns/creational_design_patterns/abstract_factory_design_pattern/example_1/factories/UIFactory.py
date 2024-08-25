from abc import abstractmethod

from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.features.Button import (
    Button,
)
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.features.Checkbox import (
    Checkbox,
)


class UIFactory:
    @abstractmethod
    def createButton(self) -> Button:
        pass

    @abstractmethod
    def createCheckbox(self) -> Checkbox:
        pass
