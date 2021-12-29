#!/usr/bin/env python3
"""Examples of various ways to draw a polygon."""
import math

from src.SimpleSurface import SimpleSurface

# Create the SimpleSurface object and set the background to white
surface = SimpleSurface(600, 800)
surface.set_background()

# Draw a black triangle
surface.draw.polygon([(250, 60), (200, 350), (50, 200)])

# Draw an empty blue quadrilateral that touches all four sides of the
# upper-right quadrant
quadrilateral = [("center", 50), (500, "center"), ("right", 200), (400, "top")]
surface.draw.polygon(points=quadrilateral, fill=False, color=(0, 0, 255))

# Draw a green pentagon with a red outline that is 10 pixels thick
radius = 100
angle = 72  # degrees
pentagon = []
origin = (surface.get_width() * 1 / 4, surface.get_height() * 3 / 4)
for i in range(5):
    x = origin[0] + radius * math.cos(math.radians(-90 + i * angle))
    y = origin[1] + radius * math.sin(math.radians(-90 + i * angle))
    pentagon.append((x, y))

surface.draw.polygon(points=pentagon, color=(0, 255, 0), outline=10, outline_color=(255, 0, 0))

# Draw a filled orange 5-pointed star with a black outline
pentagram = []
origin = (surface.get_width() * 3 / 4, surface.get_height() * 3 / 4)
for i in range(0, 5 * 2, 2):
    x = origin[0] + radius * math.cos(math.radians(-90 + (i % 5) * angle))
    y = origin[1] + radius * math.sin(math.radians(-90 + (i % 5) * angle))
    pentagram.append((x, y))

surface.draw.polygon(points=pentagram, color=(255, 165, 0), outline_color=(0, 0, 0))

# Draw gridlines for reference (outline + vertical/horizontal center lines)
surface.gridlines()

# Write our drawing to a PNG file
surface.write_to_png("example_polygon.png")
