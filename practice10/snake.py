import pygame, random, time
pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("bahnschrift", 25)

# TASK: Timer for disappearing food (5 seconds)
FOOD_TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(FOOD_TIMER, 5000)

def spawn_food():
    # TASK: Random weight (1 to 3) affecting score and size
    fx = round(random.randrange(0, WIDTH - 20) / 20.0) * 20.0
    fy = round(random.randrange(0, HEIGHT - 20) / 20.0) * 20.0
    fw = random.randint(1, 3)
    return fx, fy, fw

def gameLoop():
    x, y = WIDTH / 2, HEIGHT / 2
    dx, dy = 0, 0
    snake_list = []
    length = 1
    score = 0
    foodx, foody, foodw = spawn_food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); quit()
            # TASK: Food disappears and respawns after time
            if event.type == FOOD_TIMER:
                foodx, foody, foodw = spawn_food()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: dx, dy = -20, 0
                elif event.key == pygame.K_RIGHT: dx, dy = 20, 0
                elif event.key == pygame.K_UP: dx, dy = 0, -20
                elif event.key == pygame.K_DOWN: dx, dy = 0, 20

        x += dx; y += dy
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0: break

        screen.fill((0, 0, 0))
        # TASK: Draw food with size depending on weight
        pygame.draw.rect(screen, (213, 50, 80), [foodx, foody, 10+(foodw*3), 10+(foodw*3)])
        
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length: del snake_list[0]
        
        for segment in snake_list:
            pygame.draw.rect(screen, (0, 255, 0), [segment[0], segment[1], 20, 20])

        if x == foodx and y == foody:
            score += foodw # TASK: Add weight to score
            length += 1
            foodx, foody, foodw = spawn_food()
            pygame.time.set_timer(FOOD_TIMER, 5000) # Reset timer on eat

        msg = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(msg, [0, 0])
        pygame.display.update()
        clock.tick(10)

gameLoop()