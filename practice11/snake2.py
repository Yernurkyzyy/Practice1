import pygame, random, time
pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
snake_block = 20

# Timer Event (5 seconds)
FOOD_TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(FOOD_TIMER, 5000)

def gameLoop():
    x1, y1 = WIDTH / 2, HEIGHT / 2
    x1_c, y1_c = 0, 0
    snake_list = []
    length = 1
    score = 0
    speed = 10
    
    # Food weight logic
    def spawn_food():
        fx = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
        fy = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0
        fw = random.randint(1, 3) # Weight 1 to 3
        return fx, fy, fw

    foodx, foody, foodw = spawn_food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); quit()
            if event.type == FOOD_TIMER: # Food disappears and moves
                foodx, foody, foodw = spawn_food()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: x1_c, y1_c = -20, 0
                if event.key == pygame.K_RIGHT: x1_c, y1_c = 20, 0
                if event.key == pygame.K_UP: x1_c, y1_c = 0, -20
                if event.key == pygame.K_DOWN: x1_c, y1_c = 0, 20

        x1 += x1_c; y1 += y1_c
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0: break # Wall hit

        screen.fill((0, 0, 0))
        # Draw Food with size based on weight
        pygame.draw.rect(screen, (255, 0, 0), [foodx, foody, 10 + (foodw*5), 10 + (foodw*5)])
        
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length: del snake_list[0]
        
        for segment in snake_list:
            pygame.draw.rect(screen, (0, 255, 0), [segment[0], segment[1], 20, 20])

        if x1 == foodx and y1 == foody:
            score += foodw
            length += 1
            speed += 1
            foodx, foody, foodw = spawn_food()
            pygame.time.set_timer(FOOD_TIMER, 5000) # Reset timer

        pygame.display.update()
        clock.tick(speed)

gameLoop()