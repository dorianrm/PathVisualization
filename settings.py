# Global vars
def init():

    # Grid settings
    global ROWS, COLS, WIDTH, HEIGHT, GRID_HEIGHT, GRID_COL, CUBE_HEIGHT, CUBE_WIDTH
    ROWS = 50
    COLS = 100
    WIDTH = 1401
    HEIGHT = 801
    GRID_HEIGHT = 750
    GRID_COL = (230, 230, 230)
    CUBE_HEIGHT = GRID_HEIGHT // ROWS
    CUBE_WIDTH = WIDTH // COLS

    # Cube settings
    global START_CUBE, END_CUBE, DEFAULT_COLOR, START_COLOR, END_COLOR, WALL_COLOR
    START_CUBE = None
    END_CUBE = None
    DEFAULT_COLOR = 'White'
    START_COLOR = 'Blue'
    END_COLOR = 'Yellow'
    WALL_COLOR = 'Black'