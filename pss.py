import pygame


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

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, pos):
        x, y = pos
        a = ((x - self.left) // self.cell_size) + 1
        b = (((y - self.top) // self.cell_size) + 1)
        if a < 1 or a > self.height or b < 1 or b > self.height:
            return None
        else:
            return (a, b)

    def on_click(self, cell):
        if cell:
            print(cell)
        else:
            print('None')

    def get_click(self, pos):
        cell = self.get_cell(pos)
        self.on_click(cell)

    def render(self, scr):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(scr, colors[1], (
                    (j * self.cell_size) + self.left, (i * self.cell_size) + self.top, self.cell_size, self.cell_size),
                                 1)

    def count(self):
        for x in range(self.left, height, self.height):
            for y in range(self.top, height, self.height):
                self.spx.append(x)
                self.spy.append(y)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Инициализация игры')
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)

    colors = ['black', 'white', 'pink']

    board = Board(5, 5)
    board.set_view(50, 50, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

    pygame.quit()
