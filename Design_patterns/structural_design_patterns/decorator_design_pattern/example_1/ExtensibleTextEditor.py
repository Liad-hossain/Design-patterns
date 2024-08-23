from Design_patterns.structural_design_patterns.decorator_design_pattern.example_1.BaseEditor import BasicTextEditor
from Design_patterns.structural_design_patterns.decorator_design_pattern.example_1.decorators.AutoSaver import AutoSaveDecorator
from Design_patterns.structural_design_patterns.decorator_design_pattern.example_1.decorators.GrammerChecker import GrammerCheckDecorator
from Design_patterns.structural_design_patterns.decorator_design_pattern.example_1.decorators.SpellingChecker import SpellCheckDecorator


if __name__ == "__main__":

    text_editor = AutoSaveDecorator(GrammerCheckDecorator(SpellCheckDecorator(BasicTextEditor("This are a simple text editor for hte testing purpose."))))

    print(text_editor.display())
