#!/usr/bin/env python

#Dice for Launchpad by NiHuShu
#https://github.com/NiHuShu/Launchpad-Games

import launchpad_py as launchpad
from pygame import time
from random import randint

def main():
    #Launchpad setup
    mode = None
    lp = launchpad.LaunchpadMk2()
    if lp.Open(0, "mk2"):
        print("Launchpad Mk2")
        mode = "Mk2"
    if mode is None:
        print("Did not find any Launchpads, meh...")
        return
    #Variables for choosing color of the dice
    x = 0
    colors = [3, 16, 24, 40, 56, 72]
    selected_color = colors[x]
    #Figures on dice
    def one():
        lp.LedCtrlXYByCode(4, 5, selected_color)
        lp.LedCtrlXYByCode(4, 6, selected_color)
        lp.LedCtrlXYByCode(5, 5, selected_color)
        lp.LedCtrlXYByCode(5, 6, selected_color)

    def two():
        lp.LedCtrlXYByCode(2, 7, selected_color)
        lp.LedCtrlXYByCode(2, 8, selected_color)
        lp.LedCtrlXYByCode(3, 7, selected_color)
        lp.LedCtrlXYByCode(3, 8, selected_color)
        lp.LedCtrlXYByCode(6, 3, selected_color)
        lp.LedCtrlXYByCode(6, 4, selected_color)
        lp.LedCtrlXYByCode(7, 3, selected_color)
        lp.LedCtrlXYByCode(7, 4, selected_color)

    def three():
        lp.LedCtrlXYByCode(2, 7, selected_color)
        lp.LedCtrlXYByCode(2, 8, selected_color)
        lp.LedCtrlXYByCode(3, 7, selected_color)
        lp.LedCtrlXYByCode(3, 8, selected_color)
        lp.LedCtrlXYByCode(4, 5, selected_color)
        lp.LedCtrlXYByCode(4, 6, selected_color)
        lp.LedCtrlXYByCode(5, 5, selected_color)
        lp.LedCtrlXYByCode(5, 6, selected_color)
        lp.LedCtrlXYByCode(6, 3, selected_color)
        lp.LedCtrlXYByCode(6, 4, selected_color)
        lp.LedCtrlXYByCode(7, 3, selected_color)
        lp.LedCtrlXYByCode(7, 4, selected_color)

    def four():
        lp.LedCtrlXYByCode(2, 7, selected_color)
        lp.LedCtrlXYByCode(2, 8, selected_color)
        lp.LedCtrlXYByCode(3, 7, selected_color)
        lp.LedCtrlXYByCode(3, 8, selected_color)
        lp.LedCtrlXYByCode(6, 3, selected_color)
        lp.LedCtrlXYByCode(6, 4, selected_color)
        lp.LedCtrlXYByCode(7, 3, selected_color)
        lp.LedCtrlXYByCode(7, 4, selected_color)
        lp.LedCtrlXYByCode(2, 3, selected_color)
        lp.LedCtrlXYByCode(2, 4, selected_color)
        lp.LedCtrlXYByCode(3, 3, selected_color)
        lp.LedCtrlXYByCode(3, 4, selected_color)
        lp.LedCtrlXYByCode(6, 7, selected_color)
        lp.LedCtrlXYByCode(6, 8, selected_color)
        lp.LedCtrlXYByCode(7, 7, selected_color)
        lp.LedCtrlXYByCode(7, 8, selected_color)

    def five():
        lp.LedCtrlXYByCode(4, 5, selected_color)
        lp.LedCtrlXYByCode(4, 6, selected_color)
        lp.LedCtrlXYByCode(5, 5, selected_color)
        lp.LedCtrlXYByCode(5, 6, selected_color)
        lp.LedCtrlXYByCode(2, 7, selected_color)
        lp.LedCtrlXYByCode(2, 8, selected_color)
        lp.LedCtrlXYByCode(3, 7, selected_color)
        lp.LedCtrlXYByCode(3, 8, selected_color)
        lp.LedCtrlXYByCode(6, 3, selected_color)
        lp.LedCtrlXYByCode(6, 4, selected_color)
        lp.LedCtrlXYByCode(7, 3, selected_color)
        lp.LedCtrlXYByCode(7, 4, selected_color)
        lp.LedCtrlXYByCode(2, 3, selected_color)
        lp.LedCtrlXYByCode(2, 4, selected_color)
        lp.LedCtrlXYByCode(3, 3, selected_color)
        lp.LedCtrlXYByCode(3, 4, selected_color)
        lp.LedCtrlXYByCode(6, 7, selected_color)
        lp.LedCtrlXYByCode(6, 8, selected_color)
        lp.LedCtrlXYByCode(7, 7, selected_color)
        lp.LedCtrlXYByCode(7, 8, selected_color)
        
    def six():
        lp.LedCtrlXYByCode(2, 7, selected_color)
        lp.LedCtrlXYByCode(2, 8, selected_color)
        lp.LedCtrlXYByCode(3, 7, selected_color)
        lp.LedCtrlXYByCode(3, 8, selected_color)
        lp.LedCtrlXYByCode(6, 3, selected_color)
        lp.LedCtrlXYByCode(6, 4, selected_color)
        lp.LedCtrlXYByCode(7, 3, selected_color)
        lp.LedCtrlXYByCode(7, 4, selected_color)
        lp.LedCtrlXYByCode(2, 3, selected_color)
        lp.LedCtrlXYByCode(2, 4, selected_color)
        lp.LedCtrlXYByCode(3, 3, selected_color)
        lp.LedCtrlXYByCode(3, 4, selected_color)
        lp.LedCtrlXYByCode(6, 7, selected_color)
        lp.LedCtrlXYByCode(6, 8, selected_color)
        lp.LedCtrlXYByCode(7, 7, selected_color)
        lp.LedCtrlXYByCode(7, 8, selected_color)
        lp.LedCtrlXYByCode(2, 5, selected_color)
        lp.LedCtrlXYByCode(2, 6, selected_color)
        lp.LedCtrlXYByCode(3, 5, selected_color)
        lp.LedCtrlXYByCode(3, 6, selected_color)
        lp.LedCtrlXYByCode(6, 5, selected_color)
        lp.LedCtrlXYByCode(6, 6, selected_color)
        lp.LedCtrlXYByCode(7, 5, selected_color)
        lp.LedCtrlXYByCode(7, 6, selected_color)
    #Rolling animation
    def animation():
        six()
        time.wait(200)
        lp.Reset()
        one()
        time.wait(200)
        lp.Reset()
        five()
        time.wait(200)
        lp.Reset()
        three()
        time.wait(200)
        lp.Reset()
        four()
        time.wait(200)
        lp.Reset()
        two()
        time.wait(200)
        lp.Reset()
     #Reset before start   
    lp.Reset()
    while 1:
        selected_color = colors[x]
        #Selecting dice color
        lp.LedCtrlXYByCode(2,0, selected_color)
        lp.LedCtrlXYByCode(3, 0, selected_color)
        lp.LedCtrlXYByCode(0, 1, selected_color)
        but = lp.ButtonStateXY()
        if but:
            print(x)
            if 127 in but:
                if but == [2, 0, 127]:
                    x -= 1
                    if x < 0:
                        x = 5
                if but == [3, 0, 127]:
                    x += 1
                    if x > 5:
                        x = 0
                if but == [0, 1, 127]:
                    dice_side = randint(1, 6)
                    animation()
                    if dice_side == 1:
                        one()
                    if dice_side == 2:
                        two()
                    if dice_side == 3:
                        three()
                    if dice_side == 4:
                        four()
                    if dice_side == 5:
                        five()
                    if dice_side == 6:
                        six()



if __name__ == '__main__':
    main()
