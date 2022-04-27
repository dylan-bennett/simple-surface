#!/usr/bin/env python3
"""Examples of various ways to draw an rounded_rectangle."""
from SimpleSurface import SimpleSurface

# Create the SimpleSurface object and set the background to yellow
surface = SimpleSurface(600, 800)
surface.set_background()

font = "examples/fonts/arial.ttf"
font_size = 16

# Write a title
title_width, title_height = surface.write(
    "write()", "center", "top", font=font, font_size=30, padding={"top": 10}
)

# Describe the rounded_rectangle function at the top
y = title_height + 10
_, text_height = surface.write(
    (
        "The write function provides a lot of functionality, trying to make it "
        "as easy to write text to a SimpleSurface as possible."
    ),
    "center",
    y,
    font,
    font_size=font_size,
    alignment="center",
    padding={"top": 10, "left": 10, "right": 10},
)

y += text_height
_, text_height = surface.write(
    (
        "The default arguments include the text to be written, the top-left "
        "(x, y)-coordinates of the text's bounding box, and a path to the font "
        "file. Calling the write function with only these parameters will "
        "produce text that fills up the given SimpleSurface as much as "
        "possible (as can be seen in the first example)."
    ),
    "center",
    y,
    font,
    font_size=font_size,
    alignment="center",
    padding={"top": 10, "left": 10, "right": 10},
)

y += text_height
_, text_height = surface.write(
    "The optional arguments are:",
    "center",
    y,
    font,
    font_size=font_size,
    alignment="center",
    padding={"top": 30, "left": 10, "right": 10},
)

y += text_height
_, text_height = surface.write(
    (
        '- alignment (str) -- the alignment of the text. Can be "left", '
        '"center", "right", or "justified" (default "left").\n'
        "- break_lines (bool) -- whether to break text up into multiple lines "
        "if it's too long (default True).\n"
        "- color (3- or 4-tuple) -- the color of the text as an RGB(A) tuple "
        "(default (0, 0, 0) (black)).\n"
        '- font_size (int/str) -- the font size, in pts. If set to "fill", it '
        'will be the largest font size it can be (default "fill").\n'
        "- justify_last_line (bool) -- whether to justify the last line of "
        "text, if the text is justified. If set to False, the last line will "
        "be left-aligned (default False).\n"
        "- line_spacing (float) -- the line spacing multiplier (default 1.0).\n"
        "- max_height (int) -- the maximum vertical space the text and padding "
        'will take up. If set to "fill", it will be the largest height '
        'needed/allowed (default "fill").\n'
        "- max_width (int) -- the maximum horizontal space the text and "
        'padding will take up. If set to "fill", it will be the largest width '
        'needed/allowed (default "fill").\n'
        "- min_font_size (int) -- the minimum font size, in pts (default 7).\n"
        "- outline_width (int) -- the text outline width, in pixels "
        "(default 0).\n"
        "- outline_color (3- or 4-tuple) -- the color of the text outline as "
        "an RGB(A) tuple (default (0, 0, 0) (black)).\n"
        "- padding (dict) -- the padding around the text, in pixels. Any or "
        "all of the padding keys can be sent in. "
        '(default {"top":0, "right":0, "bottom":0, "left":0}).'
    ),
    "center",
    y,
    font,
    font_size=font_size,
    alignment="left",
    padding={"top": 10, "left": 10, "right": 10},
    line_spacing=1.1,
)

y += text_height
_, text_height = surface.write(
    (
        "You can see examples of text with these arguments in the following "
        "examples."
    ),
    "center",
    y,
    font,
    font_size=font_size,
    alignment="center",
    padding={"top": 10, "left": 10, "right": 10},
)

# Write our drawing to a PNG file
surface.write_to_png("example_write_0.png")
