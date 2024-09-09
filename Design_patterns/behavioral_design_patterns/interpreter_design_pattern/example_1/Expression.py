from abc import ABC, abstractmethod

from Design_patterns.behavioral_design_patterns.interpreter_design_pattern.example_1.Context import (
    Context,
)


class Expression(ABC):
    @abstractmethod
    def interpret(self, context: Context) -> None:
        pass
