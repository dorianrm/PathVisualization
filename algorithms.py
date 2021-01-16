import settings as ST
import window as win
from collections import deque
from cube_class import Cube


def BFS_alg(grid, surface):
    visited = set()
    global prev_grid
    queue = deque([ST.START_CUBE])
    while queue:
        curr_cube = queue.popleft()
        if curr_cube == ST.END_CUBE:
            return True
        visited.add(curr_cube)
        if curr_cube != ST.START_CUBE:
            curr_cube.set_visited()
        for nei_pos in curr_cube.get_neighbors():
            r,c = nei_pos[0], nei_pos[1]
            nei_cube = grid[r][c]
            if nei_cube not in visited:
                if nei_cube != ST.END_CUBE:
                    nei_cube.set_frontier()
                prev_grid[r][c] = curr_cube
                queue.append(nei_cube)
                # update goes here
            win.draw_window(surface, grid)
    return False
    

def BFS(grid, surface):
    # init prev cube grid
    global prev_grid
    prev_grid = []
    for i in range(ST.ROWS):
        prev_grid.append([None for j in range(ST.COLS)])
    
    # BFS alg
    if not BFS_alg(grid, surface):
        print('PATH NOT FOUND')
        return
    path = []
    curr_edge = ST.END_CUBE
    path.append(curr_edge)
    # Construct shortest path
    while prev_grid[curr_edge.row][curr_edge.col] != None:
        prev_edge = prev_grid[curr_edge.row][curr_edge.col]
        if prev_edge == ST.START_CUBE:
            break
        path.append(prev_edge)
        curr_edge = prev_edge

    # Color path
    print('RIGHT BEFORE PATH')
    for cube in path:
        cube.set_path()
    # for cube in path[::-2]:
    #     cube.set_path()
    
