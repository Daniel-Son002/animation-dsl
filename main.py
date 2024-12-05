from interpret import lexer, parser, interpret
from render import render_canvas

# S-expression DSL input
dsl_code = """
(circle (x 100) (y 150) (radius 50))
(square (x 200) (y 250) (side 100))
(line (x1 50) (y1 50) (x2 150) (y2 150))
"""

# Tokenize the DSL code
print("\nTokenizing...")
lexer.input(dsl_code)
tokens = list(lexer)
if not tokens:
    print("No tokens generated! Lexer might be failing.")
for token in tokens:
    print(token)

print("\nParsing...")
print(dsl_code)
ast = parser.parse(dsl_code, debug=True)
print("\nParsed AST:", ast)

if ast:
    print("\nInterpreting AST...")
    shapes = interpret(ast)
    print("Shapes:", shapes)
    print("\nRendering Canvas...")
    render_canvas(shapes)
else:
    print("Parsing failed. Unable to interpret or render.")
