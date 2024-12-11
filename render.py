from PIL import Image, ImageDraw

def render_canvas(shapes, width=500, height=500, filename="output.png"):
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    for shape in shapes:
        print("render", shape, shape.color, shape.fill)
        shape.render(draw)

    image.save(filename)
    print(f"Canvas saved as {filename}")

def render_animation(frames, width=500, height=500, prefix="frame"):
    for idx, frame_shapes in enumerate(frames):
        filename = f"{prefix}_{idx:03}.png"
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)

        for shape in frame_shapes:
            shape.render(draw)  # Use shape objects directly

        image.save(filename)
        print(f"Frame {idx} saved as {filename}")
