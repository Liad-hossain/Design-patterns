from Design_patterns.structural_design_patterns.flyweight_design_pattern.example_1.Glyph import (
    Glyph,
)


class Character(Glyph):
    def __init__(self, char: str, font: str, size: int, color: str):
        self.char = char
        self.font = font
        self.size = size
        self.color = color

    def render(self, position: tuple) -> None:
        print(
            f"Rendering '{self.char}' at {position} with font={self.font}, size={self.size}, color={self.color}",
        )
