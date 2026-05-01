import pygame
import sys
import random
from racer import Player, Enemy, PowerUp
from persistence import save_score

pygame.init()
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Advanced TSIS3")
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("Verdana", 20)

def game_loop(user_name):
    player = Player()
    enemies = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(player)
    
    score = 0
    distance = 0
    base_speed = 5
    nitro_timer = 0
    running = True
    
    while running:
        distance += 1
        # Difficulty: әр 500 метр сайын жылдамдық артады
        if distance % 500 == 0:
            base_speed += 1
            
        # Nitro логикасы
        current_speed = base_speed + 7 if player.nitro else base_speed
        if player.nitro:
            nitro_timer -= 1
            if nitro_timer <= 0:
                player.nitro = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        # Басқару
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.rect.left > 0:
            player.rect.move_ip(-7, 0)
        if keys[pygame.K_RIGHT] and player.rect.right < WIDTH:
            player.rect.move_ip(7, 0)

        # Spawn (Жаулар мен Сары шаршылар)
        if random.randint(1, 100) < 3:
            new_enemy = Enemy(current_speed)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
            
        if random.randint(1, 300) < 2: # Сары шаршы шығу жиілігі
            new_pw = PowerUp()
            powerups.add(new_pw)
            all_sprites.add(new_pw)

        # Объектерді жылжыту
        enemies.update()
        powerups.update()

        # Соқтығысу (Collision)
        # 1. Power-ups жинау
        pw_hits = pygame.sprite.spritecollide(player, powerups, True)
        for hit in pw_hits:
            if hit.type == 'nitro':
                player.nitro = True
                nitro_timer = 180 # 3 секунд
            elif hit.type == 'shield':
                player.shield = True

        # 2. Жаулармен соқтығысу
        if pygame.sprite.spritecollide(player, enemies, False):
            if player.shield:
                player.shield = False
                pygame.sprite.spritecollide(player, enemies, True)
            else:
                save_score(user_name, score, distance)
                print(f"Game Over! Dist: {distance}")
                running = False

        # Сурет салу
        SCREEN.fill((80, 80, 80)) # Жол түсі
        
        # Жол сызықтары
        for i in range(0, HEIGHT, 40):
            pygame.draw.line(SCREEN, (255, 255, 255), (WIDTH//2, i + (distance % 40)), (WIDTH//2, i + 20 + (distance % 40)), 2)

        all_sprites.draw(SCREEN)
        
        # Инфо
        info = FONT.render(f"Score: {score} Dist: {distance} {'[NITRO!]' if player.nitro else ''}", True, (255, 255, 0))
        SCREEN.blit(info, (10, 10))
        if player.shield:
            pygame.draw.circle(SCREEN, (0, 255, 255), player.rect.center, 40, 2) # Shield визуализациясы

        pygame.display.update()
        CLOCK.tick(60)

# Бастау
name = input("Enter name: ")
game_loop(name)