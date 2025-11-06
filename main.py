import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TicTacToe")

#define variables
line_width = 6
markers = []
pos = []
player = 1

#define colors
green = (0,255,0)
red = (255,0,0)

def draw_grid():
    bg = (255,255,200)
    line = (50,50,50)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen, line, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, line, (x * 100, 0), (x * 100, screen_height), line_width)

for x in range(3):
    row = [0] * 3
    markers.append(row)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1

run = True
while run:

    draw_grid()
    draw_markers()

    #add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(f"X = {pos[0]} Y = {pos[1]}")
            cell_x = pos[0]
            cell_y = pos[1]
            if markers[cell_x // 100][cell_y // 100] == 0:
                markers[cell_x // 100][cell_y // 100] = player
                player *= -1
                """Example: cell_x = 169. 169 / 100 = 1.69. // means floor division.
                1.69 gets rounded down to nearest whole number, meaning 1.
                cell_y = 246. 246 // 100 = 2. 
                THEN, checks if list posisition of markers is 0, meaning not used by a player.
                markers[1][2] == 0.
                If the spot is empty, fill the position with the player id.
                Either 1 or -1 depending on which turn it is.
                 """
    pygame.display.update()

pygame.quit()