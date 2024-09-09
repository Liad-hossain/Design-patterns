from Design_patterns.behavioral_design_patterns.interpreter_design_pattern.example_1.Context import (
    Context,
)
from Design_patterns.behavioral_design_patterns.interpreter_design_pattern.example_1.Expression import (
    Expression,
)
from Design_patterns.behavioral_design_patterns.interpreter_design_pattern.example_1.expressions.AndExpression import (
    AndExpression,
)
from Design_patterns.behavioral_design_patterns.interpreter_design_pattern.example_1.expressions.SelectExpression import (
    SelectExpression,
)
from Design_patterns.behavioral_design_patterns.interpreter_design_pattern.example_1.expressions.WhereExpression import (
    WhereExpression,
)

# Interpreter class to combine all expressions and process the query


class QueryInterpreter:
    def __init__(self, select_expr: Expression, where_expr: Expression = None):
        self.select_expr = select_expr
        self.where_expr = where_expr

    def interpret(self, context):
        if self.where_expr:
            filtered_data = self.where_expr.interpret(context)
            filtered_context = Context(filtered_data)
            return self.select_expr.interpret(filtered_context)
        else:
            return self.select_expr.interpret(context)


if __name__ == "__main__":
    # Example Data (Context)
    data = [
        {"name": "John", "age": 28, "city": "New York"},
        {"name": "Jane", "age": 32, "city": "London"},
        {"name": "Doe", "age": 23, "city": "New York"},
        {"name": "Alice", "age": 28, "city": "Paris"},
    ]

    context = Context(data)

    # Example query: SELECT name, age WHERE city = 'New York' AND age = 28
    select_expr = SelectExpression(columns=["name", "age"])
    where_expr_city = WhereExpression(column="city", value="New York")
    where_expr_age = WhereExpression(column="age", value=28)
    and_expr = AndExpression(where_expr_city, where_expr_age)

    # Interpreter to handle the query
    interpreter = QueryInterpreter(select_expr=select_expr, where_expr=and_expr)

    # Execute the query
    result = interpreter.interpret(context)
    print(result)
