#!/usr/bin/env python3
"""Examples of various ways to draw a line."""
import cairo

from src.ImageSurfacePlus import ImageSurfacePlus

# Create the ImageSurfacePlus object and set the background to white
surface = ImageSurfacePlus(600, 800)
surface.set_background()

# Draw a black line from (50, 250) to (200, 50)
surface.draw.line(50, 250, 200, 50)

# Draw a blue line 10 pixels thick from (350, 350) to (500, 100)
surface.draw.line(350, 350, 500, 100, color=(0, 0, 255), line_width=10)

# Draw a red line 20 pixels thick from (50, 500) to (250, 700) with a rounded
# line cap.
surface.draw.line(50, 500, 250, 700, line_cap=cairo.LINE_CAP_ROUND, color=(255, 0, 0), line_width=20)

# Draw an X in the bottom-right quadrant
surface.draw.line("center", "center", "right", "bottom")
surface.draw.line("center", "bottom", "right", "center")

# Draw gridlines for reference (outline + vertical/horizontal center lines)
surface.gridlines()

# Write our drawing to a PNG file
surface.write_to_png("example_line.png")
