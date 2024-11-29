# interpret.py
from primitive import Circle, Square, Line
from render import render_canvas

user_functions = {}

def interpret(dsl_code):
    shapes = []
    lines = dsl_code.strip().split("\n")
    print(lines)
    for line in lines:
        tokens = line.split()
        print(tokens)
        
        if tokens[0] == "function":
            function_name = tokens[1]
            parameters = tokens[2].strip("()").split(",")
            body = []
            for l in lines[lines.index(line) + 1:]:
                if l.strip() == "end":
                    break
                body.append(l.strip())
            user_functions[function_name] = (parameters, body)
        
        elif tokens[0] in user_functions:
            function_name = tokens[0]
            args = tokens[1].strip("()").split(",")
            args = [arg.strip() for arg in args]  # Clean up whitespace
            print(f"Executing function {function_name} with args {args}")
            execute_function(function_name, args, shapes)

        elif tokens[0] == "circle":
            x = int(tokens[1].split("=")[1])
            y = int(tokens[2].split("=")[1])
            radius = int(tokens[3].split("=")[1])
            shapes.append(Circle(x, y, radius))
        elif tokens[0] == "square":
            print("Parsing square:", tokens)
            x = int(tokens[1].split("=")[1])
            y = int(tokens[2].split("=")[1])
            side = int(tokens[3].split("=")[1])
            square = Square(x, y, side)
            print("Created square:", square)
            shapes.append(square)
    print("Shapes to render:", shapes)
    render_canvas(shapes)

def execute_function(function_name, args, shapes):
    params, body = user_functions[function_name]
    param_map = {param.strip(): int(arg.strip()) for param, arg in zip(params, args)}
    print(f"Parameter map: {param_map}")
    
    for line in body:
        tokens = line.split()
        print(f"Evaluating: x1={tokens[1].split('=')[1]}, param_map={param_map}")
        if tokens[0] == "circle":
            x = eval(tokens[1].split("=")[1], {}, param_map)
            y = eval(tokens[2].split("=")[1], {}, param_map)
            radius = eval(tokens[3].split("=")[1], {}, param_map)
            shapes.append(Circle(x, y, radius))
        if tokens[0] == "line":
            x1 = eval(tokens[1].split("=")[1], {}, param_map)
            y1 = eval(tokens[2].split("=")[1], {}, param_map)
            x2 = eval(tokens[3].split("=")[1], {}, param_map)
            y2 = eval(tokens[4].split("=")[1], {}, param_map)
            print(f"Creating line with: ({x1}, {y1}) to ({x2}, {y2})")
            shapes.append(Line(x1, y1, x2, y2))

