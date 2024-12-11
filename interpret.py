import ply.lex as lex
import ply.yacc as yacc
from primitive import Square, Circle, Line, Shape
# from manim import Scene, Circle, Square, Lipipne

start = 'sexpr_list'

# Token definitions
tokens = (
    'LPAREN', 'RPAREN', 'ID', 'NUMBER', 'STRING', 'BOOLEAN', 'DEFINE'
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_DEFINE = r'define'

# String token
def t_STRING(t):
    r'\"[^"]*\"'
    t.value = t.value.strip('"')  # Remove quotes
    return t

# Boolean token
def t_BOOLEAN(t):
    r'true|false'
    t.value = t.value == 'true'  # Convert to Python boolean
    print(f"Parsed BOOLEAN: {t.value}")  # Debugging line
    return t


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

lexer = lex.lex()

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
    if isinstance(p[1], tuple):
        p[0] = p[1]
    else:
        p[0] = (p[2], dict(p[3]))

def p_define_expr(p):
    '''define_expr : LPAREN DEFINE ID param_list LPAREN sexpr_list RPAREN RPAREN'''
    shape_name = p[3]
    params = dict(p[4])
    body = p[6]
    user_shapes[shape_name] = (params, body)
    p[0] = None

def p_param_list(p):
    '''param_list : param
                  | param_list param'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_param(p):
    '''param : LPAREN ID NUMBER RPAREN
             | LPAREN ID STRING RPAREN
             | LPAREN ID BOOLEAN RPAREN'''
    p[0] = (p[2], p[3])  # Pair (key, value)


def p_error(p):
    if p:
        print(f"Syntax error at token: {p.type} ({p.value}) on line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

def interpret(ast):
    shapes = []
    for shape_type, params in ast:
        print(f"Interpreting shape: {shape_type}, params: {params}")  # Debugging line
        color = params.get("color", "black")
        fill = params.get("fill", False)  # Should already be a boolean
        if shape_type == "circle":
            shapes.append(Circle(params["x"], params["y"], params["radius"], color, fill))
        elif shape_type == "square":
            shapes.append(Square(params["x"], params["y"], params["side"], color, fill))
        elif shape_type == "line":
            shapes.append(Line(params["x1"], params["y1"], params["x2"], params["y2"], color))
        else:
            print(f"Unsupported shape type: {shape_type}")
    return shapes

