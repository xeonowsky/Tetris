import pygame
import sys

from blocks import Blocks
from settings import *
from grid import *

class Game:

    def __init__(self):
        if not pygame.get_init():
            pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Tetris")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 30, bold=True)

        self.grid = create_grid()

        self.current = Blocks()

        self.fall_time = 0
        self.score = 0

    def run(self):

        while True:

            delta_ms = self.clock.tick(FPS)
            self.fall_time += delta_ms

            self.handle_events()

            if self.fall_time >= FALL_SPEED:
                self.move_down()
                self.fall_time = 0

            self.draw()

    def move_down(self):

        if not check_collision(self.grid, self.current.shape, self.current.x, self.current.y + 1):
            self.current.y += 1
        else:
            merge_shape(
                self.grid,
                self.current.shape,
                self.current.x,
                self.current.y,
                self.current.color,
            )
            self.grid, lines_cleared = clear_lines(self.grid)
            self.score += lines_cleared * LINE_POINTS
            self.current = Blocks()

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    if not check_collision(self.grid, self.current.shape, self.current.x - 1, self.current.y):
                        self.current.x -= 1

                if event.key == pygame.K_RIGHT:
                    if not check_collision(self.grid, self.current.shape, self.current.x + 1, self.current.y):
                        self.current.x += 1

                if event.key == pygame.K_DOWN:
                    self.move_down()

                if event.key == pygame.K_UP:
                    old_shape = [row[:] for row in self.current.shape]
                    self.current.rotate()
                    if check_collision(self.grid, self.current.shape, self.current.x, self.current.y):
                        self.current.shape = old_shape

    def draw(self):

        self.screen.fill(BACKGROUND_COLOR)

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):

                rect = pygame.Rect(
                    x*CELL_SIZE,
                    y*CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )

                pygame.draw.rect(self.screen, GRID_COLOR, rect, 1)

                if cell:
                    pygame.draw.rect(self.screen, cell, rect)

        for y, row in enumerate(self.current.shape):
            for x, cell in enumerate(row):
                if cell:

                    rect = pygame.Rect(
                        (self.current.x + x) * CELL_SIZE,
                        (self.current.y + y) * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    )

                    pygame.draw.rect(self.screen, self.current.color, rect)

        footer_rect = pygame.Rect(0, HEIGHT, WIDTH, FOOTER_HEIGHT)
        pygame.draw.rect(self.screen, FOOTER_COLOR, footer_rect)
        score_surface = self.font.render(f"Wynik: {self.score}", True, TEXT_COLOR)
        score_rect = score_surface.get_rect(center=(WIDTH // 2, HEIGHT + (FOOTER_HEIGHT // 2)))
        self.screen.blit(score_surface, score_rect)

        pygame.display.update()


if __name__ == "__main__":
    Game().run()
