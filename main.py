from interpret import interpret
from primitive import Line
from render import render_canvas

# Example DSL script
# circle x=100 y=150 radius=50
# square x=200 y=250 side=100
# circle x=400 y=400 radius=10
# square x=400 y=400 side=10
dsl_code = """
function star(x, y, radius)
    line x1=x-radius y1=y x2=x y2=y+radius
    line x1=x y1=y+radius x2=x+radius y2=y
    line x1=x+radius y1=y x2=x-radius/2 y2=y-radius/2
    line x1=x-radius/2 y1=y-radius/2 x2=x+radius/2 y2=y-radius/2
    line x1=x+radius/2 y1=y-radius/2 x2=x-radius y2=y
end
star(250, 250, 100)
"""
interpret(dsl_code)
# shapes = [
#     Line(150, 250, 250, 350),
#     Line(250, 350, 350, 250),
#     Line(350, 250, 200, 150),
#     Line(200, 150, 300, 150),
#     Line(300, 150, 150, 250)
# ]
# render_canvas(shapes)
