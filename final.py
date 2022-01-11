import pygame
import database
import movement
import os


class Final_Window:
    def __init__(self):
        size = self.width, self.height = 500, 400
        self.screen = pygame.display.set_mode(size)
        self.run = True

    def load_final_w(self):
        self.screen.fill((120, 148, 79))
        font = pygame.font.Font(None, 32)
        text = font.render("К сожалению, вы проиграли.", True, (100, 255, 100))
        text_x = self.width // 2 - text.get_width() // 2
        text_y = self.height // 2 - text.get_height() // 2
        self.screen.blit(text, (text_x, text_y))

    def start(self):
        pygame.init()
        self.screen.fill((120, 148, 79))
        self.load_final_w()
        self.run = True
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('yeees')
                    self.run = False
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     ## функия кнопки self.get_click(event.pos)
                #     #pygame.display.flip()
            pygame.display.flip()
        pygame.quit()
