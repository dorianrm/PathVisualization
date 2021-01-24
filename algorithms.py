import pygame
import settings as ST
import window as win
from collections import deque
from cube_class import Cube
from queue import PriorityQueue

def BFS(grid, surface):
    win.reset_costs(grid)
    visited = set()
    queue = deque([ST.START_CUBE])
    while queue:
        pygame.time.delay(ST.DELAY)
        win.check_quit()
        curr_cube = queue.popleft()
        if curr_cube == ST.END_CUBE:
            construct_path(grid, surface)
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
                visited.add(nei_cube)
        win.draw_window(surface, grid)
    print('PATH NOT FOUND')
    return False

def compute_h(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)

'''
Notes:
F = G + H
F = total cost of node
G = distance between curr node and start node
H = heuristic - estiamted distance from curr node to end node
'''
def aStar(grid,surface):
    win.reset_costs(grid)
    open_set = PriorityQueue()
    entry_id = 0 #ID number when added - used for tiebreakers
    open_set.put((ST.START_CUBE.f_cost, entry_id, ST.START_CUBE))
    queue_hash = {ST.START_CUBE}
    #fcost, entry num, cube

    while not open_set.empty():
        pygame.time.delay(ST.DELAY)
        win.check_quit()

        curr_cube = open_set.get()[2] #removes from queue

        if curr_cube == ST.END_CUBE:
            construct_path(grid, surface)
            return True
        if curr_cube != ST.START_CUBE:
            curr_cube.set_visited()

        queue_hash.remove(curr_cube) #remove from hash queue

        for nei_pos in curr_cube.get_neighbors():
            r,c = nei_pos[0], nei_pos[1]
            nei_cube = grid[r][c]
            temp_g_cost = curr_cube.g_cost + 1
            if temp_g_cost < nei_cube.g_cost and not nei_cube.wall:
                nei_cube.parent = curr_cube
                nei_cube.g_cost = temp_g_cost
                nei_cube.heuristic = compute_h(nei_cube.get_pos(), ST.END_CUBE.get_pos())
                nei_cube.f_cost = temp_g_cost + nei_cube.heuristic

                if nei_cube not in queue_hash:
                    if nei_cube != ST.END_CUBE:
                        nei_cube.set_frontier()
                    entry_id += 1
                    open_set.put((nei_cube.f_cost, entry_id, nei_cube))
                    queue_hash.add(nei_cube)

        win.draw_window(surface, grid)
    print('PATH NOT FOUND')
    return False

def construct_path(grid, surface):
    # Backtrack from end to start cube
    path = []
    curr_edge = ST.END_CUBE
    while curr_edge.parent:
        prev_edge = curr_edge.parent
        if prev_edge == ST.START_CUBE:
            break
        path.append(prev_edge)
        curr_edge = prev_edge

    # Color path
    for cube in path[::-1]:
        cube.set_path()
        win.draw_window(surface, grid)
