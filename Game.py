import movement
import window
import time
import pygame
import final
import datetime as dt
from datetime import timedelta


def main():
    rez = False
    movement.pygame.mixer.music.play(-1)
    level, start = window.start_window()
    print(45)
    print(start, 44)
    finihs = dt.datetime.now() - start
    if window.finish_window(str(finihs)):
        return main()
    movement.terminate()


main()
