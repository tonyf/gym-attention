from attention_board import AttentionBoard

from gym import Env, error, spaces, utils
from gym.utils import seeding

import numpy as np
import sys
import math

SIZE = 80

class AttentionEnv(Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
      self.board = AttentionBoard(SIZE)

  def _step(self, action):
      reward = self.board.reward(action)
      obs = self.board.next()
      return (obs, reward, False, None)

  def _reset(self):
      self.board = AttentionBoard(SIZE)
      return self.board.board()

  def _render(self, mode='human', close=False):
      image = self.board.image()
      image.show()
