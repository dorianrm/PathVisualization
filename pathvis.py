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
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        mouse_pos = pygame.mouse.get_pos()
        row, col = get_mouse_pos(mouse_pos)


        if row < ST.ROWS and col < ST.COLS: #mouse over grid
            # Set button colors
            ST.RUN_COLOR = ST.RUN_DE_COLOR
            ST.RESET_COLOR = ST.RESET_DE_COLOR
            ST.RAND_COLOR = ST.RAND_DE_COLOR
            ST.SL_COLOR = ST.SPEED_DE_COLOR
            ST.SR_COLOR = ST.SPEED_DE_COLOR
            
            ST.RUN_FONT_COLOR = ST.FONT_DE_COLOR
            ST.RESET_FONT_COLOR = ST.FONT_DE_COLOR
            ST.RAND_FONT_COLOR = ST.FONT_DE_COLOR
            ST.SL_FONT_COLOR = ST.FONT_DE_COLOR
            ST.SR_FONT_COLOR = ST.FONT_DE_COLOR

            if ST.ALG_CHOICE == 'BFS':
                ST.BFS_COLOR = ST.ALG_SEL_COLOR
                ST.ASTAR_COLOR = ST.ALG_DE_COLOR
                ST.BFS_FONT_COLOR = ST.FONT_DE_COLOR
                ST.ASTAR_FONT_COLOR = ST.FONT_SEL_COLOR
            else:
                ST.BFS_COLOR = ST.ALG_DE_COLOR
                ST.ASTAR_COLOR = ST.ALG_SEL_COLOR
                ST.BFS_FONT_COLOR = ST.FONT_SEL_COLOR
                ST.ASTAR_FONT_COLOR = ST.FONT_DE_COLOR

            clicked_cube = grid[row][col]

            if pygame.mouse.get_pressed()[0]:
                if ST.START_CUBE == None and clicked_cube != ST.END_CUBE:
                    ST.START_CUBE = clicked_cube
                    ST.START_CUBE.set_start()
                elif ST.END_CUBE == None and clicked_cube != ST.START_CUBE:
                    ST.END_CUBE = clicked_cube
                    ST.END_CUBE.set_end()
                elif clicked_cube and clicked_cube != ST.START_CUBE and clicked_cube != ST.END_CUBE:
                    clicked_cube.set_wall()

            if pygame.mouse.get_pressed()[2]:
                if clicked_cube == ST.START_CUBE:
                    ST.START_CUBE.reset()
                    ST.START_CUBE = None
                elif clicked_cube == ST.END_CUBE:
                    ST.END_CUBE.reset()
                    ST.END_CUBE = None
                elif clicked_cube:
                    clicked_cube.reset()
        
        else: # mouse over buttons
            if ST.RUN_BUTTON.collidepoint(mouse_pos):
                print('HOVERING ON RUN BUTTON')
                ST.RUN_COLOR = ST.RUN_SEL_COLOR
                ST.RUN_FONT_COLOR = ST.FONT_SEL_COLOR
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ST.RUN_COLOR = ST.RUN_DE_COLOR
                    ST.RUN_FONT_COLOR = ST.FONT_DE_COLOR
                    if ST.START_CUBE and ST.END_CUBE:
                        if ST.ALG_CHOICE == 'BFS':
                            alg.BFS(grid, surface)
                        else:
                            alg.aStar(grid, surface)
                    else:
                        print('START AND END NOT SELECTED')

            elif ST.RESET_BUTTON.collidepoint(mouse_pos):
                print('HOVERING ON RESET BUTTON')
                ST.RESET_COLOR = ST.RESET_SEL_COLOR
                ST.RESET_FONT_COLOR = ST.FONT_SEL_COLOR
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('RESET')
                    ST.RESET_COLOR = ST.RESET_DE_COLOR
                    ST.RESET_FONT_COLOR = ST.FONT_DE_COLOR
                    grid = win.init_grid()
                    ST.START_CUBE = None
                    ST.END_CUBE = None

            elif ST.BFS_BUTTON.collidepoint(mouse_pos):
                print('HOVERING ON BFS BUTTON')
                ST.BFS_COLOR = ST.ALG_SEL_COLOR
                ST.BFS_FONT_COLOR = ST.FONT_DE_COLOR
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('SELECT BFS ALG')
                    ST.ALG_CHOICE = 'BFS'
                    ST.ASTAR_COLOR = ST.ALG_DE_COLOR
                    ST.ASTAR_FONT_COLOR = ST.FONT_SEL_COLOR

            elif ST.ASTAR_BUTTON.collidepoint(mouse_pos):
                print('HOVERING ON ASTAR BUTTON')
                ST.ASTAR_COLOR = ST.ALG_SEL_COLOR
                ST.ASTAR_FONT_COLOR = ST.FONT_DE_COLOR
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('SELECT ASTAR ALG')
                    ST.ALG_CHOICE = 'ASTAR'
                    ST.BFS_COLOR = ST.ALG_DE_COLOR
                    ST.BFS_FONT_COLOR = ST.FONT_SEL_COLOR

            elif ST.RAND_BUTTON.collidepoint(mouse_pos):
                print('HOVERING ON WALL BUTTON')
                ST.RAND_COLOR = ST.RAND_SEL_COLOR
                ST.RAND_FONT_COLOR = ST.FONT_SEL_COLOR
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('SELECT RANDOM WALLS')
                    ST.RAND_COLOR = ST.RAND_DE_COLOR
                    ST.RAND_FONT_COLOR = ST.FONT_DE_COLOR
                    grid = win.generate_random_walls(grid)
            
            elif ST.S_LEFT.collidepoint(mouse_pos):
                print('SPEED LEFT')
                ST.SL_COLOR = ST.SPEED_SEL_COLOR
                ST.SL_FONT_COLOR = ST.FONT_SEL_COLOR
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('select left increase')
                    ST.SL_COLOR = ST.SPEED_DE_COLOR
                    ST.SL_FONT_COLOR = ST.FONT_DE_COLOR
                    if ST.SPEED > 1:
                        ST.SPEED -= 1
                        ST.DELAY = 500 - (ST.SPEED * ST.SPEED_FACTOR)

            elif ST.S_RIGHT.collidepoint(mouse_pos):
                print('SPEED RIGHT')
                ST.SR_COLOR = ST.SPEED_SEL_COLOR
                ST.SR_FONT_COLOR = ST.FONT_SEL_COLOR
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('select right increase')
                    ST.SR_COLOR = ST.SPEED_DE_COLOR
                    ST.SR_FONT_COLOR = ST.FONT_DE_COLOR
                    if ST.SPEED < 10:
                        ST.SPEED += 1
                        ST.DELAY = 500 - (ST.SPEED * ST.SPEED_FACTOR)

            else:
                print('OFF RUN BUTTON')
                ST.RUN_COLOR = ST.RUN_DE_COLOR
                ST.RESET_COLOR = ST.RESET_DE_COLOR
                ST.RAND_COLOR = ST.RAND_DE_COLOR
                ST.SL_COLOR = ST.SPEED_DE_COLOR
                ST.SR_COLOR = ST.SPEED_DE_COLOR

                ST.RUN_FONT_COLOR = ST.FONT_DE_COLOR
                ST.RESET_FONT_COLOR = ST.FONT_DE_COLOR
                ST.RAND_FONT_COLOR = ST.FONT_DE_COLOR
                ST.SL_FONT_COLOR = ST.FONT_DE_COLOR
                ST.SR_FONT_COLOR = ST.FONT_DE_COLOR
                
                if ST.ALG_CHOICE == 'BFS':
                    ST.ASTAR_COLOR = ST.ALG_DE_COLOR
                    ST.ASTAR_FONT_COLOR = ST.FONT_SEL_COLOR
                else:
                    ST.BFS_COLOR = ST.ALG_DE_COLOR
                    ST.BFS_FONT_COLOR = ST.FONT_SEL_COLOR
    return grid


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

def main():
    ST.init()
    window = pygame.display.set_mode((ST.WIDTH, ST.HEIGHT))
    grid = win.init_grid() #Entire grid and cubes stored in 'grid' var

    while True:
        win.draw_window(window, grid)
        # print('before event check')
        grid = event_check(window, grid)
        # print('after event check')

main()

# root = Tk()
# the_label = Label(root, text="This is easy")
# the_label.pack()
# root.mainloop()