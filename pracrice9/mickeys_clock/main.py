import pygame
import pygame
import datetime
import os

pygame.init()
W, H = 800, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mickey's Clock")


try:

    bg = pygame.image.load('images/mainclock.png')
    hand = pygame.image.load('images/mickey_hand.png')
except:
    
    print("Сурет табылмады! Тексеру режимі қосылды.")
    bg = pygame.Surface((W, H))
    bg.fill((255, 255, 255)) # Ақ фон
    hand = pygame.Surface((400, 10), pygame.SRCALPHA)
    pygame.draw.rect(hand, (0, 0, 0), (0, 0, 300, 10)) 

def rotate(image, angle):
    rotated = pygame.transform.rotate(image, angle)
    rect = rotated.get_rect(center=(W//2, H//2))
    return rotated, rect

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    
    
    sec_angle = -(now.second * 6)
    min_angle = -(now.minute * 6)

   
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    
    img_m, rect_m = rotate(hand, min_angle)
    img_s, rect_s = rotate(hand, sec_angle)

    screen.blit(img_m, rect_m)
    screen.blit(img_s, rect_s)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()