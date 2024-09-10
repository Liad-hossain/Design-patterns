from Design_patterns.behavioral_design_patterns.momento_design_pattern.example_1.CareTaker import (
    Caretaker,
)
from Design_patterns.behavioral_design_patterns.momento_design_pattern.example_1.TextEditor import (
    TextEditor,
)

if __name__ == "__main__":
    editor = TextEditor()
    caretaker = Caretaker(editor)

    editor.write("Hello, world!")
    editor.show()
    caretaker.save()  # Save the initial state

    editor.write(" This is a text editor.")
    editor.show()
    caretaker.save()  # Save after more text

    editor.write(" Adding more text.")
    editor.show()

    caretaker.undo()  # Undo last action
    editor.show()

    caretaker.undo()  # Undo again
    editor.show()

    caretaker.redo()  # Redo last undone action
    editor.show()
