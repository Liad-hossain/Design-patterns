from Design_patterns.structural_design_patterns.decorator_design_pattern.example_1.BaseDecorator import EditorDecorator


class AutoSaveDecorator(EditorDecorator):
    def set_text(self, text: str) -> None:
        self.editor.set_text(text)

    def get_text(self) -> str:
        return self.editor.get_text()

    def display(self) -> str:
        editor_display = self.editor.display()
        saved_text = self._auto_save(self.editor.get_text())
        self.set_text(saved_text)

        return editor_display + '\n' + "Auto saved: " + saved_text

    def _auto_save(self, text: str) -> str:
        return text
