import pygame
import database
import movement


class NonoGram:
    def __init__(self, width_pix, height_pix, pic_name):
        self.ots = 100
        size = (width_pix, height_pix)
        self.screen = pygame.display.set_mode(size)
        db = database.Db('./picture/pictures')
        self.decision = db.load(pic_name)
        self.width = len(self.decision[0])
        self.height = len(self.decision)
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = self.ots
        self.top = self.ots
        self.cell_size = (width_pix - (2 * self.ots)) // len(self.decision)
        self.colors = ['#78944F', 'black']
        self.pic_name = pic_name
        self.running = True

    def start(self):
        pygame.init()
        pygame.display.set_caption('NonoGram')
        self.screen.fill((120, 148, 79))
        self.print_int()
        while self.running:
            for event in pygame.event.get():
                if self.is_win():
                    if self.pic_name == 'pic_1':
                        return movement.level_2()
                    else:
                        # Финальное окно
                        pass
                    self.running = False
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_click(event.pos)
                    pygame.display.flip()
            pygame.display.flip()
            self.render(self.screen)
        pygame.quit()

    def get_cell(self, pos):
        x, y = pos
        a = ((x - self.left) // self.cell_size) + 1
        b = (((y - self.top) // self.cell_size) + 1)
        if a < 1 or a > self.width or b < 1 or b > self.height:
            return None
        else:
            return a, b

    def on_click(self, cell):
        if cell:
            self.draw(cell)
        else:
            print('None')

    def get_click(self, pos):
        cell = self.get_cell(pos)
        self.on_click(cell)

    def render(self, scr):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(scr, self.colors[1], (
                    (j * self.cell_size) + self.left,
                    (i * self.cell_size) + self.top,
                    self.cell_size, self.cell_size), 1)

    def print_int(self):
        font = pygame.font.Font(None, 20)
        for j in range(len(self.decision)):
            c = 0
            position = self.left + len(self.decision[j]) * self.cell_size
            for i in range(len(self.decision[j])):
                if self.decision[j][i] == 1:
                    c += 1
                else:
                    if self.decision[j][i] == 0 and c != 0:
                        # print("{}".format(c), end=' ')
                        text = font.render(str(c), True, (0, 0, 0))
                        wdth = text.get_width()
                        position += wdth + 2 * (self.cell_size // 5)
                        self.screen.blit(text, (position, j * self.cell_size + self.top + 2 * (self.cell_size // 5)))
                        c = 0
            if c > 0:
                text = font.render(str(c), True, (0, 0, 0))
                wdth = text.get_width()
                position += wdth + 2 * (self.cell_size // 5)
                self.screen.blit(text, (position, j * self.cell_size + self.top + 2 * (self.cell_size // 5)))
            # print()
        for j in range(len(self.decision[0])):
            c = 0
            position = self.top + len(self.decision) * self.cell_size - 10
            for i in range(len(self.decision)):
                if self.decision[i][j] == 1:
                    c += 1
                else:
                    if self.decision[i][j] == 0 and c != 0:
                        # print("{}".format(c), end=' ')
                        text = font.render(str(c), True, (0, 0, 0))
                        h = text.get_height()
                        position += h + 2 * (self.cell_size // 5)
                        self.screen.blit(text, (j * self.cell_size + self.top + 2 * (self.cell_size // 5), position))
                        c = 0
            if c > 0:
                text = font.render(str(c), True, (0, 0, 0))
                wdth = text.get_width()
                position += wdth + 2 * (self.cell_size // 5)
                self.screen.blit(text, (position, j * self.cell_size + self.top + 2 * (self.cell_size // 5)))

    def is_win(self):
        for j in range(len(self.board)):
            for i in range(len(self.board[j])):
                if self.board[i][j] != self.decision[j][i]:
                    return False
        return True

    def draw(self, cell):
        x, y = cell
        if self.board[x - 1][y - 1] == 1:
            self.board[x - 1][y - 1] = 0
        else:
            self.board[x - 1][y - 1] = 1
        pygame.draw.rect(self.screen, self.colors[self.board[x - 1][y - 1]], (
            ((x - 1) * self.cell_size) + self.left,
            ((y - 1) * self.cell_size) + self.top,
            self.cell_size,
            self.cell_size))
        pygame.display.flip()
        # if self.is_win():
        # print("You win")
        # self.running = False

# if __name__ == '__main__':
# noneGram = NonoGram(700, 700, "pic_2")
# noneGram.start()
