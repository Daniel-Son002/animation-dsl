import ply.lex as lex
import ply.yacc as yacc
from primitive import Circle, Square, Line

start = 'sexpr_list'

# Token definitions
tokens = (
    'LPAREN', 'RPAREN', 'ID', 'NUMBER'
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Number token
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convert the matched string to an integer
    return t

# Ignored characters
t_ignore = ' \t\n'

# Error handling for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Grammar rules
def p_sexpr_list(p):
    '''sexpr_list : sexpr
                  | sexpr_list sexpr'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_sexpr(p):
    '''sexpr : LPAREN ID param_list RPAREN'''
    p[0] = (p[2], dict(p[3]))

def p_param_list(p):
    '''param_list : param
                  | param_list param'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_param(p):
    '''param : LPAREN ID NUMBER RPAREN'''
    p[0] = (p[2], p[3])  # Convert the parameter into a tuple (name, value)

def p_error(p):
    if p:
        print(f"Syntax error at token: {p.type} ({p.value}) on line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

def interpret(ast):
    shapes = []
    for shape_type, params in ast:
        if shape_type == 'circle':
            shapes.append(Circle(params['x'], params['y'], params['radius']))
        elif shape_type == 'square':
            shapes.append(Square(params['x'], params['y'], params['side']))
        elif shape_type == 'line':
            shapes.append(Line(params['x1'], params['y1'], params['x2'], params['y2']))
    return shapes
