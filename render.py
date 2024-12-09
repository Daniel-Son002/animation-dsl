from PIL import Image, ImageDraw

def render_canvas(shapes, width=500, height=500, filename="output.png"):
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    for shape in shapes:
        shape.render(draw)

    image.save(filename)
    print(f"Canvas saved as {filename}")

def render_animation(frames, width=500, height=500, prefix="frame"):
    for idx, shapes in enumerate(frames):
        filename = f"{prefix}_{idx:03}.png"
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)
        
        for shape in shapes:
            shape.render(draw)
        
        image.save(filename)
        print(f"Frame {idx} saved as {filename}")
