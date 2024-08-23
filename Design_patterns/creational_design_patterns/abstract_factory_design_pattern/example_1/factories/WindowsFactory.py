from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.factories.UIFactory import \
    UIFactory
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.features.Button import \
    Button
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.features.Checkbox import \
    Checkbox
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.os.windows.WindowsButton import \
    WindowsButton
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.os.windows.WindowsCheckbox import \
    WindowsCheckbox


class WindowsFactory(UIFactory):
    def createButton(self) -> Button:
        return WindowsButton()

    def createCheckbox(self) -> Checkbox:
        return WindowsCheckbox()
