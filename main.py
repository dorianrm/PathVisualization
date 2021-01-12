import pygame
from tkinter import *
import settings as ST

def draw_grid(surface):
    sizeBtwn = ST.WIDTH // ST.COLS
    x, y = 0, 0
    for i in range(ST.COLS):
        x = x + sizeBtwn
        pygame.draw.line(surface, 'Black', (x, 0), (x, ST.HEIGHT))  # col lines
        
    sizeBtwn = ST.HEIGHT // ST.ROWS
    for i in range(ST.ROWS):
        y = y + sizeBtwn
        pygame.draw.line(surface, 'Black', (0, y), (ST.WIDTH, y))  # row lines

def draw_window(surface):
    surface.fill(ST.GRID_COL)
    draw_grid(surface)
    pygame.display.update()

def exit_check():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_q]:
                pygame.quit()

def main():
    ST.init()
    window = pygame.display.set_mode((ST.WIDTH, ST.HEIGHT))

    while True:
        exit_check()
        draw_window(window)

main()

# root = Tk()
# the_label = Label(root, text="This is easy")
# the_label.pack()
# root.mainloop()