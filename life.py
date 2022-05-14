import time 
import pygame 
import numpy as np


COLOR_BG = (10,10,10)
COLOR_GRID =(40,40,40)

COLOR_DIE_NET = (170,170,170)
COLOR_ALIVE_NET =(255,255,255)

def update (screen,cells,size,with_progress=False):
    update_cells = np.empty((cells.shape[0], cells.shape[1]))
    for row,col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2],col-1:col+2) -cells[row,col]
        color = COLOR_BG if cells[row,col] ==0 else COLOR_ALIVE_NET

        if cells[wow,col] ==1
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COLOR_DIE_NET
        elif 2 <= alive <=3:
            updated_cells[row,col] =1
            if with_progress:
                color = COLOR_ALIVE_NET

        else:
            if alive==3:
                updated_cells[row,col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NET
        
        pygame.draw.rect(screen, color,(col * size, row*size, size -1 ,size - 1  ))
    return update_cells

    def main():
        pygame.init()