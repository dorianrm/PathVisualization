import pygame
import settings as ST

class Cube(object):
    def __init__(self, row, col, color=(255,0,0), cost=0):
        self.row = row
        self.col = col
        self.color = color
        self.cost = 0

    def set_pos(self, pos):
        self.pos = pos


    def draw(self, surface):
        dis_x, dis_y = ST.WIDTH // ST.COLS, ST.HEIGHT // ST.ROWS
        pygame.draw.rect(surface, self.color, (self.col*dis_x, self.row*dis_y, dis_x, dis_y))
        # rect(left_x, left_y, dim_x, dim_y)