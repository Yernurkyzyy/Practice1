import pygame

class Ball:
    def __init__(self, x, y, radius, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius
        self.sw = screen_width
        self.sh = screen_height
        self.step = 20

    def move(self, direction):
        if direction == "UP" and self.y - self.step >= self.radius:
            self.y -= self.step
        if direction == "DOWN" and self.y + self.step <= self.sh - self.radius:
            self.y += self.step
        if direction == "LEFT" and self.x - self.step >= self.radius:
            self.x -= self.step
        if direction == "RIGHT" and self.x + self.step <= self.sw - self.radius:
            self.x += self.step

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)