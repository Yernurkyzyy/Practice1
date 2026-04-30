import pygame
import datetime
import sys
from tools import draw_shape # tools.py-дан функцияны аламыз

class PaintApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 750))
        pygame.display.set_caption("Paint TSIS2")
        self.canvas = pygame.Surface((1000, 600))
        self.canvas.fill((255, 255, 255))
        self.clock = pygame.time.Clock()
        self.tool, self.color, self.thickness = 'pencil', (0,0,0), 2
        self.drawing = False
        self.start_pos = None
        self.last_pos = None
        self.text_active, self.text_content, self.text_pos = False, "", None
        self.font = pygame.font.SysFont("Arial", 20)

    def flood_fill(self, x, y, new_color):
        target = self.canvas.get_at((x, y))
        if target == new_color: return
        pixels = [(x, y)]
        while pixels:
            cx, cy = pixels.pop()
            if self.canvas.get_at((cx, cy)) != target: continue
            self.canvas.set_at((cx, cy), new_color)
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < 1000 and 0 <= ny < 600: pixels.append((nx, ny))

    def run(self):
        while True:
            self.screen.fill((220, 220, 220))
            self.screen.blit(self.canvas, (0, 150))
            
            # UI мәтіндері
            self.screen.blit(self.font.render(f"Tool: {self.tool} | Size: {self.thickness}", True, (0,0,0)), (10, 10))
            self.screen.blit(self.font.render("P: Pencil | L: Line | S: Square | T: Rect | C: Circle | E: Eq.Tri | F: Fill | X: Text", True, (0,0,0)), (10, 40))

            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        pygame.image.save(self.canvas, f"paint_{datetime.datetime.now().strftime('%H%M%S')}.png")
                    if event.key == pygame.K_1: self.thickness = 2
                    if event.key == pygame.K_2: self.thickness = 5
                    if event.key == pygame.K_3: self.thickness = 10
                    # Құралдар
                    tools_map = {pygame.K_p:'pencil', pygame.K_l:'line', pygame.K_s:'square', pygame.K_t:'rect', 
                                 pygame.K_c:'circle', pygame.K_e:'eq_triangle', pygame.K_f:'fill', pygame.K_x:'text'}
                    if event.key in tools_map: self.tool = tools_map[event.key]
                    
                    if self.text_active:
                        if event.key == pygame.K_RETURN:
                            self.canvas.blit(self.font.render(self.text_content, True, self.color), (self.text_pos[0], self.text_pos[1]-150))
                            self.text_active = False
                        elif event.key == pygame.K_ESCAPE: self.text_active = False
                        else: self.text_content += event.unicode

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[1] > 150:
                        if self.tool == 'fill': self.flood_fill(event.pos[0], event.pos[1]-150, self.color)
                        elif self.tool == 'text': self.text_active, self.text_pos, self.text_content = True, event.pos, ""
                        else: self.drawing, self.start_pos, self.last_pos = True, event.pos, event.pos

                if event.type == pygame.MOUSEBUTTONUP:
                    if self.drawing and self.tool != 'pencil':
                        draw_shape(self.canvas, self.tool, self.color, self.start_pos, event.pos, self.thickness)
                    self.drawing = False

                if event.type == pygame.MOUSEMOTION and self.drawing and self.tool == 'pencil':
                    pygame.draw.line(self.canvas, self.color, (self.last_pos[0], self.last_pos[1]-150), (event.pos[0], event.pos[1]-150), self.thickness)
                    self.last_pos = event.pos

            if self.drawing and self.tool not in ['pencil', 'fill', 'text']:
                draw_shape(self.screen, self.tool, self.color, self.start_pos, pygame.mouse.get_pos(), self.thickness, is_preview=True)
            
            if self.text_active: self.screen.blit(self.font.render(self.text_content + "|", True, self.color), self.text_pos)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    PaintApp().run()