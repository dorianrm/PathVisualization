import pygame

# Global vars
def init():

    # Grid settings
    global ROWS, COLS, WIDTH, HEIGHT, GRID_HEIGHT, GRID_COL
    ROWS = 50
    COLS = 100
    WIDTH = 1401
    HEIGHT = 801
    GRID_HEIGHT = 750
    GRID_COL = (230, 230, 230)


    # Cube settings
    global START_CUBE, END_CUBE, CUBE_HEIGHT, CUBE_WIDTH
    START_CUBE = None
    END_CUBE = None
    CUBE_HEIGHT = GRID_HEIGHT // ROWS
    CUBE_WIDTH = WIDTH // COLS

    # Colors
    global DEFAULT_COLOR, START_COLOR, END_COLOR, WALL_COLOR, VISITED_COLOR, FRONTIER_COLOR, PATH_COLOR
    DEFAULT_COLOR = 'White'
    START_COLOR = 'Blue'
    END_COLOR = 'Yellow'
    WALL_COLOR = 'Black'
    VISITED_COLOR = 'Red'
    FRONTIER_COLOR = 'Pink'
    PATH_COLOR = 'Cyan'

    # global button settings
    global RUN_SEL_COLOR, RUN_DE_COLOR, RESET_SEL_COLOR, RESET_DE_COLOR, ALG_CHOICE, ALG_SEL_COLOR, ALG_DE_COLOR
    RUN_SEL_COLOR = (150,255,150)
    RUN_DE_COLOR = (0, 255, 0) # Darker shade, mouse not hovering on
    RESET_SEL_COLOR = (150, 150, 150)
    RESET_DE_COLOR = (100, 100, 100)
    ALG_CHOICE = 'BFS'
    ALG_SEL_COLOR = (238, 130, 238)
    ALG_DE_COLOR = (238, 180, 238)

    # Run Button settings
    global RUN_X, RUN_Y, RUN_WIDTH, RUN_HEIGHT, RUN_COLOR, RUN_BUTTON
    RUN_X = 0
    RUN_Y = 751
    RUN_WIDTH = 200
    RUN_HEIGHT = 50
    RUN_COLOR = RUN_SEL_COLOR
    RUN_BUTTON = pygame.Rect(RUN_X, RUN_Y, RUN_WIDTH, RUN_HEIGHT)


    global RESET_X, RESET_Y, RESET_WIDTH, RESET_HEIGHT, RESET_COLOR, RESET_BUTTON
    RESET_X = 250
    RESET_Y = 761
    RESET_WIDTH = 100
    RESET_HEIGHT = 30
    RESET_COLOR = RESET_SEL_COLOR
    RESET_BUTTON = pygame.Rect(RESET_X, RESET_Y, RESET_WIDTH, RESET_HEIGHT)

    # BFS Buttons settings
    global BFS_X, BFS_Y, BFS_WIDTH, BFS_HEIGHT, BFS_COLOR, BFS_COLOR, BFS_BUTTON
    BFS_X = (WIDTH//2) - 155
    BFS_Y = 751
    BFS_WIDTH = 150
    BFS_HEIGHT = 50
    BFS_COLOR = ALG_SEL_COLOR
    BFS_BUTTON = pygame.Rect(BFS_X, BFS_Y, BFS_WIDTH, BFS_HEIGHT)

    # Astar Button settings
    global ASTAR_X, ASTAR_Y, ASTAR_WIDTH, ASTAR_HEIGHT, ASTAR_COLOR, ASTAR_BUTTON
    ASTAR_X = (WIDTH//2) + 5
    ASTAR_Y = 751
    ASTAR_WIDTH = 150
    ASTAR_HEIGHT = 50
    ASTAR_COLOR = ALG_DE_COLOR
    ASTAR_BUTTON = pygame.Rect(ASTAR_X, ASTAR_Y, ASTAR_WIDTH, ASTAR_HEIGHT)

    # Text settings
    global RUN_FONT, RESET_FONT, FONT_COLOR
    pygame.font.init()
    RUN_FONT = pygame.font.SysFont('Arial', 25)
    RESET_FONT = pygame.font.SysFont('Arial', 15)
    FONT_COLOR = (0,0,0)