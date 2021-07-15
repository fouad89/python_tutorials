from utils import *

# define window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# set caption of window
pygame.display.set_caption("Paint Programm")
    
# grid & pixels
def init_grid(rows, cols, color):
    """For each row a pxiel tuple (colorV, colorV, colorV)
    corresping to the columns

    Args:
        rows (int): 0 - ROWS
        cols (int): 0 to COLUMNS
        color (tuple): (colorV, colorV, colorV)
    """
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    return grid

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE,
                                               i * PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE))
    

# drawing
def draw(win, grid):
    win.fill(BG_COLOR)
    draw_grid(win,grid)
    pygame.display.update()

# set up event loop
run = True

# set up a clock for frames per second
clock = pygame.time.Clock()
grid =init_grid(ROWS, COLS, BG_COLOR)



while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw(WIN, grid)

pygame.quet()