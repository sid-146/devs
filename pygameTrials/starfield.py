import pygame
import sys
import random

DISPLAY_HEIGHT = 600
DISPLAY_WIDTH = 1000

# pygame.display.init()

display_size = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

bg_color = (10, 10, 10)
window = pygame.display.set_mode(display_size)

pygame.display.set_caption("Star Field")

window.fill(bg_color)

pygame.display.flip()

running = True


def get_circle(window):
    color = (255, 255, 255)

    random_x = random.randint(0, DISPLAY_WIDTH)
    random_y = random.randint(0, DISPLAY_HEIGHT)

    coordiante = [random_x, random_y]
    pygame.draw.circle(window, color, coordiante, 2, 0)


first_run = True
while running:
    get_circle(window)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
