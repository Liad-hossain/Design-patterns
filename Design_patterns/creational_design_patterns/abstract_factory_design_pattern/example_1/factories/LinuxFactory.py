from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.factories.UIFactory import \
    UIFactory
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.features.Button import \
    Button
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.features.Checkbox import \
    Checkbox
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.os.linux.LinuxButton import \
    LinuxButton
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.os.linux.LinuxCheckbox import \
    LinuxCheckbox


class LinuxFactory(UIFactory):
    def createButton(self) -> Button:
        return LinuxButton()

    def createCheckbox(self) -> Checkbox:
        return LinuxCheckbox()
