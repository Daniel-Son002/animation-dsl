# interpret.py
from primitive import Circle, Square, Line
from render import render_canvas

user_functions = {}  # Dictionary to store user-defined functions

def interpret(dsl_code):
    shapes = []
    lines = dsl_code.strip().split("\\n")
    for line in lines:
        tokens = line.split()
        
        # Function definition
        if tokens[0] == "function":
            function_name = tokens[1]
            parameters = tokens[2].strip("()").split(",")
            body = []
            for l in lines[lines.index(line) + 1:]:
                if l.strip() == "end":  # End of function
                    break
                body.append(l.strip())
            user_functions[function_name] = (parameters, body)
        
        # Function invocation
        elif tokens[0] in user_functions:
            function_name = tokens[0]
            args = tokens[1].strip("()").split(",")
            execute_function(function_name, args, shapes)

        # Shape primitives
        elif tokens[0] == "circle":
            x = int(tokens[1].split("=")[1])
            y = int(tokens[2].split("=")[1])
            radius = int(tokens[3].split("=")[1])
            shapes.append(Circle(x, y, radius))
        elif tokens[0] == "square":
            x = int(tokens[1].split("=")[1])
            y = int(tokens[2].split("=")[1])
            side = int(tokens[3].split("=")[1])
            shapes.append(Square(x, y, side))
    
    render_canvas(shapes)

def execute_function(function_name, args, shapes):
    params, body = user_functions[function_name]
    param_map = {param: int(arg) for param, arg in zip(params, args)}
    
    for line in body:
        tokens = line.split()
        if tokens[0] == "circle":
            x = eval(tokens[1].split("=")[1], {}, param_map)
            y = eval(tokens[2].split("=")[1], {}, param_map)
            radius = eval(tokens[3].split("=")[1], {}, param_map)
            shapes.append(Circle(x, y, radius))
        elif tokens[0] == "line":
            x1 = eval(tokens[1].split("=")[1], {}, param_map)
            y1 = eval(tokens[2].split("=")[1], {}, param_map)
            x2 = eval(tokens[3].split("=")[1], {}, param_map)
            y2 = eval(tokens[4].split("=")[1], {}, param_map)
            shapes.append(Line(x1, y1, x2, y2))
