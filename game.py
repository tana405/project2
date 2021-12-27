import pygame
import database


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.spy = []
        self.spx = []
        self.cou = 0

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.dl = self.height * self.cell_size
        self.sh = self.width * self.cell_size

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
            self.draw(screen, cell)
            # print(cell)
        else:
            print('None')

    def get_click(self, pos):
        cell = self.get_cell(pos)
        self.on_click(cell)

    def render(self, scr):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(scr, colors[1], (
                    (j * self.cell_size) + self.left,
                    (i * self.cell_size) + self.top,
                    self.cell_size, self.cell_size), 1)

    def print_int(self):
        font = pygame.font.Font(None, 20)
        for j in range(len(decision)):
            c = 0
            position = self.left + len(decision[j]) * self.cell_size
            for i in range(len(decision[j])):
                if decision[j][i] == 1:
                    c += 1
                else:
                    if decision[j][i] == 0 and c != 0:
                        # print("{}".format(c), end=' ')
                        text = font.render(str(c), True, (0, 0, 0))
                        wdth = text.get_width()
                        position += wdth + 10
                        screen.blit(text, (position, j * self.cell_size + self.top + 10))
                        c = 0
            # print()
        for j in range(len(decision[0])):
            c = 0
            position = self.top + len(decision) * self.cell_size - 10
            for i in range(len(decision)):
                if decision[i][j] == 1:
                    c += 1
                else:
                    if decision[i][j] == 0 and c != 0:
                        # print("{}".format(c), end=' ')
                        text = font.render(str(c), True, (0, 0, 0))
                        h = text.get_height()
                        position += h + 5
                        screen.blit(text, (j * self.cell_size + self.top + 10, position))
                        c = 0
            # print()

    def count(self):
        for x in range(self.left, height, self.height):
            for y in range(self.top, height, self.height):
                self.spx.append(x)
                self.spy.append(y)

    def is_win(self):
        for j in range(len(self.board)):
            for i in range(len(self.board[j])):
                if self.board[i][j] != decision[j][i]:
                    return False
        return True

    def draw(self, screen, cell):
        x, y = cell
        if self.board[x - 1][y - 1] == 1:
            self.board[x - 1][y - 1] = 0
        else:
            self.board[x - 1][y - 1] = 1
        pygame.draw.rect(screen, colors[self.board[x - 1][y - 1]], (
            ((x - 1) * self.cell_size) + self.left,
            ((y - 1) * self.cell_size) + self.top,
            self.cell_size,
            self.cell_size))
        pygame.display.flip()
        if self.is_win():
            print("You win")


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Инициализация игры')
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    cell_size = 30

    colors = ['white', 'black']

    db = database.Db('./picture/picture1')
    decision = db.load()

    board = Board(len(decision[0]), len(decision))
    board.set_view(50, 50, cell_size)
    screen.fill((255, 255, 255))
    board.print_int()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
                pygame.display.flip()
        pygame.display.flip()
        board.render(screen)

    pygame.quit()
