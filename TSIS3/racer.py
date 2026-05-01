import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill((255, 0, 0)) # Қызыл көлік
        self.rect = self.image.get_rect(center=(200, 500))
        self.shield = False
        self.nitro = False

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill((0, 0, 255)) # Көк көлік (жау)
        self.rect = self.image.get_rect(center=(random.randint(40, 360), -100))
        self.speed = speed

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > 600:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 'nitro' - сары, 'shield' - көкшіл
        self.type = random.choice(['nitro', 'shield'])
        self.image = pygame.Surface((30, 30))
        if self.type == 'nitro':
            self.image.fill((255, 255, 0)) # Сары түс
        else:
            self.image.fill((0, 255, 255)) # Көкшіл түс
        self.rect = self.image.get_rect(center=(random.randint(40, 360), -100))

    def update(self):
        self.rect.move_ip(0, 5) # Төмен қарай жылжиды
        if self.rect.top > 600:
            self.kill()