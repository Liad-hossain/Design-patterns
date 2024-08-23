from Design_patterns.creational_design_patterns.builder_design_pattern.example_1.concreate_builders.KidsMealBuilder import \
    KidsMealBuilder
from Design_patterns.creational_design_patterns.builder_design_pattern.example_1.concreate_builders.NonVegMealBuilder import \
    NonVegMealBuilder
from Design_patterns.creational_design_patterns.builder_design_pattern.example_1.concreate_builders.VegMealBuilder import \
    VegMealBuilder
from Design_patterns.creational_design_patterns.builder_design_pattern.example_1.Director import \
    Chef

vegmeal = VegMealBuilder()
print(Chef(vegmeal).get_meal())

print("")

nonvegmeal = NonVegMealBuilder()
print(Chef(nonvegmeal).get_meal())

print("")

kidsmeal = KidsMealBuilder()
print(Chef(kidsmeal).get_meal())
