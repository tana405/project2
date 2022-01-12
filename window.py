import movement
import pygame
import time
import sys

pygame.init()
size = width, height = 805, 500
screen = pygame.display.set_mode(size)
fon = pygame.image.load('data/fon.png')
screen.blit(fon, (0, 0))
pygame.display.set_caption('')
clock = pygame.time.Clock()


class Button():
    def __init__(self, name, x, y):
        font = pygame.font.Font(None, 30)
        self.x = x
        self.y = y
        self.text = font.render(name, True, (0, 0, 0))
        self.text_w = self.text.get_width()
        self.text_h = self.text.get_height()
        pygame.draw.rect(screen, (130, 150, 40), (x, y,
                                                  self.text_w + 20, self.text_h + 20), 0)
        screen.blit(self.text, (x + 10, y + 10))

    def update(self, k):
        if self.x <= k[0] <= self.x + self.text_w and self.y <= k[1] <= self.y + self.text_h:
            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y,
                                                 self.text_w + 20, self.text_h + 20), 2)
            return True
        else:
            pygame.draw.rect(screen, (130, 150, 40), (self.x, self.y,
                                                      self.text_w + 20, self.text_h + 20), 2)
            return False


def start_window():
    global size
    screen = pygame.display.set_mode(size)
    text = pygame.transform.scale(movement.load_image('текст.png'), (600, 170))
    screen.blit(fon, (0, 0))
    screen.blit(text, (190, 100))
    font = pygame.font.Font(None, 50)
    text = font.render('Поиск Норта', True, (0, 0, 0))
    screen.blit(text, (275, 30))
    a = Button('ИГРАТЬ', 30, 125)
    b = Button('Инструкция', 30, 200)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(4)
                running = False
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                a.update(event.pos)
                b.update(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if a.update(event.pos):
                    start = time.monotonic()
                    return movement.level_1(), start
                elif b.update(event.pos):
                    manual()
                    return start_window()

        pygame.display.flip()
        clock.tick(50)


def manual():
    global size
    screen = pygame.display.set_mode(size)
    inst = pygame.transform.scale(movement.load_image('инструкция.png'), (780, 477))
    screen.fill((139, 69, 19))
    screen.blit(inst, (17, 11))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
