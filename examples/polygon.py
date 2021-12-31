#!/usr/bin/env python3
"""Examples of various ways to draw a polygon."""
import math

from src.SimpleSurface import SimpleSurface

# Create the SimpleSurface object and set the background to white
surface = SimpleSurface(600, 800)
surface.set_background()

font = "examples/fonts/arial.ttf"
font_size = 16

# Write a title
title_width, title_height = surface.write(
    "polygon()", "center", "top", font=font, font_size=30, padding={"top": 10}
)

# Describe the ellipse function at the top
y = title_height + 10
_, text_height = surface.write(
    (
        "The polygon function connects an array of (x, y)-coordinates to draw any custom shape.\n\n"
        "Optional arguments include the fill colour, whether or not to fill it with colour, the outline width and the outline colour."
    ),
    "center",
    y,
    font,
    font_size=font_size,
    alignment="center",
    padding={"top": 10, "left": 10, "right": 10},
)
y += text_height + 10
surface.line("left", y + 10, "right", y + 10)

# Draw a black triangle
surface.polygon([(250, 260), (200, 350), (50, 200)])
surface.write(
    "polygon([(250, 260), (200, 350), (50, 200)])",
    20,
    360,
    font=font,
    font_size=font_size,
)

# Draw a filled orange 5-pointed star with a black outline
radius = 100
angle = 72  # degrees
pentagram = []
origin = (surface.get_width() * 3 / 4, surface.get_height() * 1 / 3)
for i in range(0, 5 * 2, 2):
    x = origin[0] + radius * math.cos(math.radians(-90 + (i % 5) * angle))
    y = origin[1] + radius * math.sin(math.radians(-90 + (i % 5) * angle))
    pentagram.append((x, y))

surface.polygon(points=pentagram, fill_color=(255, 165, 0), line_color=(0, 0, 0))
surface.write(
    "[check file for code lol]",
    375,
    360,
    font=font,
    font_size=font_size,
    )

# Draw a green pentagon with a red outline that is 10 pixels thick
radius = 100
angle = 72  # degrees
pentagon = []
origin = (surface.get_width() * 1 / 4, surface.get_height() * 2 / 3)
for i in range(5):
    x = origin[0] + radius * math.cos(math.radians(-90 + i * angle))
    y = origin[1] + radius * math.sin(math.radians(-90 + i * angle))
    pentagon.append((x, y))

surface.polygon(points=pentagon, fill_color=(0, 255, 0), line_width=10, line_color=(255, 0, 0))
surface.write(
    f"polygon(\npoints={[(int(x), int(y)) for x, y in pentagon]},\nfill_color=(0, 255, 0),\nline_width=10,\nline_color=(255, 0, 0)\n)",
    20,
    640,
    font=font,
    font_size=font_size,
    max_width=surface.get_width()/2,
)

# Draw an empty blue quadrilateral that touches all four sides of the
# bottom-right quadrant
quadrilateral = [("center", 450), (500, "center"), ("right", 600), (400, "bottom")]
surface.polygon(points=quadrilateral, fill=False, line_color=(0, 0, 255))
surface.write(
    'polygon(\npoints=[\n("center", 450), (500, "center"),\n("right", 600), (400, "bottom")],\nfill=False,\nline_color=(0, 0, 255)\n)',
    surface.get_width()/2 + 70,
    surface.get_height()/2 + 130,
    font=font,
    font_size=font_size,
    max_width=surface.get_width()/2,
)

# Write our drawing to a PNG file
surface.write_to_png("example_polygon.png")
