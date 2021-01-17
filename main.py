import pygame
from tkinter import *
import settings as ST
import window as win
import algorithms as alg
from cube_class import Cube

'''
Notes:
BFS, A-star, Dijkstra, Kruskal
'''


def event_check(surface, grid):
    path_found = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        keys = pygame.key.get_pressed()
        # for key in keys:
        if keys[pygame.K_q]:
            pygame.quit()
        if keys[pygame.K_SPACE] and not path_found:
            print('PRESSED SPACE')
            alg.BFS(grid, surface) # run algorithm
            path_found = True
        
        if keys[pygame.K_r]:
            print('RESET')
            grid = win.init_grid()
            ST.START_CUBE = None
            ST.END_CUBE = None

        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            row, col = get_mouse_pos(mouse_pos)
            clicked_cube = grid[row][col]

            if ST.START_CUBE == None and clicked_cube != ST.END_CUBE:
                ST.START_CUBE = clicked_cube
                ST.START_CUBE.set_start()
            elif ST.END_CUBE == None and clicked_cube != ST.START_CUBE:
                ST.END_CUBE = clicked_cube
                ST.END_CUBE.set_end()
            elif clicked_cube != ST.START_CUBE and clicked_cube != ST.END_CUBE:
                clicked_cube.set_wall()
                # print("clicked cube: +++++++++")
                # print(clicked_cube.color)
                # print(clicked_cube.wall)
                # print('manual cube ----------')
                # print(grid[row][col].color)
                # print(grid[row][col].wall)
                # print('end ###########')


        if pygame.mouse.get_pressed()[2]:
            mouse_pos = pygame.mouse.get_pos()
            row, col = get_mouse_pos(mouse_pos)
            clicked_cube = grid[row][col]
            if clicked_cube == ST.START_CUBE:
                ST.START_CUBE.reset()
                ST.START_CUBE = None
            elif clicked_cube == ST.END_CUBE:
                ST.END_CUBE.reset()
                ST.END_CUBE = None
            else:
                clicked_cube.reset()
    return grid
    
    # if ST.START_CUBE != None:
    #     print('START CUBE (ROW,COL): ', ST.START_CUBE.row, ST.START_CUBE.col)
    # else:
    #     print('START CUBE ------')
    # if ST.END_CUBE != None:
    #     print('END CUBE (ROW,COL): ', ST.END_CUBE .row, ST.END_CUBE .col)
    # else:
    #     print('END CUBE ------')


def get_mouse_pos(pos):
    x,y = pos
    row = y // ST.CUBE_HEIGHT
    col = x // ST.CUBE_WIDTH
    return row,col                


def test_grid(grid):
    for i in range(ST.ROWS):
        for j in range(ST.COLS):
            print('ROW: ', grid[i][j].row)
            print('COL: ', grid[i][j].col)

def run():
    ST.init()
    window = pygame.display.set_mode((ST.WIDTH, ST.HEIGHT))
    grid = win.init_grid() #Entire grid and cubes stored in 'grid' var

    while True:
        win.draw_window(window, grid)
        # print('before event check')
        grid = event_check(window, grid)
        # print('after event check')

run()

# root = Tk()
# the_label = Label(root, text="This is easy")
# the_label.pack()
# root.mainloop()