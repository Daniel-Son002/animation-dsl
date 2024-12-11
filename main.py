# from interpret import lexer, parser, interpret_with_manim
# from manim import config

# # Configure Manim output
# config.media_dir = "./media"

# # DSL input for testing Manim integration
# dsl_code = """
# (animate circle (x 0) (y 0) (radius 1) (end_x 2) (end_y 2) (duration 2))
# """

# # Tokenize the DSL code
# print("\nTokenizing...")
# lexer.input(dsl_code)
# tokens = list(lexer)
# if not tokens:
#     print("No tokens generated! Lexer might be failing.")
# for token in tokens:
#     print(token)

# # Parse the DSL code
# print("\nParsing...")
# ast = parser.parse(dsl_code, debug=True)
# print("\nParsed AST:", ast)

# if ast:
#     print("\nGenerating Manim Scene...")
#     DSLScene = interpret_with_manim(ast)
#     scene = DSLScene()
#     scene.render()
# else:
#     print("Parsing failed. Unable to interpret or render.")

from interpret import lexer, parser, interpret
from render import render_canvas, render_animation

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
(circle (x 150) (y 150) (radius 50) (color "red") (fill true))
(square (x 250) (y 250) (side 50) (color "blue") (fill false))
(line (x1 150) (y1 150) (x2 250) (y2 250) (color "green"))
"""

print("\nTokenizing...")
lexer.input(dsl_code)
tokens = list(lexer)
for token in tokens:
    print(token)

print("\nParsing...")
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

# dsl_code_animation = """
# (animate line (x1 100) (y1 100) (x2 200) (y2 200) (end_x1 300) (end_y1 300) (end_x2 400) (end_y2 400) (duration 2))
# """

# print("\nAnimating...")
# ast = parser.parse(dsl_code_animation, debug=True)
# if ast:
#     shapes_per_frame = []
#     for shape_type, params in ast:
#         start_params = {k: params[k] for k in params if not k.startswith("end_") and k != "duration"}
#         end_params = {k[4:]: params[k] for k in params if k.startswith("end_")}
#         duration = params["duration"]
#         frames = animate_object(shape_type, start_params, end_params, duration)
#         shapes_per_frame.extend(frames)
    
#     render_animation(shapes_per_frame)
# else:
#     print("Parsing failed for animation test.")