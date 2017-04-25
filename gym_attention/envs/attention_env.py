from attention_board import AttentionBoard
from board_display import *

from gym import Env, error, spaces, utils
from gym.utils import seeding

import numpy as np
import sys
import math

SIZE = 84

class AttentionEnv(Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
      self.board = AttentionBoard(SIZE)
      self.display = None

  def _step(self, action):
      reward = self.board.reward(action)
      obs = self.board.next()
      return (obs, reward, False, None)

  def _reset(self):
      self.board = AttentionBoard(SIZE)
      return self.board.board

  def _render(self, mode='human', close=False):
      if mode == 'human':
          if self.display == None:
              self.display = BoardDisplay(SIZE, SIZE)
          self.display.render_update(self.board)
      return self.board.board
