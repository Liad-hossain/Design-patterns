from Design_patterns.structural_design_patterns.decorator_design_pattern.example_1.EditorInterface import TextEditor
from abc import abstractmethod


class EditorDecorator(TextEditor):
    def __init__(self, editor: TextEditor):
        self.editor = editor

    @abstractmethod
    def set_text(self, text: str) -> None:
        pass

    def get_text(self) -> str:
        pass

    @abstractmethod
    def display(self) -> str:
        pass
