import random
from settings import COLUMNS, BLOCK_COLORS

SHAPES = [
    {"shape": [[1, 1, 1, 1]], "color": BLOCK_COLORS[0]},
    {"shape": [[1, 1], [1, 1]], "color": BLOCK_COLORS[1]},
    {"shape": [[1, 0], [1, 1], [0, 1]], "color": BLOCK_COLORS[2]},
    {"shape": [[0, 1, 0], [1, 1, 1]], "color": BLOCK_COLORS[3]},
]


class Blocks:
    def __init__(self):
        piece = random.choice(SHAPES)
        self.shape = [row[:] for row in piece["shape"]]
        self.color = piece["color"]
        self.x = (COLUMNS - len(self.shape[0])) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
