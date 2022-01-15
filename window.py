import movement
import pygame
import time
import sys
import os
import datetime as dt


pygame.init()
size = width, height = 805, 500
screen = pygame.display.set_mode(size)
programIcon = pygame.image.load('data/icon.png')
pygame.display.set_icon(programIcon)
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
        pygame.draw.rect(screen, (130, 150, 40), (self.x, self.y,
                                                  self.text_w + 20, self.text_h + 20), 0)
        screen.blit(self.text, (self.x + 10, self.y + 10))

    def update(self, k):
        pygame.draw.rect(screen, (130, 150, 40), (self.x, self.y,
                                                  self.text_w + 20, self.text_h + 20), 0)
        screen.blit(self.text, (self.x + 10, self.y + 10))
        if self.x <= k[0] <= self.x + self.text_w and self.y <= k[1] <= self.y + self.text_h:
            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y,
                                                 self.text_w + 20, self.text_h + 20), 2)
            return True
        else:
            pygame.draw.rect(screen, (130, 150, 40), (self.x, self.y,
                                                      self.text_w + 20, self.text_h + 20), 2)
            return False

    def draw(self, q):
        pygame.draw.rect(screen, (130, 150, 40), (self.x, self.y,
                                                  self.text_w + 20, self.text_h + 20), 0)
        screen.blit(self.text, (self.x + 10, self.y + 10))
        if q:
            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y,
                                                 self.text_w + 20, self.text_h + 20), 2)
        else:
            pygame.draw.rect(screen, (130, 150, 40), (self.x, self.y,
                                                      self.text_w + 20, self.text_h + 20), 2)

    def time(self):
        pygame.draw.rect(screen, (130, 150, 40), (self.x, self.y,
                                                  self.text_w + 20, self.text_h + 20), 0)
        screen.blit(self.text, (self.x + 10, self.y + 10))


class Meeting(pygame.sprite.Sprite):
    def __init__(self, x, y, x1, y1):

        dog = [pygame.image.load(os.path.join('data', 'щенок1.png')).convert_alpha(),
               pygame.image.load(os.path.join('data', 'щенок2.png')).convert_alpha(),
               pygame.image.load(os.path.join('data', 'щенок3.png')).convert_alpha(),
               pygame.image.load(os.path.join('data', 'щенок4.png')).convert_alpha()]
        girl = [pygame.image.load(os.path.join('data', '0.png')).convert_alpha(),
                pygame.image.load(os.path.join('data', '1.png')).convert_alpha(),
                pygame.image.load(os.path.join('data', '2.png')).convert_alpha(),
                pygame.image.load(os.path.join('data', '3.png')).convert_alpha(),
                pygame.image.load(os.path.join('data', '4.png')).convert_alpha(),
                pygame.image.load(os.path.join('data', '5.png')).convert_alpha(),
                pygame.image.load(os.path.join('data', '6.png')).convert_alpha(),
                pygame.image.load(os.path.join('data', '7.png')).convert_alpha(),
                pygame.image.load(os.path.join('data', '8.png')).convert_alpha()]
        self.stop1 = pygame.image.load(os.path.join('data', 'щенок1.png')).convert_alpha()
        self.stop2 = pygame.image.load(os.path.join('data', '111.png')).convert_alpha()
        self.frames = []
        self.frames1 = []
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        for i in dog:
            self.frames.append(i)
        for i in girl:
            self.frames1.append(i)

        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect().move(self.x, self.y)
        self.counter = 0

        self.cur_frame1 = 0
        self.image1 = self.frames1[self.cur_frame]
        self.rect1 = self.image.get_rect().move(self.x, self.y)
        self.counter1 = 0

    def update1(self, a):
        if self.x >= 410:
            if self.counter == a:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
                self.counter = 0
            else:
                self.counter += 1
            self.rect = self.image.get_rect().move(self.x, self.y)
            self.x -= 2
        else:
            self.image = self.stop1
        screen.blit(self.image, (self.x, self.y))

    def update2(self, a):
        if self.x1 <= 375:
            if self.counter1 == a:
                self.cur_frame1 = (self.cur_frame1 + 1) % len(self.frames1)
                self.image1 = self.frames1[self.cur_frame1]
                self.counter1 = 0
            else:
                self.counter1 += 1
            self.rect1 = self.image1.get_rect().move(self.x1, self.y1)
            self.x1 += 2
        else:
            self.image1 = self.stop2
        screen.blit(self.image1, (self.x1, self.y1))


def start_window():
    global size
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Поиск Норта')
    text_1 = pygame.transform.scale(movement.load_image('текст.png'), (600, 170))
    screen.blit(fon, (0, 0))
    screen.blit(text_1, (190, 100))
    font = pygame.font.Font(None, 50)
    text = font.render('Поиск Норта', True, (0, 0, 0))
    screen.blit(text, (275, 30))
    a = Button('ИГРАТЬ', 30, 125)
    b = Button('Инструкция', 30, 200)
    c = Button('Выход', 700, 450)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                a.update(event.pos)
                b.update(event.pos)
                c.update(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if a.update(event.pos):
                    start = dt.datetime.now()
                    return movement.level_1(), start
                elif c.update(event.pos):
                    sys.exit()
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


def finish_window(rez):
    global size
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Поиск Норта')
    # text = pygame.transform.scale(movement.load_image('текст.png'), (600, 170))
    movement.generate_level(movement.load_level('заключение.txt'))
    screen.blit(fon, (0, 0))
    m = Meeting(805, 360, 0, 330)
    # screen.blit(text, (190, 100))
    font = pygame.font.Font(None, 50)
    text = font.render('The End', True, (0, 0, 0))
    screen.blit(text, (275, 30))
    c = Button('Главное меню', 550, 30)
    d = Button('Время: ' + rez, 550, 80)
    running = True
    q = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(4)
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                if c.update(event.pos):
                    q = True
                else:
                    q = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if c.update(event.pos):
                    movement.tiles_group.empty()
                    movement.defeat_group.empty()
                    movement.item_group.empty()
                    movement.ladder_group.empty()
                    return True
        screen.blit(fon, (0, 0))
        movement.tiles_group.draw(screen)
        screen.blit(text, (275, 30))
        m.update1(3)
        m.update2(3)
        c.draw(q)
        d.time()
        pygame.display.flip()
        clock.tick(50)
