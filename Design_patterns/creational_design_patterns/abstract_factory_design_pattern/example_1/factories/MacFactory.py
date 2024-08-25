from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.factories.UIFactory import (
    UIFactory,
)
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.features.Button import (
    Button,
)
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.features.Checkbox import (
    Checkbox,
)
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.os.mac.MacButton import (
    MacButton,
)
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.os.mac.MacCheckbox import (
    MacCheckbox,
)


class MacFactory(UIFactory):
    def createButton(self) -> Button:
        return MacButton()

    def createCheckbox(self) -> Checkbox:
        return MacCheckbox()
