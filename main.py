import pygame
import numpy as np
import random
from environment import*

# Define the colors
AQUA = (0, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
OLIVE = (128, 128, 0)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)

# Window size
WEIDTH = 1055
HEIGHT = 700

# Q-learning parameters
LEARNING_RATE = 0.1
DISCOUNT = 0.99

# Q table size
SIZE = (10, 10, 4)

q_table = np.random.uniform(low=-1, high=0, size=SIZE)

def main():
    # ----  Define the pygame window ----  #
    pygame.init()
    win = pygame.display.set_mode([WEIDTH, HEIGHT])
    pygame.display.set_caption("Q-learning basic")
    done = False
    clock = pygame.time.Clock()
    # -----------------------------------#

    MOVE_UP = 0
    MOVE_RIGHT = 1
    MOVE_LEFT = 2
    MOVE_DOWN = 3
    # Make the Q sides
    for i in range(10):
        q_table[i, 0, 2] = -100 # First collum move up
        q_table[i, 9, 1] = -100 # Last collum move down
        q_table[0, i, 0] = -100 # First row move left
        q_table[9, i, 3] = -100 # Last row move right

    env = Environment()

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Q Algorithm
        old_state = env.pos
        action = np.argmax(q_table[env.pos[0], env.pos[1]])
        current_q = q_table[env.pos[0], env.pos[1], action]
        env.move(mv=action)
        reward = env.get_reward()
        print(reward)
        max_future_q = np.max(q_table[old_state[0], old_state[1]])
        new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
        q_table[old_state[0], old_state[1], action] = new_q

        if env.is_Done():
            env = Environment()

        win.fill((GREEN))
        env.draw(win)
        pygame.display.flip()
        clock.tick(20)

if __name__ == '__main__':
    run = True
    while run:
        run = main()


