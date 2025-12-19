from PIL import Image


def load_image(filename: str) -> Image.Image:
    """
    Load an input PNG image.
    """
    return Image.open(filename)


def compute_next_coordinate(x: int, y: int, width: int, height: int):
    """
    Compute the next coordinate in a hexagonal grid.
    This is a placeholder and will be completed later.
    """
    return -1, -1


def sample_color(coord, image: Image.Image):
    """
    Sample the average color around a hexagon center.
    Placeholder implementation.
    """
    return (0, 0, 0)


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
