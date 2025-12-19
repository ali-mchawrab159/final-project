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


def generate_hexagon(coord, color):
    """
    Generate the SVG geometry for a hexagon.
    Placeholder implementation.
    """
    return ""


def build_svg(image: Image.Image) -> str:
    """
    Core algorithm as described in the course.
    """
    output = []

    x, y = 0, 0
    width, height = image.size

    while True:
        coord = compute_next_coordinate(x, y, width, height)
        if coord == (-1, -1):
            break

        rgb = sample_color(coord, image)
        geometry = generate_hexagon(coord, rgb)
        output.append(geometry)

        x, y = coord

    return "\n".join(output)
