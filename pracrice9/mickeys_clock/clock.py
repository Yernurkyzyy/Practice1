import pygame
import datetime

def get_time_angles():
    now = datetime.datetime.now()
    
    sec_angle = -((now.second * 6) - 90)
    min_angle = -((now.minute * 6) - 90)
    return sec_angle, min_angle

def rotate_hand(image, angle, center_pos):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=center_pos).center)
    return rotated_image, new_rect