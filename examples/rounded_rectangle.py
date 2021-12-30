#!/usr/bin/env python3
"""Examples of various ways to draw a rounded rectangle."""
from src.SimpleSurface import SimpleSurface

# Create the SimpleSurface object and set the background to yellow
surface = SimpleSurface(600, 800)
surface.set_background((255, 255, 0))

# Draw a black rounded rectangle at (50, 50), measuring 100x200 pixels with a
# 10-pixel radius on its corners
surface.rounded_rectangle(50, 50, 100, 200, 10)

# Draw a blue rounded rectangle at ("left", 650), measuring 200x100 pixels with
# a 20-pixel radius on its corners
surface.rounded_rectangle("left", 650, width=200, height=100, radius=20, color=(0, 0, 255))

# Draw an empty rounded rectangle at (200, "top"), measuring 200x250 pixels
# with a 100-pixel radius on its corners
surface.rounded_rectangle(200, "top", 200, 250, 100, fill=False)

# Draw a pink rounded rectangle at ("right", "bottom") that fills in the entire
# bottom-right quadrant with a purple outline that is 20 pixels thick
surface.rounded_rectangle(
    x="right",
    y="bottom",
    width=surface.get_width() / 2,
    height=surface.get_height() / 2,
    radius=min(surface.get_width() / 5, surface.get_height() / 5),
    color=(255, 192, 203),
    outline=20,
    outline_color=(128, 0, 128),
)

# Draw a transparent lime-green rounded rectangle at ("center", "center")
# measuring 250x250 pixels, with a red outline and a 15-pixel radius on its
# corners
surface.rounded_rectangle(
    "center", "center", 250, 250, 15, color=(50, 205, 50, 128), outline_color=(255, 0, 0)
)

# Draw gridlines for reference (outline + vertical/horizontal center lines)
surface.gridlines()

# Write our drawing to a PNG file
surface.write_to_png("example_rounded_rectangle.png")
