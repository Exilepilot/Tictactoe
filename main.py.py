import sys, pygame, math
import pygame.gfxdraw
###################
# Game state stuff
###################


# Here is the board state.
board_state = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

current_player = 1 # At the start of every game, player 1 plays first.
turn_taken = False
def update_board_state(mousePos):
    """ Get the tile that has been clicked. """
    x = math.floor((mousePos[1]) / 200)
    y = math.floor((mousePos[0]) / 200)
    print("Player {}, position {}{} has been clicked".format(current_player, x, y))
    if board_state[y][x] == 0:
        board_state[y][x] = current_player
        return True
    return False


def swap_player():
    """ Change who is playing each turn. """
    global current_player
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1

def has_player_won():
    """ Check if the current player has won the game. """
    global current_player

    # Go through three searches, one horizontal, one verticle and one horizontal
    # Note to self: this could be simplified!
    for y in board_state:
        sum = 0
        for x in range(3):
            if y[x] == current_player:
                sum += 1
                if sum == 3:
                    return True

    for x in range(3):
        sum = 0
        for y in range(3):
            if board_state[y][x] == current_player:
                sum += 1
                if sum == 3:
                    return True
    if board_state[0][0] == current_player and board_state[1][1] == current_player and board_state[2][2] == current_player:
        return True
    elif board_state[2][0] == current_player and board_state[1][1] == current_player and board_state[0][2] == current_player:
        return True

    return False

###############
# Pygame stuff
###############
pygame.init()
size = (600, 600) # size of window in pixels
black = (0, 0, 0) # Make the screen black.
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)

while 1:
    for event in pygame.event.get(): # If player wants to exit, exit.
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # When player clicks on a tile, update board.
            if update_board_state(pygame.mouse.get_pos()):
                turn_taken = True
                

    screen.fill(black)

    # Draws horizontal lines
    for hor in range(3):
        pygame.gfxdraw.hline(screen, 0, 600, hor * 200, (255, 255, 255))
        
    # Draws vertical lines
    for ver in range(3):
        pygame.gfxdraw.vline(screen, ver * 200, 0, 600, (255, 255, 255))

    # Draws board 'tokens'
    for y in range(3):
        for x in range(3):
            if board_state[y][x] == 1:
                pygame.gfxdraw.filled_circle(screen, (y*200) + 100, (x*200) + 100, 50, (255, 0, 0))
            elif board_state[y][x] == 2:
                pygame.gfxdraw.filled_circle(screen, (y*200) + 100, (x*200) + 100, 50, (0, 255, 0))
    pygame.display.flip()

    if turn_taken:
        if has_player_won():
            print ("Player {} has won!".format(current_player))
            pygame.display.quit()
            sys.exit()
        else:
            swap_player()
            turn_taken = False


    
