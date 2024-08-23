from Design_patterns.creational_design_patterns.abstract_factory_design_pattern.example_1.features.Checkbox import \
    Checkbox


class LinuxCheckbox(Checkbox):
    def create(self) -> None:
        print("Linux Checkbox is created")
