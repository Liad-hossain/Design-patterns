from Design_patterns.structural_design_patterns.composite_design_pattern.example_1.ComponentInterface import (
    FileSystemComponent,
)


class File(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self.name = name

    def show_details(self, indent: str = "") -> None:
        print(f"{indent}- {self.name}")
