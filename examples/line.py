#!/usr/bin/env python3
"""Examples of various ways to draw a line."""
import cairo

from SimpleSurface import SimpleSurface

# Create the SimpleSurface object and set the background to white
surface = SimpleSurface(600, 800)
surface.set_background()

font = "examples/fonts/arial.ttf"
font_size = 16

# Write a title
title_width, title_height = surface.write(
    "line()", "center", "top", font=font, font_size=30, padding={"top": 10}
)

# Describe the ellipse function at the top
y = title_height + 10
_, text_height = surface.write(
    (
        "The line function draws, you guessed it, a line from (x1, y1) to "
        "(x2, y2).\n\n"
        "Optional arguments include the colour, the width, and the cap style."
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

# Draw a black line from (50, 250) to (200, 50)
y += 50
surface.line(50, y, 200, y + 100)
surface.write(
    f"line(50, {y}, 200, {y + 100})",
    40,
    y - (font_size + 5),
    font=font,
    font_size=font_size,
)

# Draw a blue line 10 pixels thick from (350, 350) to (500, 100)
surface.line(350, y + 100, 500, y, line_color=(0, 0, 255), line_width=10)
surface.write(
    f"line(350, {y + 100}, 500, {y},\nline_color=(0, 0, 255), line_width=10)",
    300,
    y + 110,
    font=font,
    font_size=font_size,
)

# Draw a red line 20 pixels thick from (50, 500) to (250, 700) with a
# rounded line cap.
surface.line(
    50,
    400,
    250,
    550,
    line_cap=cairo.LINE_CAP_ROUND,
    line_color=(255, 0, 0),
    line_width=20,
)
surface.write(
    (
        "line(50, 400, 250, 550, line_cap=cairo.LINE_CAP_ROUND, "
        "line_color=(255, 0, 0), line_width=20)"
    ),
    10,
    320,
    font=font,
    font_size=font_size,
    max_width=surface.get_width() / 2,
)

# Draw an X in the bottom-right quadrant
surface.line("center", "center", "right", "bottom")
surface.line("center", "bottom", "right", "center")
surface.rectangle(
    surface.get_width() / 2,
    surface.get_height() / 2,
    surface.get_width() / 2,
    surface.get_height() / 2,
    fill=False,
)
surface.write(
    (
        'line("center", "center", "right", "bottom")\n'
        'line("center", "bottom", "right", "center")\n'
        "rectangle(\nsurface.get_width() / 2,\nsurface.get_height() / 2,\n"
        "surface.get_width() / 2,\nsurface.get_height() / 2,\nfill=False\n)"
    ),
    "left",
    "bottom",
    font=font,
    # font_size=font_size-2,
    max_width=surface.get_width() / 2,
    max_height=surface.get_height() / 4,
    padding={"bottom": 10, "left": 10},
)

# Write our drawing to a PNG file
surface.write_to_png("example_line.png")
