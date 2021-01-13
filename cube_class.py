import pygame
import settings as ST

class Cube(object):
    def __init__(self, row, col, cost=0):
        self.row = row
        self.col = col
        self.color = ST.DEFAULT_COLOR
        self.cost = 0

    def set_pos(self, pos):
        self.pos = pos


    def draw(self, surface):
        # dis_x, dis_y = ST.WIDTH // ST.COLS, ST.GRID_HEIGHT // ST.ROWS
        dis_x, dis_y = ST.CUBE_WIDTH, ST.CUBE_HEIGHT
        pygame.draw.rect(surface, self.color, (self.col*dis_x, self.row*dis_y, dis_x, dis_y))
        # rect(left_x, left_y, dim_x, dim_y)
    def set_start(self):
        self.color = ST.START_COLOR
    
    def set_end(self):
        self.color = ST.END_COLOR

    def reset(self):
        self.color = ST.DEFAULT_COLOR