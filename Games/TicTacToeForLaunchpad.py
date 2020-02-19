#!/usr/bin/env python

#TicTacToe for Launchpad by NiHuShu
#https://github.com/NiHuShu/Launchpad-Games

import launchpad_py as launchpad
import pygame

#Sorry for those global variables
moves = 0
red = False
blue = False
tie = False

def main():
    #Lauchpad setup
    mode = None
    lp = launchpad.LaunchpadMk2()
    if lp.Open(0, "mk2"):
        print("Launchpad Mk2")
        mode = "Mk2"
    if mode is None:
        print("Did not find any Launchpads, meh...")
        return

    game_board = [0, 0, 0, 0, 0, 0, 0, 0, 0, ]
    #PyGame initialisation
    pygame.init()
    white = (255, 255, 255)
    black = (0, 0, 0)
    display_surface = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("TicTacToe for Launchpad by NiHuShu")
    font1 = pygame.font.Font("freesansbold.ttf", 24)
    font2 = pygame.font.Font("freesansbold.ttf", 50)
    #Some global variables for displaying who won
    global moves
    moves = 0
    global blue
    blue = False
    global red
    red = False
    global tie
    tie = False
    player = 0 #Sets the player
    won = False #If False then game is still running
    #Boolean array for checking if the button is occupied
    placed = [False] * 9

    #Turns on white LEDs to indicate where you can move
    def empty_board():
        lp.Reset()
        lp.LedCtrlXYByCode(1,1, 3)
        lp.LedCtrlXYByCode(4, 1, 3)
        lp.LedCtrlXYByCode(7, 1, 3)
        lp.LedCtrlXYByCode(1, 4, 3)
        lp.LedCtrlXYByCode(4, 4, 3)
        lp.LedCtrlXYByCode(7, 4, 3)
        lp.LedCtrlXYByCode(1, 7, 3)
        lp.LedCtrlXYByCode(4, 7, 3)
        lp.LedCtrlXYByCode(7, 7, 3)

    #Draws red circle for "O" player
    def draw_circle(a, b):
        global moves
        moves += 1
        lp.LedCtrlXYByCode(a, b+1, 72)
        lp.LedCtrlXYByCode(a, b-1, 72)
        lp.LedCtrlXYByCode(a+1, b, 72)
        lp.LedCtrlXYByCode(a-1, b, 72)
        lp.LedCtrlXYByCode(a+1, b+1, 72)
        lp.LedCtrlXYByCode(a+1, b-1, 72)
        lp.LedCtrlXYByCode(a-1, b+1, 72)
        lp.LedCtrlXYByCode(a-1, b-1, 72)
        if but == [1,1,127]:
            game_board[0] = "O"
            lp.LedCtrlXYByCode(1, 1, 0)
        elif but == [4,1,127]:
            game_board[1] = "O"
            lp.LedCtrlXYByCode(4, 1, 0)
        elif but == [7,1,127]:
            game_board[2] = "O"
            lp.LedCtrlXYByCode(7, 1, 0)
        elif but == [1,4,127]:
            game_board[3] = "O"
            lp.LedCtrlXYByCode(1, 4, 0)
        elif but == [4,4,127]:
            game_board[4] = "O"
            lp.LedCtrlXYByCode(4, 4, 0)
        elif but == [7,4,127]:
            game_board[5] = "O"
            lp.LedCtrlXYByCode(7, 4, 0)
        elif but == [1,7,127]:
            game_board[6] = "O"
            lp.LedCtrlXYByCode(1, 7, 0)
        elif but == [4,7,127]:
            game_board[7] = "O"
            lp.LedCtrlXYByCode(4, 7, 0)
        elif but == [7,7,127]:
            game_board[8] = "O"
            lp.LedCtrlXYByCode(7, 7, 0)

    # Draws blue cross for "X" player
    def draw_cross(a, b):
        global moves
        moves += 1
        lp.LedCtrlXY(a, b, 0, 0, 64)
        lp.LedCtrlXY(a+1, b+1, 0, 0, 64)
        lp.LedCtrlXY(a+1, b-1, 0, 0, 64)
        lp.LedCtrlXY(a-1, b+1, 0, 0, 64)
        lp.LedCtrlXY(a-1, b-1, 0, 0, 64)
        if but == [1,1,127]:
            game_board[0] = "X"
        elif but == [4,1,127]:
            game_board[1] = "X"
        elif but == [7,1,127]:
            game_board[2] = "X"
        elif but == [1,4,127]:
            game_board[3] = "X"
        elif but == [4,4,127]:
            game_board[4] = "X"
        elif but == [7,4,127]:
            game_board[5] = "X"
        elif but == [1,7,127]:
            game_board[6] = "X"
        elif but == [4,7,127]:
            game_board[7] = "X"
        elif but == [7,7,127]:
            game_board[8] = "X"

    #Displays "BLUE WON" and restarts the game
    def blue_won():
        global blue
        blue = True
        draw_game()
        lp.Reset()
        lp.LedCtrlString("BLUE WON", 0, 0, 64, -1, 50)
        won = True
        lp.Close()
        main()

    #Displays "RED WON" and restarts the game
    def red_won():
        global red
        red = True
        draw_game()
        lp.Reset()
        lp.LedCtrlString("RED WON", 63, 0, 0, -1, 50)
        won = True
        lp.Close()
        main()

    #Checks row for three same letters
    def check_row():
        row_first = game_board[0] == game_board[1] == game_board[2] != 0
        row_second = game_board[3] == game_board[4] == game_board[5] != 0
        row_third = game_board[6] == game_board[7] == game_board[8] != 0
        if row_first:
            return game_board[0]
        elif row_second:
            return game_board[3]
        elif row_third:
            return game_board[6]
        else:
            pass

    # Checks column for three same letters
    def check_column():
        column_first = game_board[0] == game_board[3] == game_board[6] != 0
        column_second = game_board[1] == game_board[4] == game_board[7] != 0
        column_third = game_board[2] == game_board[5] == game_board[8] != 0
        if column_first:
            return game_board[0]
        elif column_second:
            return game_board[1]
        elif column_third:
            return game_board[2]
        else:
            pass

    # Checks diagonal for three same letters
    def check_diagonal():
        diagonal_first = game_board[0] == game_board[4] == game_board[8] != 0
        diagonal_second = game_board[2] == game_board[4] == game_board[6] != 0
        if diagonal_first:
            return  game_board[0]
        elif diagonal_second:
            return  game_board[2]
        else:
            pass

    #Checks if anyone won
    def check_win():
        #Checks for a TIE
        if moves >= 9 and won == False:
            global tie
            tie = True
            draw_game()
            lp.Reset()
            lp.LedCtrlString("TIE", 0, 64, 64, -1, 50)
            lp.Close()
            main()
        if check_row() == 'X':
            blue_won()
        elif check_column() == 'X':
            blue_won()
        elif check_diagonal() == 'X':
            blue_won()
        elif check_row() == 'O':
            red_won()
        elif check_column() == 'O':
            red_won()
        elif check_diagonal() == 'O':
            red_won()

    #Checks if a letter was already placed
    def check():
        if but == [1,1,127] and placed[0] == False:
            placed[0] = True
            return True
        if but == [4,1,127] and placed[1] == False:
            placed[1] = True
            return True
        if but == [7,1,127] and placed[2] == False:
            placed[2] = True
            return True
        if but == [1, 4, 127] and placed[3] == False:
            placed[3] = True
            return True
        if but == [4, 4, 127] and placed[4] == False:
            placed[4] = True
            return True
        if but == [7, 4, 127] and placed[5] == False:
            placed[5] = True
            return True
        if but == [1, 7, 127] and placed[6] == False:
            placed[6] = True
            return True
        if but == [4, 7, 127] and placed[7] == False:
            placed[7] = True
            return True
        if but == [7, 7, 127] and placed[8] == False:
            placed[8] = True
            return True
        else:
            return False
    def draw_game():
        #It's a bit messy but it works
        game1 = font2.render(''.join(map(str, game_board[0:1])) + "|" + ''.join(map(str, game_board[1:2])) + "|" + ''.join(map(str, game_board[2:3])), True, white)
        textRect3 = game1.get_rect()
        textRect3.center = (1280 // 2, 720 // 2)
        pygame.draw.rect(display_surface, black, (500, 300, 300, 300))
        display_surface.blit(game1, textRect3)
        game2 = font2.render(''.join(map(str, game_board[3:4])) + "|" + ''.join(map(str, game_board[4:5])) + "|" + ''.join(map(str, game_board[5:6])), True, white)
        textRect4 = game1.get_rect()
        textRect4.center = (1280 // 2, (720 // 2) + 50)
        display_surface.blit(game2, textRect4)
        game3 = font2.render(''.join(map(str, game_board[6:7])) + "|" + ''.join(map(str, game_board[7:8])) + "|" + ''.join(map(str, game_board[8:9])), True, white)
        textRect4 = game3.get_rect()
        textRect4.center = (1280 // 2, (720 // 2) + 100)
        display_surface.blit(game3, textRect4)
        pygame.display.update()
        if red:
            redwon = font2.render("RED WON", True, white)
            textRect5 = redwon.get_rect()
            textRect5.center = (1280 // 2, (720 // 2) + 300)
            display_surface.blit(redwon, textRect5)
            pygame.display.update()
        if blue:
            bluewon = font2.render("BLUE WON", True, white)
            textRect6 = bluewon.get_rect()
            textRect6.center = (1280 // 2, (720 // 2) + 300)
            display_surface.blit(bluewon, textRect6)
            pygame.display.update()
        if tie:
            tiewon = font2.render("TIE", True, white)
            textRect7 = tiewon.get_rect()
            textRect7.center = (1280 // 2, (720 // 2) + 300)
            display_surface.blit(tiewon, textRect7)
            pygame.display.update()

    #Pygame stuff
    info = font1.render("Tic Tac Toe for Laucnhpad, a simple game that I've coded for my MK2 in two days, Enjoy :D", True, white)
    disclaimer = font1.render("You can use Session button to restart the game, O start first also I've never used Python before" , True, white)
    textRect1 = info.get_rect()
    textRect1.center = (1280 // 2, 40)
    textRect2 = disclaimer.get_rect()
    textRect2.center = (1280 // 2, 80)
    display_surface.fill(black)
    display_surface.blit(info, textRect1)
    display_surface.blit(disclaimer, textRect2)
    pygame.display.update()

    lp.Reset() #Resets launchpad lights just to be sure that it's empty
    lp.ButtonFlush() #Resets the button state just in case
    lp.LedCtrlString("Tic Tac Toe", 0, 64, 0, -1, 10) #Title screen
    empty_board() #Draws white playing space
    #Game loop
    while 1:
        draw_game()
        but = lp.ButtonStateXY()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lp.Reset()
                lp.Close()
                pygame.quit()
                quit()
        if but:
            if 127 in but: #Checks if button was presse
                if but == [4, 0, 127]: #Uses "Session" button to restart the game
                    lp.Close()
                    main()
                if check():
                    if player == 0:
                        draw_circle(but[0], but[1])
                        #Changes player
                        player = not player
                        print(game_board[0:3])
                        print(game_board[3:6])
                        print(game_board[6:9])
                        check_win()
                    elif player == 1:
                        draw_cross(but[0], but[1])
                        # Changes player
                        player = not player
                        print(game_board[0:3])
                        print(game_board[3:6])
                        print(game_board[6:9])
                        check_win()


if __name__ == '__main__':
    main()