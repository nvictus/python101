import random
import math

from euclid import Vector2
from pygame.locals import QUIT
import pygame


# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)


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


def get_random_velocity(speed):
    angle = random.uniform(0, 2*math.pi)
    x = math.sin(angle)
    y = math.cos(angle)
    unit_vector = Vector2(x, y).normalize()
    return speed * unit_vector


def main():
    colors = [BLACK, RED, GREEN, BLUE]
    speed = 100   # pixels per second
    number_of_circles = 10

    # Initialize the display screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a list of circles with random positions, radii, and velocities
    circles = []
    for _ in range(number_of_circles):
        radius = random.randint(10, 20)
        x = random.randint(radius, SCREEN_WIDTH - radius)
        y = random.randint(radius, SCREEN_HEIGHT - radius)
        position = Vector2(x, y)
        velocity = get_random_velocity(speed)
        color = random.choice(colors)
        circles.append( Circle(position, velocity, radius, color) )

    ### --- GAME LOOP --- ###
    running = True
    clock = pygame.time.Clock()
    fps_limit = 60

    while running:
        # break out of the game loop if the window is closed
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # get the time elapsed in milliseconds
        dt_ms = clock.tick(fps_limit)
        dt = dt_ms / 1000.0  # convert to seconds

        # make background white
        screen.fill(WHITE)

        # move circles and draw them
        for circle in circles:
            circle.move(dt)
            circle.draw(screen)

        # refresh the display
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
