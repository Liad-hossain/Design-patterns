from Design_patterns.structural_design_patterns.composite_design_pattern.example_1.ComponentInterface import (
    FileSystemComponent,
)


class Directory(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent) -> None:
        self.children.append(component)

    def remove(self, component: FileSystemComponent) -> None:
        self.children.remove(component)

    def show_details(self, indent: str = "") -> None:
        print(f"{indent}+ {self.name}")
        for child in self.children:
            child.show_details(indent + " ")
