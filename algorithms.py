import settings as ST
import window as win
from collections import deque
from cube_class import Cube


def BFS_alg(grid, surface):
    visited = set()
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
            if nei_cube not in visited and not nei_cube.wall:
                if nei_cube != ST.END_CUBE:
                    nei_cube.set_frontier()
                nei_cube.parent = curr_cube
                queue.append(nei_cube)
            win.draw_window(surface, grid)
    return False
    

def BFS(grid, surface):
    # init prev cube grid
    # BFS alg
    if not BFS_alg(grid, surface):
        print('PATH NOT FOUND')
        return
    path = []
    curr_edge = ST.END_CUBE
    while curr_edge.parent:
        prev_edge = curr_edge.parent
        if prev_edge == ST.START_CUBE:
            break
        path.append(prev_edge)
        curr_edge = prev_edge

    # Color path
    print('RIGHT BEFORE PATH')
    print(len(path))
    for cube in path[::-1]:
        cube.set_path()
        win.draw_window(surface, grid)
    
