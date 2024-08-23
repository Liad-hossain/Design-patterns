from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.features.Button import \
    Button


class MacButton(Button):
    def create(self) -> None:
        print("Mac Button is created")
