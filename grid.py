
from settings import ROWS, COLUMNS


def create_grid():
    return [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]


def check_collision(grid, shape, offset_x, offset_y):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = x + offset_x
                new_y = y + offset_y

                if new_x < 0 or new_x >= COLUMNS:
                    return True
                if new_y < 0 or new_y >= ROWS:
                    return True
                if grid[new_y][new_x]:
                    return True
    return False


def merge_shape(grid, shape, offset_x, offset_y, color):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid[y + offset_y][x + offset_x] = color


def clear_lines(grid):
    new_grid = [row for row in grid if any(cell == 0 for cell in row)]
    lines_cleared = ROWS - len(new_grid)
    for _ in range(lines_cleared):
        new_grid.insert(0, [0] * COLUMNS)

    return new_grid, lines_cleared
