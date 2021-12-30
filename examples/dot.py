#!/usr/bin/env python3
"""Examples of various ways to draw a dot."""
from src.SimpleSurface import SimpleSurface

# Create the SimpleSurface object and set the background to white
surface = SimpleSurface(600, 800)
surface.set_background()

# Draw a black dot at (50, 50)
surface.dot(50, 50)

# Draw a blue dot at ("left", 150) with a radius of 20 pixels
surface.dot("left", 150, radius=20, color=(0, 0, 255))

# Draw a lime-green dot at ("center", "center") with a radius of 50 pixels
# and a red outline
surface.dot("center", "center", 50, color=(50, 205, 50), outline_color=(255, 0, 0))

# Draw an empty dot at (200, "top") with a radius of 10 pixels
surface.dot(200, "top", 10, fill=False)

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

# Draw gridlines for reference (outline + vertical/horizontal center lines)
surface.gridlines()

# Write our drawing to a PNG file
surface.write_to_png("example_dot.png")
