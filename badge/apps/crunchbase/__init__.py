import sys
import os

sys.path.insert(0, "/system/apps/crunchbase")
os.chdir("/system/apps/crunchbase")

from badgeware import (
    Image,
    PixelFont,
    SpriteSheet,
    brushes,
    io,
    run,
    screen,
    shapes,
)

FRAME_COUNT = 24
BACKGROUND = brushes.color(6, 18, 34)
TEXT_COLOR = brushes.color(200, 234, 255)

logo_sheet = SpriteSheet("assets/crunchbase-spin.png", FRAME_COUNT, 1)
logo_animation = logo_sheet.animation()

screen.font = PixelFont.load("/system/assets/fonts/absolute.ppf")
screen.antialias = Image.X2


def draw_background():
    screen.brush = BACKGROUND
    screen.draw(shapes.rectangle(0, 0, screen.width, screen.height))


def draw_logo():
    # io.ticks increases with time; dividing controls spin speed
    frame_time = io.ticks / 110
    frame = logo_animation.frame(frame_time)
    x = (screen.width - frame.width) // 2
    y = (screen.height - frame.height) // 2 - 6
    screen.blit(frame, x, y)


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
