import pygame
import random
import math

class SnakeGame:
    def __init__(self, color=(0, 255, 0)):
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = (10, 0)
        self.score = 0
        self.level = 1
        self.speed = 10
        self.snake_color = color
        
        self.food = self.rand_pos()
        self.poison = self.rand_pos()
        self.powerup = None
        self.powerup_timer = 0
        self.obstacles = []
        
    def rand_pos(self):
        return (random.randrange(1, 39) * 10, random.randrange(1, 39) * 10)

    def spawn_obstacles(self):
        # 3-деңгейден бастап кедергілер (Критерий 3.4)
        if self.level >= 3:
            self.obstacles = [self.rand_pos() for _ in range(self.level * 2)]

    def move(self):
        head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        
        # Соқтығысуларды тексеру
        if head[0] < 0 or head[0] >= 400 or head[1] < 0 or head[1] >= 400: return False
        if head in self.snake or head in self.obstacles: return False

        self.snake.insert(0, head)

        # Кәдімгі тамақ
        if head == self.food:
            self.score += 10
            self.food = self.rand_pos()
            if self.score % 30 == 0:
                self.level += 1
                self.speed += 2
                self.spawn_obstacles()
        # Улы тамақ (Критерий 3.2)
        elif head == self.poison:
            if len(self.snake) <= 3: return False # Тым қысқа болса - өледі
            self.snake.pop(); self.snake.pop(); self.snake.pop()
            self.poison = self.rand_pos()
        else:
            self.snake.pop()
        
        # Power-up шығару (Критерий 3.3)
        if not self.powerup and random.random() < 0.02:
            self.powerup = self.rand_pos()
            self.powerup_timer = pygame.time.get_ticks()

        if self.powerup and pygame.time.get_ticks() - self.powerup_timer > 8000:
            self.powerup = None # 8 секундтан кейін жоғалады
            
        if head == self.powerup:
            self.score += 50
            self.powerup = None

        return True