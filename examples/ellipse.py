#!/usr/bin/env python3
"""Examples of various ways to draw an ellipse."""
from src.SimpleSurface import SimpleSurface

# Create the SimpleSurface object and set the background to yellow
surface = SimpleSurface(600, 800)
surface.set_background()

font = "examples/fonts/arial.ttf"
font_size = 16

# Write a title
title_width, title_height = surface.write(
    "ellipse()", "center", "top", font=font, font_size=30, padding={"top": 10}
)

# Describe the ellipse function at the top
y = title_height + 10
_, text_height = surface.write(
    (
        "The ellipse function draws an ellipse of any size, originating at the top-left corner.\n\n"
        "Optional arguments include the colour, whether or not to fill it "
        "with colour, the outline thickness, and the outline colour.\n\n"
        "The width and height of the ellipse take into account the thickness of the "
        "outline, so the resulting shape's size will always be the values "
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

# Draw a black ellipse measuring 50x100 pixels
y += 50
surface.ellipse(50, y, 50, 100)
surface.write(
    f"ellipse(50, {y}, 50, 100)",
    50,
    y - (font_size + 5),
    font=font,
    font_size=font_size,
)

# Draw a transparent lime-green ellipse at ("center", "center") measuring
# 250x250 pixels and with a red outline
surface.write(
    'ellipse("center", "center", 250, 250,\nfill_color=(50, 205, 50, 128), line_color=(255, 0, 0))\n(The RGBA fill_color makes this one see-through!)',
    "center",
    "center",
    font=font,
    max_width=surface.get_width() * 0.75,
    alignment="center",
    font_size=font_size,
)
surface.ellipse("center", "center", 250, 250, fill_color=(50, 205, 50, 128), line_color=(255, 0, 0))

# Draw an empty ellipse measuring 200x250 pixels with an outline 20 pixels thick
surface.ellipse(450, 590, 120, 200, fill=False, line_width=20)
surface.write(
    "ellipse(450, 590, 120, 200, fill=False, line_width=20)", "right", 570, font=font, font_size=font_size, padding={"right": 10},
)

# Draw a pink ellipse at ("left", "bottom") that fills in the entire
# bottom-right quadrant with a purple outline that is 20 pixels thick
surface.ellipse(
    x="left",
    y="bottom",
    width=surface.get_width() / 4,
    height=surface.get_height() / 4,
    fill_color=(255, 192, 203),
    line_width=10,
    line_color=(128, 0, 128),
)
a, b = surface.write(
    'ellipse(\nx="left",\ny="bottom",\nwidth=surface.get_width() / 4,\nheight=surface.get_height() / 4,\nfill_color=(255, 192, 203),\nline_width=10,\nline_color=(128, 0, 128),\n)',
    surface.get_width() / 4 + 20,
    "bottom",
    font=font,
    font_size=font_size,
)

# Write our drawing to a PNG file
surface.write_to_png("example_ellipse.png")