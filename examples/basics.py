#!/usr/bin/env python3
"""Examples of basic commands done using SimpleSurface."""
import math
import random

from SimpleSurface import SimpleSurface

font = "examples/fonts/arial.ttf"
font_size = 16

# Create a second SimpleSurface
surface = SimpleSurface(600, 800)
surface.set_background()

# Write a title
title_width, title_height = surface.write(
    "The Basics", "center", "top", font=font, font_size=30, padding={"top": 10}
)

# Describe the basics of SimpleSurface at the top
y = title_height + 10
_, text_height = surface.write(
    (
        "Welcome to SimpleSurface! This package is designed to enhance Pycairo"
        " by handling much of the extra work required for features not "
        "natively supported.\n\n"
        "In this example there are common tasks showcased, namely cropping "
        "and pasting a Surface, as well as additional functions like outlining "
        "a SimpleSurface, drawing gridlines, and retrieving metadata.\n\n"
        "Check out the other examples to see what else SimpleSurface has to "
        "offer!"
    ),
    "center",
    y,
    font,
    font_size=font_size,
    alignment="center",
    padding={"top": 10, "left": 10, "right": 10},
)
y += text_height + 10
surface.line("left", y, "right", y)
y += 10

# Create a SimpleSurface
surface2 = SimpleSurface(600, 800)

# Set the background colour
surface2.set_background((255, 255, 0))

# Cover the entire thing with text
surface2.write(
    (
        "This is text to fill the entire page and show off the crop function."
        "We're going to crop out the middle of this text and then paste it "
        "onto another SimpleSurface in various ways."
    ),
    0,
    0,
    font=font,
)


# Set up some cropping parameters
crop_width = 200
crop_height = 200

# Create a new cropped surface at a random position
crop_x = random.randrange(surface2.get_width() - crop_width)
crop_y = random.randrange(surface2.get_height() - crop_height)
cropped_surface = surface2.crop(crop_x, crop_y, crop_width, crop_height)

# Paste the cropped version with default parameters
surface.paste(cropped_surface, 50, y + font_size)

# Re-crop the surface to get a clean slate
cropped_surface = surface2.crop(crop_x, crop_y, crop_width, crop_height)

# Paste the cropped version scaled to a particular width and height
# (plus gridlines)
cropped_surface.gridlines()
surface.paste(cropped_surface, 20, 515, width=267, height=135)

# Re-crop the surface to get a clean slate
cropped_surface = surface2.crop(crop_x, crop_y, crop_width, crop_height)

# Paste the cropped version rotated 45 degrees (plus an outline)
cropped_surface.outline(color=(0, 0, 255), width=5)
surface.paste(cropped_surface, 450, 250, rotate=math.pi / 4)

# Re-crop the surface to get a clean slate
cropped_surface = surface2.crop(crop_x, crop_y, crop_width, crop_height)

# Paste the cropped version scaled by a factor of 0.5 and 1.5
surface.paste(
    cropped_surface, "right", "bottom", scaling="ratio", width=0.5, height=1.5
)

# Write out the width and height and format of this SimpleSurface
y = 660
surface.write(
    (
        f"Info about the cropped SimpleSurface\n"
        f"width={cropped_surface.get_width()}\n"
        f"height={cropped_surface.get_height()}\n"
        f"format={repr(cropped_surface.get_format())}"
    ),
    10,
    y,
    font,
    max_height=surface.get_height() - y,
    max_width=surface.get_width() - cropped_surface.get_width() * 0.5 - 10,
)

# Save to PNG
surface.write_to_png("basics.png")
