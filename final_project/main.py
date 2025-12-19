from PIL import Image

def compute_next_coordinate(x: int, y: int, width: int, height: int, step: int = 10):
    dx = step
    dy = int(step * math.sqrt(3) / 2)

    if x == 0 and y == 0:
        return dx // 2, dy // 2

    x_next = x + dx

    if x_next >= width:
        y_next = y + dy
        if y_next >= height:
            return -1, -1

        row_index = (y_next // dy)
        x_next = dx // 2 if row_index % 2 == 0 else dx
        return x_next, y_next

    return x_next, y


def sample_color(coord, image: Image.Image, radius: int = 5):
    x_center, y_center = coord
    pixels = image.load()

    r_total = g_total = b_total = count = 0

    for dx in range(-radius, radius + 1):
        for dy in range(-radius, radius + 1):
            x = x_center + dx
            y = y_center + dy
            if 0 <= x < image.width and 0 <= y < image.height:
                r, g, b = pixels[x, y][:3]
                r_total += r
                g_total += g
                b_total += b
                count += 1

    if count == 0:
        return (0, 0, 0)

    return (r_total // count, g_total // count, b_total // count)


def generate_hexagon(coord, color, size: int = 6):
    """
    Generate an SVG polygon representing a hexagon at coord with given RGB color.
    """
    x, y = coord
    r, g, b = color

    points = []
    for i in range(6):
        angle = math.pi / 3 * i
        px = x + size * math.cos(angle)
        py = y + size * math.sin(angle)
        points.append(f"{px:.2f},{py:.2f}")

    points_str = " ".join(points)
    color_str = f"rgb({r},{g},{b})"

    return f'<polygon points="{points_str}" fill="{color_str}" />'

def build_svg(image: Image.Image) -> str:
    """
    Build the SVG document from the input image.
    """
    width, height = image.size
    elements = []

    x, y = 0, 0

    while True:
        coord = compute_next_coordinate(x, y, width, height)
        if coord == (-1, -1):
            break

        color = sample_color(coord, image)
        hexagon = generate_hexagon(coord, color)
        elements.append(hexagon)

        x, y = coord

    svg_elements = "\n".join(elements)

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}">\n'
        f'{svg_elements}\n'
        f'</svg>'
    )
def save_svg(svg_content: str, filename: str = "output.svg"):
    """
    Write SVG content to a file.
    """
    with open(filename, "w") as f:
        f.write(svg_content)

if __name__ == "__main__":
    img = load_image("example.png")
    svg = build_svg(img)
    save_svg(svg)
