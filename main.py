"""
 TODO: Clean up and declutter later...

"""

import pygame, sys, math
import pygame.gfxdraw

"""
 Main game stuff
"""
screen_size = (400, 400)
ttt_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_player = 1
number_of_turns = 0
game_over = False
text_msg = "Player 1's turn"

def update_ttt_board(mousePos):
    """ Get the tile that has been clicked. """
    if 50 < mousePos[0] < 350 and 50 < mousePos[1] < 350: 
        x = math.floor((mousePos[1] - 50) / 100)
        y = math.floor((mousePos[0] - 50) / 100)
        print("Player {}, position {}{} has been clicked".format(current_player, x, y))
        if ttt_board[y][x] == 0:
            ttt_board[y][x] = current_player
            return True
        return False
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

    # Go through three searches, one horizontal, one verticle and one horizontal
    # Note to self: this could be simplified!
    for y in range(3):
        sum = 0
        for x in range(3):
            if ttt_board[y][x] == current_player:
                sum += 1
                if sum == 3:
                    return True

    for x in range(3):
        sum = 0
        for y in range(3):
            if ttt_board[y][x] == current_player:
                sum += 1
                if sum == 3:
                    return True
    if ttt_board[0][0] == current_player and ttt_board[1][1] == current_player and ttt_board[2][2] == current_player:
        return True
    elif ttt_board[2][0] == current_player and ttt_board[1][1] == current_player and ttt_board[0][2] == current_player:
        return True

    return False

"""
 Drawing and pygame stuff
"""

def draw_lines(board_surface, colour = (0, 0, 0)):
    for hor in range(3):
        pygame.gfxdraw.hline(board_surface, 0, 300, hor* 100, colour)
    for ver in range(3):
        pygame.gfxdraw.vline(board_surface, ver * 100, 0, 300, colour)

def draw_tokens(board_surface, colors = ( (255, 0, 0), (0, 255, 0) )):
    for x in range(3):
        for y in range(3):
            if ttt_board[y][x] == 1:
                pygame.gfxdraw.filled_circle(board_surface, (y * 100) + 50, (x * 100) + 50, 25, colors[0])
            elif ttt_board[y][x] == 2:
                pygame.gfxdraw.filled_circle(board_surface, (y * 100) + 50, (x * 100) + 50, 25, colors[1])            
    


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    text_surface = pygame.Surface((250, 30))
    board_surface = pygame.Surface((300,300))
    font = pygame.font.Font(pygame.font.get_default_font(), 24)
    pygame.display.set_caption("Tictactoe game")
    
    while 1:
        text_msg = "Player {}'s turn".format(current_player)
        if number_of_turns == 9:
            game_over = True
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if update_ttt_board(pygame.mouse.get_pos()):
                    number_of_turns += 1
                    if not has_player_won():
                        swap_player()
                    else:
                        text_msg = "Player {} has won!".format(current_player)
                        
                    
                
        if game_over:
            text_msg = "Draw!".format(current_player)
            
        text = font.render(text_msg, 1, (255, 255, 255))
        text_pos = text.get_rect()
        text_pos.centerx = 100
        ## Drawing the essentials
        board_surface.fill((255, 255, 255))
        screen.fill((0, 0, 0))
        text_surface.fill((0, 0, 0))
        draw_lines(board_surface)
        draw_tokens(board_surface)
        text_surface.blit(text, text_pos)
        screen.blit(text_surface, (100, 5))
        screen.blit(board_surface, (50, 50))
        pygame.display.flip()

        if game_over or has_player_won():
            pygame.time.wait(2000)
            pygame.display.quit()
            sys.exit()
            
