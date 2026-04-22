import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Paint Application")
    
    
    screen.fill((255, 255, 255))
    
    clock = pygame.time.Clock()
    radius = 15
    drawing = False
    color = (255, 0, 0) 
    mode = 'brush'
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: color = (255, 0, 0) # R - Red
                if event.key == pygame.K_g: color = (0, 255, 0) # G - Green
                if event.key == pygame.K_b: color = (0, 0, 255) # B - Blue
                if event.key == pygame.K_e: mode = 'eraser'     # E - Eraser
                if event.key == pygame.K_t: mode = 'brush'      # T - Brush
                if event.key == pygame.K_s: mode = 'rect'       # S - Rectangle
                if event.key == pygame.K_c: mode = 'circle'     # C - Circle

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                # Фигураларды бір рет басу арқылы салу
                if mode == 'rect':
                    pygame.draw.rect(screen, color, (event.pos[0], event.pos[1], 100, 60), 2)
                if mode == 'circle':
                    pygame.draw.circle(screen, color, event.pos, 50, 2)

            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if mode == 'brush':
                        pygame.draw.circle(screen, color, event.pos, radius)
                    if mode == 'eraser':
                        
                        pygame.draw.circle(screen, (255, 255, 255), event.pos, radius)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()