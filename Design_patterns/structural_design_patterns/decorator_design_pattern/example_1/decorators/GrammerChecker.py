from Design_patterns.structural_design_patterns.decorator_design_pattern.example_1.BaseDecorator import EditorDecorator


class GrammerCheckDecorator(EditorDecorator):

    def set_text(self, text: str) -> None:
        self.editor.set_text(text)

    def get_text(self) -> str:
        return self.editor.get_text()

    def display(self) -> str:
        editor_display = self.editor.display()
        corrected_text = self._check_grammer(self.editor.get_text())
        self.set_text(corrected_text)

        return editor_display + '\n' + "Grammer checked: " + corrected_text

    def _check_grammer(self, text: str) -> str:
        return text.replace("are a", "is a")
