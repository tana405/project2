import pygame
import os

left_status = False
right_status = False
up_status = False
down_status = False
jump_status = False
vertical_movement = False
horizontal_movement = True


# Сделать все функции и классы
def animation():
    global left_status, right_status, up_status, down_status, jump_status, \
        jump_height, x, y, anima, left_animation, right_animation
    if left_status:
        x -= 5
        anima = left_animation
    elif right_status:
        x += 5
        anima = right_animation
    if up_status:
        y -= 5
    elif down_status:
        y += 5
    if jump_status:
        if jump_height >= -20:
            y -= jump_height
            jump_height -= 4
        else:
            jump_status = False
            jump_height = 20


def keyboard_events_down():
    global left_status, right_status, up_status, down_status, jump_status, vertical_movement, horizontal_movement
    if event.key == pygame.K_LEFT and horizontal_movement:
        left_status = True
    if event.key == pygame.K_RIGHT and horizontal_movement:
        right_status = True
    if event.key == pygame.K_UP and vertical_movement:
        up_status = True
    if event.key == pygame.K_DOWN and vertical_movement:
        down_status = True
    if event.key == pygame.K_SPACE and not vertical_movement:
        jump_status = True


def keyboard_events_up():
    global left_status, right_status, up_status, down_status, jump_status, vertical_movement, horizontal_movement, \
        anima, state_animation
    if event.key == pygame.K_LEFT:
        left_status = False
        anima = state_animation
    if event.key == pygame.K_RIGHT:
        right_status = False
        anima = state_animation
    if event.key == pygame.K_UP:
        up_status = False
    if event.key == pygame.K_DOWN:
        down_status = False


class Borders():
    pass  # границы игры


class Obstacles_land():
    pass  # маски


if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 400
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    pygame.display.set_caption('')
    x = 30
    y = 300
    running = True
    jump_height = 20
    right_animation = [pygame.image.load(os.path.join('data', '0.png')).convert_alpha(),
                       pygame.image.load(os.path.join('data', '1.png')).convert_alpha(),
                       pygame.image.load(os.path.join('data', '2.png')).convert_alpha(),
                       pygame.image.load(os.path.join('data', '3.png')).convert_alpha(),
                       pygame.image.load(os.path.join('data', '4.png')).convert_alpha(),
                       pygame.image.load(os.path.join('data', '5.png')).convert_alpha(),
                       pygame.image.load(os.path.join('data', '6.png')).convert_alpha(),
                       pygame.image.load(os.path.join('data', '7.png')).convert_alpha(),
                       pygame.image.load(os.path.join('data', '8.png')).convert_alpha()]
    left_animation = [pygame.image.load(os.path.join('data', '00.png')).convert_alpha(),
                      pygame.image.load(os.path.join('data', '11.png')).convert_alpha(),
                      pygame.image.load(os.path.join('data', '22.png')).convert_alpha(),
                      pygame.image.load(os.path.join('data', '33.png')).convert_alpha(),
                      pygame.image.load(os.path.join('data', '44.png')).convert_alpha(),
                      pygame.image.load(os.path.join('data', '55.png')).convert_alpha(),
                      pygame.image.load(os.path.join('data', '66.png')).convert_alpha(),
                      pygame.image.load(os.path.join('data', '77.png')).convert_alpha(),
                      pygame.image.load(os.path.join('data', '88.png')).convert_alpha()]
    state_animation = [pygame.image.load(os.path.join('data', '111.png')).convert_alpha()]
    anima = state_animation
    clock = pygame.time.Clock()
    i = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keyboard_events_down()
            elif event.type == pygame.KEYUP:
                keyboard_events_up()
        animation()
        screen.fill((0, 0, 0))
        if anima == state_animation:
            screen.blit(anima[0], (x, y))
        else:
            screen.blit(anima[i % 9], (x, y))
        i += 1
        pygame.display.flip()
        clock.tick(20)
    pygame.quit()
