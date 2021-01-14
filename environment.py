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

    box_size = 30
    board_size = [20, 20]
    max_steps = 300

    def __init__(self):
        self.board = np.zeros((self.board_size[0], self.board_size[1])) - 1
        self.board[self.board_size[0] - 1, self.board_size[1] - 1] = 10
        self.pos = [0, 0]
        self.step = 0
        self.path = []
        self.path.append([0, 0])
        self.fire = []

    def get_reward(self):
        if self.pos[0] < 0 or self.pos[0] > self.board_size[0] - 1 or self.pos[1] < 0 or self.pos[1] > self.board_size[1] - 1:
            return -100
        return self.board[self.pos[0], self.pos[1]]

    def is_Done(self):

        for f in self.fire:
            if self.pos[0] == f[0] and self.pos[1] == f[1]:
                return True

        if self.pos[0] < 0 or self.pos[0] > self.board_size[0] - 1 or self.pos[1] < 0 or self.pos[1] > self.board_size[1] - 1:
            return True
        if self.pos == [self.board_size[0] - 1, self.board_size[1] - 1]:
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
        for x in range(self.board_size[0]):
            for y in range(self.board_size[1]):
                xx = x*self.box_size
                yy = y*self.box_size
                for p in self.path:
                    if p == [x, y]:
                        pygame.draw.rect(win, AQUA, (xx, yy, self.box_size, self.box_size), 0)
                if self.pos == [x, y]:
                    pygame.draw.rect(win, BLACK, (xx, yy, self.box_size, self.box_size), 0)
                elif (x, y) == (self.board_size[0] - 1, self.board_size[1] - 1):
                    pygame.draw.rect(win, WHITE, (xx, yy, self.box_size, self.box_size), 0)
                pygame.draw.rect(win, BLACK, (xx, yy, self.box_size, self.box_size), 3)
        for f in self.fire:
            xx = f[0] * self.box_size
            yy = f[1] * self.box_size
            pygame.draw.rect(win, BLACK, (xx, yy, self.box_size, self.box_size), 0)

    def if_click(self):
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]

        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                x1 = i * self.box_size
                x2 = (i + 1) * self.box_size
                y1 = j * self.box_size
                y2 = (j + 1) * self.box_size
                if x > x1 and x < x2 and y > y1 and y < y2:
                    self.fire.append([i, j])
                    self.board[i, j] = -100

    def reset(self):
        self.step = 0
        self.pos[0] = 0
        self.pos[1] = 0
        self.path = []
        self.path.append([0, 0])

