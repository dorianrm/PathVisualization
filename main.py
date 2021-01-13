import pygame
from tkinter import *
import settings as ST
from cube_class import Cube

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

def event_check(grid):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_q]:
                pygame.quit()

        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            row, col = get_mouse_pos(mouse_pos)
            clicked_cube = grid[row][col]
            if clicked_cube == ST.END_CUBE:
                if ST.START_CUBE != None:
                    ST.START_CUBE.reset()
                if ST.END_CUBE != None:
                    ST.END_CUBE = None
                ST.START_CUBE = clicked_cube
                ST.START_CUBE.set_start()
            else: # if start_cube != None:
                if ST.START_CUBE != None:
                    ST.START_CUBE.reset()
                ST.START_CUBE = clicked_cube
                ST.START_CUBE.set_start()

        if pygame.mouse.get_pressed()[2]:
            mouse_pos = pygame.mouse.get_pos()
            row, col = get_mouse_pos(mouse_pos)
            clicked_cube = grid[row][col]
            if clicked_cube == ST.START_CUBE:
                if ST.END_CUBE != None:
                    ST.END_CUBE.reset()
                if ST.START_CUBE != None:
                    ST.START_CUBE = None
                ST.END_CUBE = clicked_cube
                ST.END_CUBE.set_end()
            else: # if start_cube != None:
                if ST.END_CUBE != None:
                    ST.END_CUBE.reset()
                ST.END_CUBE = clicked_cube
                ST.END_CUBE.set_end()


    
    if ST.START_CUBE != None:
        print('START CUBE (ROW,COL): ', ST.START_CUBE.row, ST.START_CUBE.col)
    if ST.END_CUBE != None:
        print('END CUBE (ROW,COL): ', ST.END_CUBE .row, ST.END_CUBE .col)

def get_mouse_pos(pos):
    x,y = pos
    row = y // ST.CUBE_HEIGHT
    col = x // ST.CUBE_WIDTH
    return row,col                

def init_grid():
    grid = []
    for i in range(ST.ROWS):
        grid.append([Cube(i,j) for j in range(ST.COLS)])
    return grid


def test_grid(grid):
    for i in range(ST.ROWS):
        for j in range(ST.COLS):
            print('ROW: ', grid[i][j].row)
            print('COL: ', grid[i][j].col)

def main():
    ST.init()
    window = pygame.display.set_mode((ST.WIDTH, ST.HEIGHT))
    grid = init_grid() #Entire grid and cubes stored in 'grid' var
    # test_grid(grid)

    while True:
        event_check(grid)
        draw_window(window, grid)

main()

# root = Tk()
# the_label = Label(root, text="This is easy")
# the_label.pack()
# root.mainloop()