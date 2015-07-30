import random
from euclid import Vector2

import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
SCREEN_SIZE = (600, 400)
screen_width, screen_height = SCREEN_SIZE
SPEED = 20  # pixels per second

colors = [BLACK, RED, GREEN, BLUE]
number_of_circles = 10


class Circle:
    def __init__(self, position, velocity, radius, color=RED, width=1):
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.color = color
        self.width = width

    def draw(self, screen_to_draw_on):
        pygame.draw.circle(
            screen_to_draw_on,
            self.color,
            (int(self.position.x), int(self.position.y)),
            self.radius,
            self.width
        )

    def move(self, dt):
        self.position = self.position + self.velocity * dt

    def __repr__(self):
        return "Circle(position={}, velocity={}, radius={}, color={}, width={})".format(
            self.position, self.velocity, self.radius, self.color, self.width)

# Initialize screen object
screen = pygame.display.set_mode(SCREEN_SIZE)

# Create a list of circles with random positions and velocities
circles = []
for i in range(number_of_circles):
    radius = random.randint(10, 20)
    x = random.randint(radius, screen_width - radius)
    y = random.randint(radius, screen_height - radius)
    position = Vector2(x, y)
    velocity = Vector2(SPEED, 0)
    color = random.choice(colors)
    circles.append(
        Circle(position, velocity, radius, color)
    )


### --- GAME LOOP --- ###

running = True
clock = pygame.time.Clock()
fps_limit = 60

while running:
    # get the time elapsed in milliseconds
    dt_ms = clock.tick(fps_limit)
    dt = dt_ms / 1000.0  # seconds

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # make background white
    screen.fill(WHITE)

    # move circles and draw them
    for circle in circles:
        circle.move(dt)
        circle.draw(screen)

    # refresh the display
    pygame.display.flip()

pygame.quit()

