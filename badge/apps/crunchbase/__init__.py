import sys
import os

sys.path.insert(0, "/system/apps/crunchbase")
os.chdir("/system/apps/crunchbase")

from badgeware import screen, brushes, shapes, io, run, SpriteSheet, PixelFont

BACKGROUND = brushes.color(4, 12, 26)
FOREGROUND = brushes.color(255, 255, 255)

logo_sheet = SpriteSheet("assets/crunchbase-rot.png", 6, 4)
logo_animation = logo_sheet.animation()
font = PixelFont.load("/system/assets/fonts/absolute.ppf")
screen.font = font


def draw_background():
    screen.brush = BACKGROUND
    screen.draw(shapes.rectangle(0, 0, screen.width, screen.height))


def update():
    draw_background()

    frame_time = io.ticks / 120
    frame = logo_animation.frame(frame_time)

    x = (screen.width - frame.width) / 2
    y = (screen.height - frame.height) / 2 - 6
    screen.blit(frame, int(x), int(y))

    screen.brush = FOREGROUND
    label = "Crunchbase"
    width, height = screen.measure_text(label)
    screen.text(label, 80 - (width / 2), screen.height - height - 6)

    return None


if __name__ == "__main__":
    run(update)
