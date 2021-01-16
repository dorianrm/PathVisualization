import pygame
from tkinter import *
import settings as ST
import algorithms as alg
from cube_class import Cube


def init_grid():
    grid = []
    for i in range(ST.ROWS):
        grid.append([Cube(i,j) for j in range(ST.COLS)])
    return grid

def draw_cubes(surface, grid):
    for i in range(ST.ROWS):
        for j in range(ST.COLS):
            grid[i][j].draw(surface)
            

def draw_grid(surface):
    sizeBtwn = ST.WIDTH // ST.COLS
    x, y = 0, 0
    for i in range(ST.COLS):
        x = x + sizeBtwn
        pygame.draw.line(surface, 'Black', (x, 0), (x, ST.GRID_HEIGHT))  # col lines
        
    sizeBtwn = ST.GRID_HEIGHT // ST.ROWS
    for i in range(ST.ROWS):
        y = y + sizeBtwn
        pygame.draw.line(surface, 'Black', (0, y), (ST.WIDTH, y))  # row lines

def draw_window(surface, grid):
    surface.fill(ST.GRID_COL)
    draw_cubes(surface, grid)
    draw_grid(surface)
    pygame.display.update()