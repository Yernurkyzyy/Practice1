import pygame
import math

def draw_shape(surface, tool, color, start, end, thickness, is_preview=False, offset=150):
    x1, y1 = start[0], start[1] - (0 if is_preview else offset)
    x2, y2 = end[0], end[1] - (0 if is_preview else offset)
    width, height = x2 - x1, y2 - y1

    if tool == 'line':
        pygame.draw.line(surface, color, (x1, y1), (x2, y2), thickness)
    elif tool == 'rect':
        pygame.draw.rect(surface, color, (x1, y1, width, height), thickness)
    elif tool == 'square':
        side = max(abs(width), abs(height))
        s_x = x1 if width > 0 else x1 - side
        s_y = y1 if height > 0 else y1 - side
        pygame.draw.rect(surface, color, (s_x, s_y, side, side), thickness)
    elif tool == 'circle':
        radius = int(math.hypot(width, height))
        pygame.draw.circle(surface, color, (x1, y1), radius, thickness)
    elif tool == 'right_triangle':
        pygame.draw.polygon(surface, color, [(x1, y1), (x1, y2), (x2, y2)], thickness)
    elif tool == 'eq_triangle':
        side = width
        h = int(side * math.sqrt(3) / 2)
        pygame.draw.polygon(surface, color, [(x1, y1), (x1 - side//2, y1 + h), (x1 + side//2, y1 + h)], thickness)
    elif tool == 'rhombus':
        pygame.draw.polygon(surface, color, [(x1 + width//2, y1), (x2, y1 + height//2), (x1 + width//2, y2), (x1, y1 + height//2)], thickness)