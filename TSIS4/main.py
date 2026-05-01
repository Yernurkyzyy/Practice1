import pygame
import sys
import json
import os
from game import SnakeGame
from db import save_game, get_leaderboard

# 3.5 JSON Settings
def load_settings():
    if not os.path.exists("settings.json"):
        return {"color": [0, 255, 0], "grid": True}
    with open("settings.json", "r") as f: return json.load(f)

pygame.init()
screen = pygame.display.set_mode((400, 500))
font = pygame.font.SysFont("Verdana", 20)
settings = load_settings()

def draw_text(text, pos, color=(255, 255, 255)):
    screen.blit(font.render(text, True, color), pos)

def main_menu():
    user = ""
    while True:
        screen.fill((0, 0, 0))
        draw_text("SNAKE TSIS 4", (120, 50))
        draw_text(f"Enter Username: {user}", (50, 200))
        draw_text("Press ENTER to Play", (100, 300))
        draw_text("Press L for Leaderboard", (100, 350))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and user: return user
                if event.key == pygame.K_l: show_leaderboard()
                if event.key == pygame.K_BACKSPACE: user = user[:-1]
                else: 
                    if len(user) < 15: user += event.unicode

def show_leaderboard():
    data = get_leaderboard()
    while True:
        screen.fill((20, 20, 20))
        draw_text("TOP 10 SCORES", (120, 30))
        for i, row in enumerate(data):
            draw_text(f"{i+1}. {row[0]} - {row[1]} pts (Lvl {row[2]})", (50, 80 + i*30))
        draw_text("Press B to Back", (130, 450))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b: return

def play(user):
    game = SnakeGame(color=settings['snake_color'])
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game.direction != (0, 10): game.direction = (0, -10)
                if event.key == pygame.K_DOWN and game.direction != (0, -10): game.direction = (0, 10)
                if event.key == pygame.K_LEFT and game.direction != (10, 0): game.direction = (-10, 0)
                if event.key == pygame.K_RIGHT and game.direction != (-10, 0): game.direction = (10, 0)

        if not game.move():
            save_game(user, game.score, game.level)
            return # Game Over

        screen.fill((30, 30, 30))
        if settings['grid_overlay']:
            for x in range(0, 400, 10): pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, 400))
            for y in range(0, 400, 10): pygame.draw.line(screen, (50, 50, 50), (0, y), (400, y))

        # Сурет салу
        for p in game.snake: pygame.draw.rect(screen, game.snake_color, (*p, 10, 10))
        pygame.draw.rect(screen, (0, 255, 0), (*game.food, 10, 10)) # Food
        pygame.draw.rect(screen, (255, 0, 0), (*game.poison, 10, 10)) # Poison
        if game.powerup: pygame.draw.rect(screen, (255, 255, 0), (*game.powerup, 10, 10)) # Powerup
        for obs in game.obstacles: pygame.draw.rect(screen, (150, 150, 150), (*obs, 10, 10)) # Obstacle
        
        draw_text(f"User: {user} | Score: {game.score} | Level: {game.level}", (10, 420))
        pygame.display.flip()
        clock.tick(game.speed)

if __name__ == "__main__":
    while True:
        username = main_menu()
        play(username)