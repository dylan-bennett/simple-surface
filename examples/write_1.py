#!/usr/bin/env python3
"""Example of text written with the default parameters."""
from src.SimpleSurface import SimpleSurface

# Create the SimpleSurface object and set the background to white
surface = SimpleSurface(600, 800)
surface.set_background()

# Write text with default parameters
surface.write(
    (
        "This is one text block written with the default parameters.\n\n"
        "Line breaks are supported and\n"
        "give\n"
        "more\n"
        "control\n"
        "over how the text looks.\n\n"
        "With the font size not specified, the text will fill as much of "
        "the area as it's allowed to (in this case, the entire page)."
    ),
    0,
    0,
    "examples/fonts/arial.ttf",
)

# Write our drawing to a PNG file
surface.write_to_png("example_write_1.png")
