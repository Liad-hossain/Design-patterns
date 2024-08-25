from Design_patterns.structural_design_patterns.flyweight_design_pattern.example_1.GlyphFactory import (
    GlyphFactory,
)

if __name__ == "__main__":
    factory = GlyphFactory()

    # Render multiple characters on the screen
    positions = [(10, 20), (15, 20), (20, 20), (25, 20)]

    # Render 'H' multiple times with the same style
    for pos in positions:
        glyph_h = factory.get_glyph("H", "Arial", 12, "Black")
        glyph_h.render(pos)

    # Render 'e' with a different style and position
    glyph_e = factory.get_glyph("e", "Arial", 12, "Black")
    glyph_e.render((30, 20))

    # Render 'H' again with the same style as before
    glyph_h.render((35, 20))
