from PIL import Image, ImageDraw

def render_canvas(shapes, width=500, height=500, filename="output.png"):
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    for shape in shapes:
        shape.render(draw)
    image.save(filename)