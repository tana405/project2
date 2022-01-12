import movement
import window
import time
import pygame
import final


def main():
    movement.pygame.mixer.music.play(-1)
    level, start = window.start_window()
    finihs = time.monotonic() - start
    print("{:>.3f}".format(finihs))
    movement.terminate()


main()
