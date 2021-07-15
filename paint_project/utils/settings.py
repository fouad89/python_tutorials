import pygame

# initialize pygame
pygame.init()
pygame.font.init()

# colors using RGB

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
BLUE = (0, 255, 0)
GREEN = (0, 0 , 255)

# frame rate 

FPS = 60
WIDTH, HEIGHT = 600, 700

# individual pixels
ROWS = COLS = 50

# toolbar size 
TOOLBAR = HEIGHT - WIDTH
PIXEL_SIZE = WIDTH // COLS

# BIXEL SIZE
BG_COLOR = WHITE

DRAW_GRID_LINE = False

def get_font(size):
    """[summary]

    Args:
        size ([type]): [description]

    Returns:
        [type]: [font object]
    """
    return pygame.font.SysFont("comicsans", size)
