#!/usr/bin/env python

#Paint for Launchpad by NiHuShu
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
    r = 1
    g = 1
    b = 1
    lp.Reset()
    while 1:
        lp.LedCtrlXY(0,0,r,0,0)
        lp.LedCtrlXY(1,0,r,0,0)
        lp.LedCtrlXY(2, 0, 0, g, 0)
        lp.LedCtrlXY(3, 0, 0, g, 0)
        lp.LedCtrlXY(4, 0, 0, 0, b)
        lp.LedCtrlXY(5, 0, 0, 0, b)
        lp.LedCtrlXY(6, 0, r, g, b)
        lp.LedCtrlXY(8, 0, 32, 32, 32)
        lp.LedCtrlXY(8, 1, 63, 0, 0)
        lp.LedCtrlXY(8, 2, 0, 63, 0)
        lp.LedCtrlXY(8, 3, 0, 0, 63)
        lp.LedCtrlXY(8, 4, 63, 63, 0)
        lp.LedCtrlXY(8, 5, 0, 63, 63)
        lp.LedCtrlXY(8, 6, 63, 0, 63)
        lp.LedCtrlXY(8, 7, 63, 63, 63)
        lp.LedCtrlXY(8, 8, 0, 0, 0)
        but = lp.ButtonStateXY()
        if but:
            if 127 in but:
                x = but[0]
                y = but[1]
                print(x,y)
                if but == [8,1,127]:
                    r = 48
                    g = 0
                    b = 0
                if but == [8,2,127]:
                    r = 0
                    g = 48
                    b = 0
                if but == [8,3,127]:
                    r = 0
                    g = 0
                    b = 48
                if but == [8,4,127]:
                    r = 48
                    g = 48
                    b = 0
                if but == [8,5,127]:
                    r = 0
                    g = 48
                    b = 48
                if but == [8,6,127]:
                    r = 48
                    g = 0
                    b = 48
                if but == [8,7,127]:
                    r = 48
                    g = 48
                    b = 48
                if but == [8,8,127]:
                    r = 0
                    g = 0
                    b = 0
                if but == [0, 0, 127]:
                    r -= 2
                    if r < 0:
                        r = 48
                if but == [1, 0, 127]:
                    r += 2
                    if r > 48:
                        r = 0
                if but == [2, 0, 127]:
                    g -= 2
                    if g < 0:
                        g = 48
                if but == [3, 0, 127]:
                    g += 2
                    if g > 48:
                        g = 0
                if but == [4, 0, 127]:
                    b -= 2
                    if b < 0:
                        b = 48
                if but == [5, 0, 127]:
                    b += 2
                    if b > 48:
                        b = 0
                if but == [7, 0, 127]:
                    lp.Reset()
                if y != 0 and x != 8:
                    lp.LedCtrlXY(x, y, r, g, b)





if __name__ == '__main__':
    main()
