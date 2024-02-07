import numpy as np


class SaperMan:
    def __init__(self):
        self._nb_bombs = None
        self._matrix = None
        self.view = None
        self._total_elements = None
        self.rows = None
        self.cols = None
        self.start()

    def start(self):
        pass

    def initialize(self, shape, nb_bombs):
        self.rows, self.cols = shape
        self._total_elements = np.prod(shape)
        self._matrix = np.zeros(shape=shape, dtype=np.int8)
        self.view = np.full(shape, 'X')

        bombs_indices = np.random.choice(self._total_elements, nb_bombs, replace=False)
        rows, cols = np.unravel_index(bombs_indices, shape)
        self._matrix[rows, cols] = -8

        for i in range(self.rows):
            for j in range(self.cols):
                if self._matrix[i, j] == 0:
                    self._matrix[i, j] = self.count_bombs(i, j)

    def count_bombs(self, row, col):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (0 <= row + i < self.rows and 0 <= col + j < self.cols) and (i != 0 or j != 0):
                    if self._matrix[row + i, col + j] == -8:
                        count += 1
        return count


saper = SaperMan()
saper.initialize((5, 5), 10)
print(saper._matrix)