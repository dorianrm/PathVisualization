import pygame
import settings as ST

class Cube(object):
    def __init__(self, row, col, wall=False, parent=None, cost=0, heuristic=0):
        self.row = row
        self.col = col
        self.color = ST.DEFAULT_COLOR
        self.wall = False
        self.parent = None
        self.cost = 0
        self.heuristic = 0

    def draw(self, surface):
        dis_x, dis_y = ST.CUBE_WIDTH, ST.CUBE_HEIGHT
        pygame.draw.rect(surface, self.color, (self.col*dis_x, self.row*dis_y, dis_x, dis_y))
        # rect(left_x, left_y, dim_x, dim_y)
        
    # Color setting
    def set_start(self):
        self.color = ST.START_COLOR
    
    def set_end(self):
        self.color = ST.END_COLOR

    def set_wall(self):
        self.color = ST.WALL_COLOR
        self.wall = True
    
    def set_visited(self):
        self.color = ST.VISITED_COLOR
    
    def set_frontier(self):
        self.color = ST.FRONTIER_COLOR

    def set_path(self):
        self.color = ST.PATH_COLOR


    def set_parent(self, p_cube):
        self.parent = p_cube

    def set_cost(self, c):
        self.cost = c
    
    def set_heuristic(self, h):
        self.heuristic = h

    def get_neighbors(self):
        neighbors = []
        if self.row-1 >= 0:
            neighbors.append([self.row-1, self.col])
        if self.row+1 < ST.ROWS:
            neighbors.append([self.row+1, self.col])
        if self.col-1 >= 0:
            neighbors.append([self.row, self.col-1])
        if self.col+1 < ST.COLS:
            neighbors.append([self.row, self.col+1])
        return neighbors
    
    def reset(self):
        self.color = ST.DEFAULT_COLOR
        self.wall = False
        self.parent = None
        self.cost = 0
        self.heuristic = 0
