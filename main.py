from PIL import Image, ImageDraw
"""A quick project to brush up on PIL. Perhaps a FastAPI resume-builder project could come forth if I finish it."""


def create_print_page(page_size: tuple = (2550, 3295)) -> Image:
    """Creates the base for the black and white only image."""
    page = Image.new(mode="1", size=page_size, color=1)
    draw = ImageDraw.Draw(page)
    draw.line(xy=[(800, 0), (800, 3295)], width=6)
    return page


def create_styled_page(page_size: tuple = (2550, 3295)) -> Image:
    """Creates the base for the full color image. Defaults to RGB 200/200/200"""
    # TODO: Use classes to implement templates and generating both versions of the resume at once
    # Consider making the print-ready one a lower resolution
    page = Image.new(mode="RGB", size=page_size, color=(250, 250, 250))
    draw = ImageDraw.Draw(page)
    draw.rounded_rectangle(xy=[(-50, 0), (800, 3295)], radius=20, fill=(200, 200, 200), outline=0, width=3)
    return page


def render_image():
    create_styled_page().show()


def render_printable():
    create_print_page().show()


def main():
    render_image()
    render_printable()


if __name__ == '__main__':
    main()

