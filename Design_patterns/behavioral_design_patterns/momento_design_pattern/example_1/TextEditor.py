from Design_patterns.behavioral_design_patterns.momento_design_pattern.example_1.Momento import (
    Momento,
)


class TextEditor:
    def __init__(self):
        self._text = ""

    def write(self, text: str) -> None:
        self._text += text

    def show(self) -> None:
        print(f"Current Text: {self._text}")

    def save(self) -> Momento:
        return Momento(self._text)

    def restore(self, momento: Momento) -> None:
        self._text = momento.get_state()
