from Design_patterns.creational_design_patterns.factory_design_pattern.example_1.factories.OperatingSystem import (
    OperatingSystem,
)


class WindowsOperatingSystem(OperatingSystem):

    def get_specifications(self) -> str:
        print(f"-----Specifications are given below------")
        print(f"Operating System: {self.get_name()}")
        print(f"Version: {self.get_version()}")
        print(f"Architecture: {self.get_architecture()}")
