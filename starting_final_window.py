import pygame
from movement import load_image

size = width, height = 805, 500
screen = pygame.display.set_mode(size)
pygame.mixer.music.load('data/страшный лес.mp3')
pygame.mixer.music.set_volume(0.05)
fon = pygame.image.load('data/fon.png')
pygame.display.set_caption('')
clock = pygame.time.Clock()

def start_window():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]
    print(1)
    fon = pygame.transform.scale(load_image('fon.png'), (805, 500))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(50)

