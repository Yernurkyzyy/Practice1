import pygame
import datetime

pygame.init()
W, H = 800, 800
screen = pygame.display.set_mode((W, H))

# Суреттерді жүктеу (аттарын тексер!)
bg = pygame.image.load('mickeys_clock/images/mainclock.png')
hand = pygame.image.load('mickeys_clock/images/mickey_hand.png')

def rotate(image, angle):
    rotated = pygame.transform.rotate(image, angle)
    rect = rotated.get_rect(center=(W//2, H//2))
    return rotated, rect

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    now = datetime.datetime.now()
    # -90 градус - Миккидің қолы басында 3-ке қарап тұрса, 12-ге келтіру үшін
    sec_angle = -(now.second * 6) + 90 
    min_angle = -(now.minute * 6) + 90

    screen.blit(bg, (0, 0))
    
    img_m, rect_m = rotate(hand, min_angle)
    img_s, rect_s = rotate(hand, sec_angle)

    screen.blit(img_m, rect_m)
    screen.blit(img_s, rect_s)

    pygame.display.flip()
    pygame.time.Clock().tick(1)
pygame.quit()