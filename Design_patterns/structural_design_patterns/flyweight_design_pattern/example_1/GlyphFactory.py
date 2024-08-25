from Design_patterns.structural_design_patterns.flyweight_design_pattern.example_1.Character import (
    Character,
)


class GlyphFactory:
    def __init__(self):
        self._glyphs = {}

    def get_glyph(self, char: str, font: str, size: int, color: str) -> Character:
        key = (char, font, size, color)
        if key not in self._glyphs:
            self._glyphs[key] = Character(char, font, size, color)
            print(
                f"Creating new glyph: '{char}', font={font}, size={size}, color={color}",
            )
        else:
            print(
                f"Reusing existing glyph: '{char}', font={font}, size={size}, color={color}",
            )
        return self._glyphs[key]
