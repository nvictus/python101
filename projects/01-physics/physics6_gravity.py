import random
import math

from euclid import Vector2
from pygame.locals import QUIT
import pygame


# Constants
FPS_LIMIT = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DRAG = 0.1


class Circle:
    def __init__(self, position, velocity, accel, radius, color, width=1):
        self.position = position
        self.velocity = velocity
        self.accel = accel
        self.radius = radius
        self.color = color
        self.width = width

    def _bounce(self):
        left_margin = self.radius
        right_margin = SCREEN_WIDTH - self.radius
        top_margin = self.radius
        bottom_margin = SCREEN_HEIGHT - self.radius

        # Check for collision with left or right wall.
        # Push the circle inwards and reflect the velocity through the y-axis
        if self.position.x <= left_margin:
            self.position.x = 2*left_margin - self.position.x
            self.velocity = self.velocity.reflect(Vector2(1,0))
        elif self.position.x >= right_margin:
            self.position.x = 2*right_margin - self.position.x
            self.velocity = self.velocity.reflect(Vector2(1,0))

        # Check for collision with top or bottom wall.
        # Push the circle inwards and reflect the velocity through the x-axis
        if self.position.y <= top_margin:
            self.position.y = 2*top_margin - self.position.y
            self.velocity = self.velocity.reflect(Vector2(0,1))
        elif self.position.y >= bottom_margin:
            self.position.y = 2*bottom_margin - self.position.y
            self.velocity = self.velocity.reflect(Vector2(0,1))

    def _get_next_position(self, dt):
        return self.position + 0.5 * self.accel * dt**2 + self.velocity * dt

    def draw(self, surface):
        pos = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(
            surface,
            self.color,
            pos,
            self.radius,
            self.width
        )

    def collide(self, other):
        collision_vector = (self.position - other.position).normalize()
        self.velocity = self.velocity.reflect(collision_vector)
        other.velocity = other.velocity.reflect(collision_vector)

    def surface_distance(self, other, dt):
        # Equation for distance between surfaces
        # d(t) = ||pos1(t) - pos2(t)|| - (r1 + r2)
        pos1 = self._get_next_position(dt)
        pos2 = other._get_next_position(dt)
        return abs(pos1 - pos2) - (self.radius + other.radius)

    def move(self, dt):
        self.velocity = self.velocity + self.accel * dt - DRAG * self.velocity * dt
        self.position = self._get_next_position(dt)
        self._bounce()


def get_random_velocity(speed):
    angle = random.uniform(0, 2*math.pi)
    x = math.cos(angle)
    y = math.sin(angle)
    unit_vector = Vector2(x, y)
    return speed * unit_vector


def main():
    colors = [BLACK, RED, GREEN, BLUE]
    speed = 100  # pixels per second
    number_of_circles = 10
    gravity = Vector2(0, 10)  # pixels per second per second

    # Initialize the display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a list of circles with random positions, radii, and velocities
    circles = []
    for i in range(number_of_circles):
        radius = random.randint(10, 20)
        x = random.randint(radius, SCREEN_WIDTH - radius)
        y = random.randint(radius, SCREEN_HEIGHT - radius)
        position = Vector2(x, y)
        velocity = get_random_velocity(speed)
        color = random.choice(colors)
        circles.append( Circle(position, velocity, gravity, radius, color) )

    ### GAME LOOP ###

    clock = pygame.time.Clock()
    running = True

    while running:

        # break out of game loop if the window is closed
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # get the time elapsed
        dt_ms = clock.tick(FPS_LIMIT)  # milliseconds
        dt = dt_ms / 1000  # convert to seconds

        # make the background white
        screen.fill(WHITE)

        # move the circles and draw them
        for i, circle in enumerate(circles):
            circle.move(dt)
            for other_circle in circles[i+1:]:
                if circle.surface_distance(other_circle, dt) <= 0:
                    circle.collide(other_circle)

        for circle in circles:
            circle.draw(screen)

        # refresh the display window
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
