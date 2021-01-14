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
EPISODES = 10000
VIEW_EVERY = 250

def main():

    # Define the pygame window
    pygame.init()
    win = pygame.display.set_mode([WEIDTH, HEIGHT])
    pygame.display.set_caption("Q-learning basic")
    done = False
    clock = pygame.time.Clock()

    """
    MOVE_UP = 0
    MOVE_RIGHT = 1
    MOVE_LEFT = 2
    MOVE_DOWN = 3
    """

    # Make the environment
    env = Environment()

    # Q table size
    SIZE = (env.board_size[0], env.board_size[1], 4)

    # Make the Q sides
    q_table = np.random.uniform(low=-2, high=-1, size=SIZE)
    for i in range(20):
        q_table[i, 0, 0] = -100  # First collum move up
        q_table[SIZE[0] - 1, i, 1] = -100  # Last collum move down
        q_table[0, i, 2] = -100  # First row move left
        q_table[i, SIZE[1] - 1, 3] = -100  # Last row move right

    # Display font
    font = pygame.font.Font('freesansbold.ttf', 32)

    # This boolean is for making the arena
    making = True

    # Making the drawing easy
    draw = False
    while not done:

        if making:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    draw = True
                    env.if_click()

                if event.type == pygame.MOUSEBUTTONUP:
                    draw = False

                if event.type == pygame.KEYDOWN:
                    making = False

            if draw:
                env.if_click()

            # Re-Drawing
            episode_text = font.render("Press any key to start the training", True, BLACK)
            explain_text = font.render("Click in the boxes to add obstacles", True, BLACK)
            win.fill((GREEN))
            env.draw(win)
            win.blit(episode_text, (50, 655))
            win.blit(explain_text, (50, 620))
            pygame.display.flip()
            clock.tick(20)

        else:
            for episode in range(EPISODES):

                if episode % VIEW_EVERY == 0:
                    view = True
                else:
                    view = False

                q_done = False

                if done:
                    break

                while not q_done and not done:

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True

                    # Q Algorithm
                    old_state = [0, 0]
                    old_state[0] = env.pos[0]
                    old_state[1] = env.pos[1]
                    action = np.argmax(q_table[env.pos[0], env.pos[1]])
                    current_q = q_table[old_state[0], old_state[1], action]
                    env.move(mv=action)
                    reward = env.get_reward()
                    max_future_q = np.max(q_table[env.pos[0], env.pos[1]])
                    new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
                    q_table[old_state[0], old_state[1], action] = new_q

                    if env.is_Done():
                        env.reset()
                        q_done = True

                    if view:
                        episode_text = font.render("Episode: " + str(episode), True, BLACK)
                        win.fill((GREEN))
                        env.draw(win)
                        win.blit(episode_text, (50, 630))
                        pygame.display.flip()
                        clock.tick(20)

if __name__ == '__main__':
    run = True
    while run:
        run = main()


