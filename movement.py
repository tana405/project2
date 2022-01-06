import pygame
import os
import sys

jump_status = False
vertical_movement = [False, False]
horizontal_movement = [True, True]
jump = True
vniz = False
defeat = False
count_life = 3
v = 5
jump_height = 20

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
defeat_group = pygame.sprite.Group()
ladder_group = pygame.sprite.Group()
item_group = pygame.sprite.Group()

size = width, height = 805, 500
screen = pygame.display.set_mode(size)
fon = pygame.image.load('data/fon.png')
screen.blit(fon, (0, 0))
pygame.display.set_caption('')
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, ani):
        super().__init__(player_group, all_sprites)
        self.frames = []
        for i in ani:
            self.frames.append(i)

        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.counter = 0

    def image(self):
        return self.image

    def update(self, x, y):
        global jump_status, vniz, defeat, count_life
        # self.mask = pygame.mask.from_surface(self.image) МАСКА!
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect().move(x, y)
        if pygame.sprite.spritecollideany(self, defeat_group):
            if count_life == 1:
                print('Ты проиграл')
            count_life -= 1
            defeat = True

        if pygame.sprite.spritecollideany(self, ladder_group):
            vertical_movement[0] = True
        a = pygame.sprite.spritecollide(self, tiles_group, False)
        l = []
        r = []
        u = []
        d = []
        for i in a:
            if i.rect[0] < x <= i.rect[0] + 35:
                l.append(False)
            else:
                l.append(True)
            if i.rect[0] + 35 > x + 35 >= i.rect[0]:
                r.append(False)
            else:
                r.append(True)
            if i.rect[1] - 35 <= y:
                u.append(False)
            else:
                u.append(True)
            if i.rect[1] <= y + 70 and i.rect[1] - y > 50:
                d.append(False)
                if len(l) == len(d):
                    l[-1] = True
                if len(r) == len(d):
                    r[-1] = True
            else:
                d.append(True)
        if False in l:
            horizontal_movement[0] = False
        else:
            horizontal_movement[0] = True
        if False in r:
            horizontal_movement[1] = False
        else:
            horizontal_movement[1] = True
        if False in u:
            vertical_movement[0] = False
        else:
            # vertical_movement[0] = True
            pass
        if False in d:
            vertical_movement[1] = False
            vniz = False
        else:
            vertical_movement[1] = True
            vniz = True
        if pygame.sprite.spritecollideany(self, ladder_group):
            if vertical_movement[1]:
                vertical_movement[1] = True
            vertical_movement[0] = True
            vniz = False

        screen.blit(self.image, (x, y))

    def transition(self):
        print(pygame.sprite.spritecollide(self, item_group, False))
        if pygame.sprite.spritecollideany(self, item_group):
            return True

    def life(self, count):
        if self.counter == 2:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.counter = 0
        else:
            self.counter += 1
        x = 40
        for _ in range(count):
            screen.blit(self.image, (x, 40))
            x += 40


class AnimatedSpriteItem(pygame.sprite.Sprite):
    def __init__(self, ani):
        super().__init__(item_group, all_sprites)
        self.frames = []
        for i in ani:
            self.frames.append(i)

        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect().move(680, 135)
        self.counter = 0

    def wolf(self):
        if self.counter == 8:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.counter = 0
        else:
            self.counter += 1
        self.rect = self.image.get_rect().move(680, 135)
        screen.blit(self.image, (680, 135))

    def transition(self):
        if pygame.sprite.spritecollideany(self, player_group):
            return True


# анимация персонажей
right_animation = AnimatedSprite([pygame.image.load(os.path.join('data', '0.png')).convert_alpha(),
                                  pygame.image.load(os.path.join('data', '1.png')).convert_alpha(),
                                  pygame.image.load(os.path.join('data', '2.png')).convert_alpha(),
                                  pygame.image.load(os.path.join('data', '3.png')).convert_alpha(),
                                  pygame.image.load(os.path.join('data', '4.png')).convert_alpha(),
                                  pygame.image.load(os.path.join('data', '5.png')).convert_alpha(),
                                  pygame.image.load(os.path.join('data', '6.png')).convert_alpha(),
                                  pygame.image.load(os.path.join('data', '7.png')).convert_alpha(),
                                  pygame.image.load(os.path.join('data', '8.png')).convert_alpha()])
left_animation = AnimatedSprite([pygame.image.load(os.path.join('data', '00.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', '11.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', '22.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', '33.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', '44.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', '55.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', '66.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', '77.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', '88.png')).convert_alpha()])
state_animation = AnimatedSprite([pygame.image.load(os.path.join('data', '111.png')).convert_alpha()])
anima = state_animation
life_animation = AnimatedSprite([pygame.image.load(os.path.join('data', 'сердце.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', 'сердце1.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', 'сердце2.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', 'сердце3.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', 'сердце4.png')).convert_alpha()])
back_animation = AnimatedSprite([pygame.image.load(os.path.join('data', 'a1.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', 'a2.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', 'a3.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', 'a4.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', 'a5.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', 'a6.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', 'a7.png')).convert_alpha(),
                                 pygame.image.load(os.path.join('data', 'a8.png')).convert_alpha()])
state_back_animation = AnimatedSprite([pygame.image.load(os.path.join('data', 'a1.png')).convert_alpha()])
wolf_animation = AnimatedSpriteItem([pygame.image.load(os.path.join('data', 'волк1.png')).convert_alpha(),
                                     pygame.image.load(os.path.join('data', 'волк2.png')).convert_alpha()])
player = None


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                Tile('grass', x, y, tiles_group)
            elif level[y][x] == '*':
                Tile('land', x, y, tiles_group)
            elif level[y][x] == '(':
                Tile('grassl', x, y, tiles_group)
            elif level[y][x] == ')':
                Tile('grassr', x, y, tiles_group)
            elif level[y][x] == ',':
                Tile('landl', x, y, tiles_group)
            elif level[y][x] == '/':
                Tile('landr', x, y, tiles_group)
            elif level[y][x] == 'l':
                Tile('land_y_lu', x, y, tiles_group)
            elif level[y][x] == 'r':
                Tile('land_y_ru', x, y, tiles_group)
            elif level[y][x] == 'o':
                Tile('island', x, y, tiles_group)
            elif level[y][x] == 'p':
                Tile('plant', x, y, defeat_group)
            elif level[y][x] == '+':
                Tile('landl', x, y, ladder_group)
                Tile('ladder', x, y, ladder_group)
            elif level[y][x] == '=':
                Tile('grassl', x, y, ladder_group)
                Tile('ladder', x, y, ladder_group)
    return x, y


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


tile_images = {
    'land': load_image('земля.jpg', -1),
    'grass': load_image('трава.png', -1),
    'grassl': load_image('травал.png', -1),
    'grassr': load_image('травап.png', -1),
    'nothing': load_image('ничего.png', -1),
    'landl': load_image('землябокл.png', -1),
    'land_y_lu': load_image('земля_у_лв.png', -1),
    'land_y_ru': load_image('земля_у_пв.png', -1),
    'island': load_image('остров.png', -1),
    'plant': load_image('раст.png', -1),
    'ladder': load_image('лестн.png', -1),
    'landr': load_image('землябокп.png', -1)
}
# player_image = load_image('mario.png')

tile_width = tile_height = 35


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, group):
        super().__init__(group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y + 80)


# Сделать все функции и классы
def animation(y):
    global jump_status, jump, v, jump_height
    if jump_status:
        if jump_height > 0:
            y -= jump_height
            jump_height -= 4
            v = 10

        else:
            jump_status = False
            jump_height = 20
            v = 5
    else:
        jump_status = False
        jump_height = 20
        v = 5
    return y


def keyboard_events_down():
    global jump_status, jump, event
    if event.key == pygame.K_SPACE and jump:
        jump_status = True
    else:
        jump_status = False


class Borders():
    pass  # границы игры


class Obstacles_land():
    pass  # маски


def level_1():
    global defeat, anima, jump_status
    generate_level(load_level('копия.txt'))
    x = 30
    y = 360
    running = True
    i = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and jump:
                    jump_status = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    horizontal_movement[0] = False
                    anima = state_animation
                if event.key == pygame.K_RIGHT:
                    horizontal_movement[1] = False
                    anima = state_animation
                if event.key == pygame.K_UP:
                    vertical_movement[0] = False
                    anima = state_back_animation
                if event.key == pygame.K_DOWN:
                    vertical_movement[1] = False
                    anima = state_back_animation
        if defeat:
            x, y = 30, 360
            defeat = False

        screen.blit(fon, (0, 0))
        ladder_group.draw(screen)
        anima.update(x, y)
        wolf_animation.wolf()
        life_animation.life(count_life)
        i += 1
        tiles_group.update()
        keys = pygame.key.get_pressed()
        y = animation(y)

        if keys[pygame.K_LEFT] and horizontal_movement[0]:
            x -= v
            anima = left_animation
        elif keys[pygame.K_RIGHT] and horizontal_movement[1]:
            x += v
            anima = right_animation
        elif keys[pygame.K_UP] and vertical_movement[0]:
            y -= v
            anima = back_animation
        elif keys[pygame.K_DOWN] and vertical_movement[1]:
            y += v
            anima = back_animation
        if vniz and not jump_status:
            y += v + 10
        if pygame.sprite.spritecollideany(anima, item_group):
            tiles_group.empty()
            defeat_group.empty()
            item_group.empty()
            return

        tiles_group.draw(screen)
        defeat_group.draw(screen)
        pygame.display.flip()
        clock.tick(20)


def level_2():
    global defeat, anima, jump_status
    generate_level(load_level('2 уровень.txt'))
    x = 30
    y = 70
    running = True
    i = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and jump:
                    jump_status = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    horizontal_movement[0] = False
                    anima = state_animation
                if event.key == pygame.K_RIGHT:
                    horizontal_movement[1] = False
                    anima = state_animation
                if event.key == pygame.K_UP:
                    vertical_movement[0] = False
                    anima = state_back_animation
                if event.key == pygame.K_DOWN:
                    vertical_movement[1] = False
                    anima = state_back_animation
        if defeat:
            x, y = 30, 360
            defeat = False
        screen.blit(fon, (0, 0))
        life_animation.life(count_life)
        anima.update(x, y)
        i += 1
        tiles_group.update()
        keys = pygame.key.get_pressed()
        y = animation(y)

        if keys[pygame.K_LEFT] and horizontal_movement[0]:
            x -= v
            anima = left_animation
        elif keys[pygame.K_RIGHT] and horizontal_movement[1]:
            x += v
            anima = right_animation
        elif keys[pygame.K_UP] and vertical_movement[0]:
            y -= v
            anima = back_animation
        elif keys[pygame.K_DOWN] and vertical_movement[1]:
            y += v
            anima = back_animation
        if vniz and not jump_status:
            y += v + 10

        # screen.blit(anima, (0, 0))
        tiles_group.draw(screen)
        defeat_group.draw(screen)
        # player_group.draw(screen)
        pygame.display.flip()
        clock.tick(20)


level_1()
level_2()
terminate()