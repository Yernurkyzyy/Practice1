import pygame

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Verdana", 40)
        self.small_font = pygame.font.SysFont("Verdana", 20)

    def draw_text(self, text, pos, color=(0,0,0), center=True):
        surf = self.font.render(text, True, color)
        rect = surf.get_rect(center=pos) if center else surf.get_rect(topleft=pos)
        self.screen.blit(surf, rect)

    def main_menu(self):
        self.screen.fill((200, 200, 200))
        self.draw_text("RACER ADVANCED", (200, 100))
        # Бұл жерде батырмаларды салу логикасы болады (Play, Settings, т.б.)
        