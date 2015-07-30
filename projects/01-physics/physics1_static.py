import random
import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
SCREEN_SIZE = screen_width, screen_height = 600, 400

colors = [BLACK, RED, GREEN, BLUE]
number_of_circles = 10


class Circle:
    def __init__(self, x, y, radius, color=RED, width=1):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.width = width

    def draw(self, screen_to_draw_on):
        pygame.draw.circle(
            screen_to_draw_on,
            self.color, 
            (self.x, self.y), 
            self.radius, 
            self.width
        )

    def __repr__(self):
        return "Circle(x={}, y={}, radius={}, color={}, width={})".format(
            self.x, self.y, self.radius, self.color, self.width)

screen = pygame.display.set_mode(SCREEN_SIZE)

circles = []
for i in range(number_of_circles):
    radius = random.randint(10, 20)
    x = random.randint(radius, screen_width - radius)
    y = random.randint(radius, screen_height - radius)
    color = random.choice(colors)
    circles.append(Circle(x, y, radius, color))


running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Make the background white
    screen.fill(WHITE)

    # Draw the circles on the screen canvas
    for circle in circles:
        circle.draw(screen)

    # Refresh the display
    pygame.display.flip()

pygame.quit()

