import sys
import os
import math

sys.path.insert(0, "/system/apps/crunchbase")
os.chdir("/system/apps/crunchbase")

from badgeware import (
    Image,
    Matrix,
    PixelFont,
    brushes,
    io,
    run,
    screen,
    shapes,
)

BACKGROUND = brushes.color(6, 18, 34)
TILE_COLOR = brushes.color(10, 42, 76)
TILE_GLOW = brushes.color(32, 110, 173, 140)
TEXT_COLOR = brushes.color(200, 234, 255)
ICON_ALPHA_ACTIVE = 255
ICON_SCALE = 4.5
SPIN_SPEED = 140

icon_image = Image.load("assets/cbuddy.png")
squircle = shapes.squircle(-28, -28, 56, 6)

screen_font = PixelFont.load("/system/assets/fonts/absolute.ppf")

screen.font = screen_font
screen.antialias = Image.X2


def draw_background():
    screen.brush = BACKGROUND
    screen.draw(shapes.rectangle(0, 0, screen.width, screen.height))


def draw_logo():
    # Create a spin similar to the menu icon flip animation
    phase = io.ticks / SPIN_SPEED
    width_raw = round(math.cos(phase) * 5) / 5
    if width_raw >= 0:
        width_factor = max(0.14, width_raw)
    else:
        width_factor = min(-0.14, width_raw)

    sprite_width = icon_image.width * ICON_SCALE * width_factor
    sprite_height = icon_image.height * ICON_SCALE
    sprite_offset = abs(sprite_width) / 2

    centre_x = 80
    centre_y = 58

    # subtle glow behind the icon
    squircle.transform = Matrix().translate(centre_x, centre_y).scale(1.35, 1.35)
    screen.brush = TILE_GLOW
    screen.draw(squircle)

    squircle.transform = Matrix().translate(centre_x, centre_y)
    screen.brush = TILE_COLOR
    screen.draw(squircle)

    icon_image.alpha = ICON_ALPHA_ACTIVE

    screen.scale_blit(
        icon_image,
        centre_x - sprite_offset,
        centre_y - sprite_height / 2,
        sprite_width,
        sprite_height,
    )


def draw_caption():
    screen.brush = TEXT_COLOR
    label = "crunchbase"
    width, height = screen.measure_text(label)
    screen.text(label, 80 - (width / 2), screen.height - height - 6)


def update():
    draw_background()
    draw_logo()
    draw_caption()
    return None


if __name__ == "__main__":
    run(update)
