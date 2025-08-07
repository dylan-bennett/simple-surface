#!/usr/bin/env python3
"""Example of text written with the default parameters."""
from SimpleSurface import SimpleSurface

# Create the SimpleSurface object and set the background to white
surface = SimpleSurface(600, 800)
surface.set_background()

# Write text with default parameters
surface.write(
    (
        "This page contains one block of text, written with the default "
        "parameters.\n\n"
        '\tBoth tabs ("\\t") and leading spaces are supported, and can be used '
        "to create an indented paragraph. One tab is the equivalent of four "
        "spaces.\n\n"
        'Line breaks ("\\n") with leading spaces or tabs can be combined to\n'
        "\t\t\t\t\t\t\t\t\t\tgive\n"
        "\t\t\t\t\t\t   more\n"
        "\t\t   control\n"
        "over how the text looks.\n\n"
        "With the font size not specified, the text will fill as much of "
        "the area as it's allowed to (in this case, the entire page)."
    ),
    0,
    0,
    "examples/fonts/arial.ttf",
)

# Write our drawing to a PNG file
surface.write_to_png("write_1.png")
