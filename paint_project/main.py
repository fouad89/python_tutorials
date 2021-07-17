from utils import *

# define window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# set caption of window
pygame.display.set_caption("Python Paint")
    
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
    
    if DRAW_GRID_LINES: 
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE),
                             (WIDTH, i * PIXEL_SIZE))
        for i in range(COLS +1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR))
# drawing
def draw(win, grid, buttons):
    
    win.fill(BG_COLOR)
    draw_grid(win,grid)
    for button in buttons:
        button.draw(win)
    pygame.display.update()


# to get the position of the mouse click
def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE
    if row >= ROWS:
        raise IndexError
    return row, col
    

# set up event loop
run = True

# set up a clock for frames per second
clock = pygame.time.Clock()
grid =init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

# set up buttons 
button_y = HEIGHT - TOOLBAR/2 - 25
buttons = [Button(10, button_y, 50, 50, BLACK),
           Button(70, button_y, 50, 50, RED),
           Button(130, button_y, 50, 50, GREEN),
           Button(190, button_y, 50, 50, BLUE),
           Button(250, button_y, 50, 50, WHITE, text="Erase", text_color = BLACK),
           Button(321, button_y, 50, 50, WHITE, text="Clear",text_color= BLACK)
           ]

while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]: # check for left click
            pos = pygame.mouse.get_pos()
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    drawing_color = button.color
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                        
                        
                    
                        

    draw(WIN, grid, buttons)

pygame.quet()