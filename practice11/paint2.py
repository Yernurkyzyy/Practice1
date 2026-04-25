import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))
mode = 'brush'
color = (0, 0, 0)

while True:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: mode = 'square'
            if event.key == pygame.K_2: mode = 'right_triangle'
            if event.key == pygame.K_3: mode = 'equilateral_triangle'
            if event.key == pygame.K_4: mode = 'rhombus'
            if event.key == pygame.K_0: mode = 'brush'

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if mode == 'square':
                pygame.draw.rect(screen, color, (x, y, 100, 100), 3)
            elif mode == 'right_triangle':
                pygame.draw.polygon(screen, color, [(x, y), (x, y+100), (x+100, y+100)], 3)
            elif mode == 'equilateral_triangle':
                pygame.draw.polygon(screen, color, [(x, y), (x-50, y+86), (x+50, y+86)], 3)
            elif mode == 'rhombus':
                pygame.draw.polygon(screen, color, [(x, y), (x+40, y+60), (x, y+120), (x-40, y+60)], 3)

        if pygame.mouse.get_pressed()[0] and mode == 'brush':
            pygame.draw.circle(screen, color, pos, 5)

    pygame.display.flip()