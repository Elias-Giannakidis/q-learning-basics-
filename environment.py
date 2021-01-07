import numpy as np
import pygame

MOVE_UP = 0
MOVE_RIGHT = 1
MOVE_LEFT = 2
MOVE_DOWN = 3

# Define the colors
AQUA = (0, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
OLIVE = (128, 128, 0)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)

class Environment:

    board = np.zeros((10, 10)) - 1
    max_steps = 30
    box_size = 60

    def __init__(self):
        self.board[9, 9] = 10
        self.pos = [0, 0]
        self.step = 0
        self.path = []

    def get_reward(self):
        if self.pos[0] < 0 or self.pos[0] > 9 or self.pos[1] < 0 or self.pos[1] > 9:
            return -100
        return self.board[self.pos[0], self.pos[1]]

    def is_Done(self):
        if self.pos[0] < 0 or self.pos[0] > 9 or self.pos[1] < 0 or self.pos[1] > 9:
            return True
        if self.pos == (9, 9):
            return True
        if self.step > self.max_steps:
            return True
        else:
            return False


    def move(self, mv):
        if mv == MOVE_UP:
            self.pos[1] = self.pos[1] - 1
            x = self.pos[0]
            y = self.pos[1]
            self.path.append([x, y])
        elif mv == MOVE_DOWN:
            self.pos[1] = self.pos[1] + 1
            x = self.pos[0]
            y = self.pos[1]
            self.path.append([x, y])
        elif mv == MOVE_LEFT:
            self.pos[0] = self.pos[0] - 1
            x = self.pos[0]
            y = self.pos[1]
            self.path.append([x, y])
        elif mv == MOVE_RIGHT:
            self.pos[0] = self.pos[0] + 1
            x = self.pos[0]
            y = self.pos[1]
            self.path.append([x, y])

    def draw(self, win):
        self.step = self.step + 1
        for x in range(10):
            for y in range(10):
                xx = x*self.box_size
                yy = y*self.box_size
                for p in self.path:
                    if p == [x, y]:
                        pygame.draw.rect(win, AQUA, (xx, yy, self.box_size, self.box_size), 0)
                if self.pos == [x, y]:
                    pygame.draw.rect(win, BLACK, (xx, yy, self.box_size, self.box_size), 0)
                elif (x, y) == (9, 9):
                    pygame.draw.rect(win, WHITE, (xx, yy, self.box_size, self.box_size), 0)

                pygame.draw.rect(win, BLACK, (xx, yy, self.box_size, self.box_size), 3)
