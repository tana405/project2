import pygame
import os
import sys

jump_status = False
vertical_movement = [False, False]
horizontal_movement = [True, True]
jump = True
vniz = False
defeat = False
v = 5

player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
defeat_group = pygame.sprite.Group()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, ani):
        super().__init__(player_group, all_sprites)
        self.frames = []
        for i in ani:
            self.frames.append(i)

        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()

    def update(self, x, y):
        global jump_status, vniz, defeat
        # self.mask = pygame.mask.from_surface(self.image) МАСКА!
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect().move(x, y)
        if pygame.sprite.spritecollideany(self, defeat_group):
            defeat = True
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
            vertical_movement[0] = True
        if False in d:
            vertical_movement[1] = False
            vniz = False
        else:
            vertical_movement[1] = True
            vniz = True

        screen.blit(self.image, (x, y))


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
            elif level[y][x] == 'l':
                Tile('land_y_lu', x, y, tiles_group)
            elif level[y][x] == 'r':
                Tile('land_y_ru', x, y, tiles_group)
            elif level[y][x] == 'o':
                Tile('island', x, y, tiles_group)
            elif level[y][x] == 'p':
                Tile('plant', x, y, defeat_group)
    return x, y


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
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
    'plant': load_image('раст.png', -1)
}
# player_image = load_image('mario.png')

tile_width = tile_height = 35


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, group):
        super().__init__(group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y + 80)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        # self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)


# Сделать все функции и классы
def animation():
    global jump_status, jump_height, x, y, jump, v
    if jump_status and vertical_movement[0]:
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


def keyboard_events_down():
    global jump_status, jump
    if event.key == pygame.K_SPACE and jump:
        jump_status = True
    else:
        jump_status = False


class Borders():
    pass  # границы игры


class Obstacles_land():
    pass  # маски


if __name__ == '__main__':
    pygame.init()
    size = width, height = 805, 500
    screen = pygame.display.set_mode(size)
    fon = pygame.image.load('data/fon.png')
    screen.blit(fon, (0, 0))
    pygame.display.set_caption('')
    level_x, level_y = generate_level(load_level('копия.txt'))
    x = 30
    y = 360
    q = v
    running = True
    jump_height = 20
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
    clock = pygame.time.Clock()
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
                if event.key == pygame.K_DOWN:
                    vertical_movement[1] = False
        if defeat:
            x, y = 30, 360
            defeat = False

        screen.blit(fon, (0, 0))
        anima.update(x, y)
        i += 1
        tiles_group.update()
        keys = pygame.key.get_pressed()
        animation()

        if keys[pygame.K_LEFT] and horizontal_movement[0]:
            x -= v
            anima = left_animation
        elif keys[pygame.K_RIGHT] and horizontal_movement[1]:
            x += v
            anima = right_animation
        elif keys[pygame.K_UP] and vertical_movement[0]:
            y -= v
        elif keys[pygame.K_DOWN] and vertical_movement[1]:
            y += v
        if vniz and not jump_status:
            y += v + 10

        # screen.blit(anima, (0, 0))
        tiles_group.draw(screen)
        defeat_group.draw(screen)
        # player_group.draw(screen)
        pygame.display.flip()
        clock.tick(20)

    pygame.quit()
