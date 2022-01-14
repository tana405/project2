import movement
import window
import time
import pygame
import final
import datetime as dt
from datetime import timedelta


def main():
    movement.pygame.mixer.music.play(-1)
    level, start = window.start_window()
    print(start, 44)
    finihs = dt.datetime.now() - start
    window.finish_window(str(finihs))
    movement.terminate()


main()
