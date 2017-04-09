from PIL import Image
import numpy as np
import random

class AttentionBoard(object):
    def __init__(self, size, start_pos=None, timestep=1):
        self.board = np.zeros((size, size))
        self.time = 0
        self.size = size
        self.timestep = timestep
        self.pos = np.array(start_pos) if start_pos else np.array([size/2, size/2])
        self.velocity = np.zeros((2))
        self.acceleration = np.zeros((2))
        self.update_board(self.pos)

    """ Get reward for being attentive to a certain pixel """
    def reward(self, attention, scale=1, mode='distance'):
        attention = np.array(attention)
        if attention == self.pos:
            return 1 * scale
        if mode == 'binary':
            return 0
        if mode == 'distance':
            d = numpy.linalg.norm(self.pos - attention)
            return -(d * d)

    def board(self):
        return self.board

    """ Get image from board """
    def image(self):
        w, h = self.size, self.size
        img = Image.fromarray(self.board)
        return img

    """ Update the board  """
    def next(self, acceleration=None):
        if acceleration:
            return self._next(acceleration)
        return self._rand_next()


    """ Helper Functions """

    def update_pos(self):
        pos = self.pos + (self.velocity * self.timestep) + (0.5 * self.acceleration * self.timestep * self.timestep)
        if pos[0] < 0: pos[0] = 0
        if pos[1] < 0: pos[1] = 0
        if pos[0] >= self.size: pos[0] = self.size-1
        if pos[1] >= self.size: pos[1] = self.size-1
        return pos

    def update_board(self, pos, pixel_value=255):
        self.board[self.pos[0], self.pos[1]] = 0
        self.board[pos[0], pos[1]] = pixel_value
        self.pos = pos

    def _rand_next(self):
        a = np.random.rand(2)
        return self._next(a)

    def _next(self, a):
        self.time += self.timestep
        self.acceleration += a
        self.velocity = self.velocity + self.acceleration * self.timestep
        self.update_board(self.update_pos())
        return self.board
