#!/usr/bin/env python3
"""Examples of various ways to draw a dot."""
from src.SimpleSurface import SimpleSurface

# Create the SimpleSurface object and set the background to white
surface = SimpleSurface(600, 800)
surface.set_background()

font = "examples/fonts/arial.ttf"
font_size = 16

# Write a title
title_width, title_height = surface.write(
    "dot()", "center", "top", font=font, font_size=30, padding={"top": 10}
)

# Describe the dot function at the top
y = title_height + 10
_, text_height = surface.write(
    (
        "The dot function draws a dot of any size, originating at the center. "
        "The default radius is 1 pixel (you know, like a dot).\n\n"
        "Optional arguments include the colour, whether or not to fill it "
        "with colour, the outline thickness, and the outline colour.\n\n"
        "The radius of the dot takes into account the thickness of the "
        "outline, so the resulting shape's radius will always be the value "
        "sent in."
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

# Draw a black dot
y += 50
surface.dot(50, y)
surface.write(
    f"dot(50, {y})",
    60,
    y - font_size / 2,
    font=font,
    font_size=font_size,
)

# Draw a blue dot with a radius of 20 pixels
y += 50
surface.dot(x="left", y=y, radius=20, color=(0, 0, 255))
surface.write(
    f'dot(x="left", y={y}, radius=20, color=(0, 0, 255))',
    60,
    y - font_size / 2,
    font=font,
    font_size=font_size,
)

# Draw a lime-green dot at ("center", "center") with a radius of 50 pixels
# and a red outline
surface.dot("center", "center", 50, color=(50, 205, 50), outline_color=(255, 0, 0))
surface.write(
    'dot("center", "center", 50, color=(50, 205, 50), outline_color=(255, 0, 0))',
    "center",
    surface.get_height() / 2 + 60,
    font=font,
    font_size=font_size,
)

# Draw an empty dot with a radius of 30 pixels
surface.dot(500, 540, 30, fill=False)
surface.write(
    "dot(500, 540, 30, fill=False)", 250, 540 - font_size / 2, font=font, font_size=font_size
)

# Draw a pink dot at ("right", "bottom") with a radius of 100 pixels and a
# purple outline that is 20 pixels thick
surface.dot(
    x="right",
    y="bottom",
    radius=100,
    color=(255, 192, 203),
    outline=20,
    outline_color=(128, 0, 128),
)
a, b = surface.write(
    'dot(\nx="right",\ny="bottom",\nradius=100,\ncolor=(255, 192, 203),\noutline=20,\noutline_color=(128, 0, 128),\n)',
    "center",
    "bottom",
    font=font,
    font_size=font_size,
)

# Write our drawing to a PNG file
surface.write_to_png("example_dot.png")
