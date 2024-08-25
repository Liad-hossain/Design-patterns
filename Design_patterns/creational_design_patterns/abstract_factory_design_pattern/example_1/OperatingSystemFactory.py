from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.factories.LinuxFactory import (
    LinuxFactory,
)
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.factories.MacFactory import (
    MacFactory,
)
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.factories.UIFactory import (
    UIFactory,
)
from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.factories.WindowsFactory import (
    WindowsFactory,
)


class OperatingSystemFactory:
    def __init__(self, factory: UIFactory) -> None:
        self.button = factory.createButton()
        self.checkbox = factory.createCheckbox()

    def create_ui(self) -> None:
        self.button.create()
        self.checkbox.create()


if __name__ == "__main__":
    factory = WindowsFactory()
    os = OperatingSystemFactory(factory)
    os.create_ui()

    print("")

    factory = LinuxFactory()
    os = OperatingSystemFactory(factory)
    os.create_ui()

    print("")

    factory = MacFactory()
    os = OperatingSystemFactory(factory)
    os.create_ui()
