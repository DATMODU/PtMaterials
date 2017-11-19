# define price vector memory and experience replay memory
from config import *

import numpy as np


class Memory(object):
    def __init__(self, total_steps):
        self.state = np.zeros(shape=[total_steps - WINDOW_SIZE + 1, NUM_ASSET, WINDOW_SIZE, INPUT_FEATURES])
        self.state_ = np.zeros(shape=[total_steps - WINDOW_SIZE + 1, NUM_ASSET, WINDOW_SIZE, INPUT_FEATURES])
        self.action = np.zeros(shape=[total_steps - WINDOW_SIZE + 1, NUM_ASSET +1])
        self.pvm_all = np.zeros(shape=[total_steps - WINDOW_SIZE + 1 + WEIGHT_LAYER, NUM_ASSET + 1])
        self.pvm_all[:WEIGHT_LAYER, 0, ] = 1  # Bitcoin 의 WIEGHTLAYER 부분만큼 가져오기 [1,0,0,0,] portfolio 설정
        self.pvm_all_ = np.zeros(shape=[total_steps - WINDOW_SIZE + 1 + WEIGHT_LAYER, NUM_ASSET + 1])
        self.pvm_all_[:WEIGHT_LAYER, 0, ] = 1  # Bitcoin 의 WIEGHTLAYER 부분만큼 가져오기 [1,0,0,0,] portfolio 설정