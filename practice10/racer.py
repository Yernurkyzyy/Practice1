import pygame, sys, random, time
from pygame.locals import *


pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()


WHITE, BLACK, RED = (255, 255, 255), (0, 0, 0), (255, 0, 0)
YELLOW, GOLD = (255, 255, 0), (255, 215, 0)
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
SPEED = 5
SCORE = 0
COINS = 0

DISPLAYSURFACE = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer Practice 11")
font_small = pygame.font.SysFont("Verdana", 20)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((50, 80))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.weight = random.choice([1, 3])
        if self.weight == 1:
            self.image = pygame.Surface((20, 20))
            self.image.fill(YELLOW)
        else:
            self.image = pygame.Surface((35, 35))
            self.image.fill(GOLD)
            
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((45, 75))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]: self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]: self.rect.move_ip(5, 0)

P1, E1, C1 = Player(), Enemy(), Coin()
enemies, coins = pygame.sprite.Group(E1), pygame.sprite.Group(C1)
all_sprites = pygame.sprite.Group(P1, E1, C1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT: pygame.quit(); sys.exit()

    DISPLAYSURFACE.fill(WHITE)
    DISPLAYSURFACE.blit(font_small.render(f"Score: {SCORE}", True, BLACK), (10, 10))
    DISPLAYSURFACE.blit(font_small.render(f"Coins: {COINS}", True, BLACK), (280, 10))

    for entity in all_sprites:
        DISPLAYSURFACE.blit(entity.image, entity.rect)
        entity.move()

   
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += C1.weight
        
        if COINS % 5 == 0:
            SPEED += 1
        C1.rect.top = 0
        C1.__init__() 

    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURFACE.fill(RED)
        pygame.display.update()
        time.sleep(1); pygame.quit(); sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)