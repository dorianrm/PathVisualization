import pygame
import settings as ST
from cube_class import Cube

def init_grid():
    grid = []
    for i in range(ST.ROWS):
        grid.append([Cube(i,j) for j in range(ST.COLS)])
    return grid

def draw_buttons(surface):
    pygame.draw.rect(surface, ST.RUN_COLOR, ST.RUN_BUTTON)
    pygame.draw.rect(surface, ST.RESET_COLOR, ST.RESET_BUTTON)
    pygame.draw.rect(surface, ST.BFS_COLOR, ST.BFS_BUTTON)
    pygame.draw.rect(surface, ST.ASTAR_COLOR, ST.ASTAR_BUTTON)

def draw_text(surface):
    # render(text, antialias, color, background=None)
    run_width, run_height = ST.RUN_FONT.size('Run')
    run_text = ST.RUN_FONT.render('Run', True, ST.RUN_FONT_COLOR)
    run_x = (ST.RUN_X + (ST.RUN_WIDTH//2)) - (run_width//2)
    run_y = (ST.RUN_Y + (ST.RUN_HEIGHT//2)) - (run_height//2)
    surface.blit(run_text, (run_x, run_y))

    res_width, res_height = ST.RESET_FONT.size('Reset')
    res_text = ST.RESET_FONT.render('Reset', True, ST.RESET_FONT_COLOR)
    res_x = (ST.RESET_X + (ST.RESET_WIDTH//2)) - (res_width//2)
    res_y = (ST.RESET_Y + (ST.RESET_HEIGHT//2)) - (res_height//2)
    surface.blit(res_text, (res_x, res_y))

    bfs_width, bfs_height = ST.RUN_FONT.size('BFS')
    bfs_text = ST.RUN_FONT.render('BFS', True, ST.BFS_FONT_COLOR)
    bfs_x = (ST.BFS_X + (ST.BFS_WIDTH//2)) - (bfs_width//2)
    bfs_y = (ST.BFS_Y + (ST.BFS_HEIGHT//2)) - (bfs_height//2)
    surface.blit(bfs_text, (bfs_x, bfs_y))

    astar_width, astar_height = ST.RUN_FONT.size('A-Star')
    astar_text = ST.RUN_FONT.render('A-Star', True, ST.ASTAR_FONT_COLOR)
    astar_x = (ST.ASTAR_X + (ST.ASTAR_WIDTH//2)) - (astar_width//2)
    astar_y = (ST.ASTAR_Y + (ST.ASTAR_HEIGHT//2)) - (astar_height//2)
    surface.blit(astar_text, (astar_x, astar_y))

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
    pygame.display.set_caption('Path Visualization Tool')
    draw_cubes(surface, grid)
    draw_grid(surface)
    draw_buttons(surface)
    draw_text(surface)
    pygame.display.update()

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def reset_costs(grid):
    for i in range(ST.ROWS):
        for j in range(ST.COLS):
            if grid[i][j] == ST.START_CUBE:
                grid[i][j].set_start()
            else:
                grid[i][j].f_cost = float('inf')
                grid[i][j].g_cost = float('inf')
                grid[i][j].heuristic = 0
    

