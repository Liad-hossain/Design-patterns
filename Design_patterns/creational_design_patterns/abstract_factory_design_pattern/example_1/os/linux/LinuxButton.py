from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.features.Button import \
    Button


class LinuxButton(Button):
    def create(self) -> None:
        print("Linux Button is created")
