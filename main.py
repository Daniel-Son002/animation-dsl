from interpret import lexer, parser, interpret
from render import render_canvas

# DSL input with user-defined shape
# Test inputs:

# (define star (cx 0) (cy 0) (radius 50) (
#     (line (x1 (- cx radius)) (y1 (- cy radius)) (x2 (+ cx radius)) (y2 (+ cy radius)))
#     (line (x1 (- cx radius)) (y1 (+ cy radius)) (x2 (+ cx radius)) (y2 (- cy radius)))
#     (line (x1 cx) (y1 (- cy radius)) (x2 cx) (y2 (+ cy radius)))
#     (line (x1 (- cx radius)) (y1 cy) (x2 (+ cx radius)) (y2 cy))
# ))
# (star (cx 250) (cy 250) (radius 100))


dsl_code = """
(line (x1 150) (y1 150) (x2 250) (y2 250))
(square (x 250) (y 250) (side 50))
(circle (x 150) (y 150) (radius 50))
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
    print(ast)
    shapes = interpret(ast)
    print("Shapes:", shapes)
    print("\nRendering Canvas...")
    render_canvas(shapes)
else:
    print("Parsing failed. Unable to interpret or render.")
