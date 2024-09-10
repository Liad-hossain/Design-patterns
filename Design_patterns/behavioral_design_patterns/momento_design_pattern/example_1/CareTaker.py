from Design_patterns.behavioral_design_patterns.momento_design_pattern.example_1.TextEditor import (
    TextEditor,
)


class Caretaker:
    def __init__(self, editor: TextEditor):
        self._editor = editor
        self._history = []
        self._redo_stack = []

    def save(self):
        print("Caretaker: Saving current state.")
        self._history.append(self._editor.save())
        self._redo_stack.clear()  # Once a new change is made, redo history is cleared.

    def undo(self):
        if not self._history:
            print("Caretaker: No states to undo.")
            return
        print("Caretaker: Undoing last state.")
        self._redo_stack.append(self._editor.save())  # Save current state for redo
        memento = self._history.pop()
        self._editor.restore(memento)

    def redo(self):
        if not self._redo_stack:
            print("Caretaker: No states to redo.")
            return
        print("Caretaker: Redoing last undone state.")
        self._history.append(self._editor.save())  # Save current state for undo
        memento = self._redo_stack.pop()
        self._editor.restore(memento)
