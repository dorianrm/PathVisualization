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
