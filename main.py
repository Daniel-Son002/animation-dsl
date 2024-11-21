from interpret import interpret

# Example DSL script
dsl_code = """
circle x=100 y=150 radius=50
square x=200 y=250 side=100
"""
interpret(dsl_code)
