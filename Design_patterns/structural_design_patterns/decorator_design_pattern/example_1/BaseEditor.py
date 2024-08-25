from Design_patterns.structural_design_patterns.decorator_design_pattern.example_1.EditorInterface import (
    TextEditor,
)


class BasicTextEditor(TextEditor):
    def __init__(self, text: str):
        self.text = text

    def set_text(self, text: str) -> None:
        self.text = text

    def get_text(self) -> str:
        return self.text

    def display(self) -> str:
        return self.text
