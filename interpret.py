import ply.lex as lex
import ply.yacc as yacc
from primitive import Circle, Square, Line
from math import cos, sin, pi

start = 'sexpr_list'

# Token definitions
tokens = (
    'LPAREN', 'RPAREN', 'ID', 'NUMBER', 'DEFINE'
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_DEFINE = r'define'

# Number token
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = ' \t\n'

# Error handling for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# User-defined shapes storage
user_shapes = {}

# Grammar rules
def p_sexpr_list(p):
    '''sexpr_list : sexpr
                  | sexpr_list sexpr'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_sexpr(p):
    '''sexpr : LPAREN ID param_list RPAREN
             | define_expr'''
    if isinstance(p[1], tuple):  # If `p[1]` is a tuple, it's a defined shape
        p[0] = p[1]
    else:
        p[0] = (p[2], dict(p[3]))

def p_define_expr(p):
    '''define_expr : LPAREN DEFINE ID param_list LPAREN sexpr_list RPAREN RPAREN'''
    shape_name = p[3]
    params = dict(p[4])  # List of parameter defaults
    body = p[6]          # Body of the shape
    user_shapes[shape_name] = (params, body)  # Store the custom shape
    p[0] = None  # `define` does not return a value directly

def p_param_list(p):
    '''param_list : param
                  | param_list param'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_param(p):
    '''param : LPAREN ID NUMBER RPAREN'''
    p[0] = (p[2], p[3])  # Parameter as a tuple

def p_error(p):
    if p:
        print(f"Syntax error at token: {p.type} ({p.value}) on line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Helper function to generate star lines
def generate_star_lines(cx, cy, radius, points=5):
    """Generates the lines for a star shape."""
    lines = []
    angle = 2 * pi / points
    vertices = [
        (cx + cos(i * angle) * radius, cy + sin(i * angle) * radius)
        for i in range(points * 2)
    ]
    for i in range(0, len(vertices), 2):  # Connect every other vertex
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 2) % len(vertices)]
        lines.append(Line(x1, y1, x2, y2))
    return lines

def interpret(ast):
    shapes = []
    for shape_type, params in ast:
        if shape_type in user_shapes:  # Handle user-defined shapes
            default_params, body = user_shapes[shape_type]
            # Merge default params with provided params
            merged_params = {**default_params, **params}
            for sub_shape in body:
                sub_type, sub_params = sub_shape
                eval_params = {
                    k: eval(str(v), {}, merged_params)  # Evaluate expressions
                    for k, v in sub_params.items()
                }
                shapes.extend(interpret([(sub_type, eval_params)]))
        elif shape_type == 'circle':
            shapes.append(Circle(params['x'], params['y'], params['radius']))
        elif shape_type == 'square':
            shapes.append(Square(params['x'], params['y'], params['side']))
        elif shape_type == 'line':
            shapes.append(Line(params['x1'], params['y1'], params['x2'], params['y2']))
        elif shape_type == 'star':  # Special case for predefined star
            shapes.extend(generate_star_lines(
                params['cx'], params['cy'], params['radius']
            ))
    return shapes
