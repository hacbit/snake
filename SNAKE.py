__author__ = 'hacbit'
__doc__ = '''
Copyright (C) 2023- hacbit
'''

import curses
from numpy import sum
from random import randint


class Snake:
    def __init__(self):
        self.__snakeAxis = [[3, 6], [3, 4]]
        self.__snakeDirectionDict = {
                curses.KEY_UP:[-1,0],
                curses.KEY_DOWN:[1,0],
                curses.KEY_RIGHT:[0,2],
                curses.KEY_LEFT:[0,-2]
            }
        
    def crawl(self, direction, fln, fclm):
        nextAxis = [self.addAxis(self.__snakeAxis[0], 
                                self.__snakeDirectionDict[direction])]
        self.__snakeAxis = nextAxis + self.__snakeAxis
        if not self.isEat(fln, fclm):
            self.__snakeAxis.pop()

    def addAxis(self, axis, direction):
        return sum([axis, direction], axis=0).tolist()
    
    def isCollide(self, upb, downb, leftb, rightb):
        return self.__snakeAxis[0] in self.__snakeAxis[1:] or \
                self.__snakeAxis[0][0] in [upb, downb] or \
                self.__snakeAxis[0][1] in [leftb, rightb]
    
    def isEat(self, fln, fclm):
        return self.__snakeAxis[0] == [fln, fclm]

    def snakeAxis(self):
        return self.__snakeAxis
    
# ===== class Snake end =====


def getRandomYX(al, ar, bl, br):
    return [randint(al, ar),
            randint(bl, br)*2]

def main(stdscr):
    # stdscr = curses.initscr()
    curses.curs_set(0)      # hide the cursor
    curses.noecho()
    curses.cbreak()
    curses.filter()         # ignore all character input
    stdscr.nodelay(1)
    stdscr.keypad(1)
    stdscr.addstr(0, 0, "--------- WELCOME TO SNAKE ---------")
    stdscr.addstr(1, 0, "using 'W A S D' or '↑ ↓ ← →' to contorl")
    stdscr.addstr(2, 0, 'press ENTER to continue ......')
    stdscr.refresh()
    stdscr.getstr(3, 0)     # wait before press enter
    stdscr.addstr(4, 0, 'Now choose your game level (1.EASY  2.MEDIUM  3.HARD)')
    stdscr.refresh()
    while True:
        k = stdscr.getch()
        if k == ord('1'):
            stdscr.addstr(5, 0, 'YOU CHOOSE 1st LEVEL')
            level = 1
            break
        elif k == ord('2'):
            stdscr.addstr(5, 0, 'YOU CHOOSE 2nd LEVEL')
            level = 2
            break
        elif k == ord('3'):
            stdscr.addstr(5, 0, 'YOU CHOOSE 3rd LEVEL')
            level = 3
            break
    stdscr.refresh()
    curses.napms(1000)
    stdscr.clear()
    stdscr.addstr(0, 0, '--------- LEVEL ' + str(level) + '---------')
    stdscr.addstr(1, 0, "using 'W A S D' or '↑ ↓ ← →' to contorl")
    stdscr.refresh()
    win = curses.newwin(22, 43, 2, 0)
    g = Snake(level)
    if level == 1:
        nap = 200
    elif level == 2:
        nap = 120
    elif level == 3:
        nap = 70
    direction = curses.KEY_RIGHT
    isExistfood = False
    score = 0

    while True:
        win.clear()
        win.border()

        key = stdscr.getch()
        if (key == ord('a') or key == curses.KEY_LEFT) and not direction == curses.KEY_RIGHT:
            direction = curses.KEY_LEFT
        elif (key == ord('d') or key == curses.KEY_RIGHT) and not direction == curses.KEY_LEFT:
            direction = curses.KEY_RIGHT
        elif (key == ord('w') or key == curses.KEY_UP) and not direction == curses.KEY_DOWN:
            direction = curses.KEY_UP
        elif (key == ord('s') or key == curses.KEY_DOWN) and not direction == curses.KEY_UP:
            direction = curses.KEY_DOWN

        snake = g.snakeAxis()
        win.addch(snake[0][0], snake[0][1], '@')
        for node in snake[1:]:
            win.addch(node[0], node[1], '*')

        if not isExistfood:
            isExistfood = True
            foodline, foodcolume = getRandomYX(1, 20, 1, 20)
            if [foodline, foodcolume] in snake:
                continue

        win.addch(foodline, foodcolume, '$')
        win.refresh()

        if g.isCollide(0, 21, 0, 42):
            break
        
        g.crawl(direction=direction, fln=foodline, fclm=foodcolume)
        if g.isEat(fln=foodline, fclm=foodcolume):
            isExistfood = False
            score += 1

        curses.napms(nap)
        
    curses.napms(1000)
    curses.nocbreak()
    stdscr.clear()
    stdscr.nodelay(0)
    stdscr.keypad(0)
    stdscr.addstr(0, 0, '  GGGGGG       A      MM      MM  EEEEEEEEE   OOOOOO   VV       VV EEEEEEEEE RRRRRRRR')
    stdscr.addstr(1, 0, 'GGG    GG     AAA     MMM    MMM  EE         OO    OO  VV       VV EE        RR     RR')
    stdscr.addstr(2, 0, 'GG           A   A    MM M  M MM  EE        OO      OO VV       VV EE        RR     RR')
    stdscr.addstr(3, 0, 'GG   GGGGG  AA   AA   MM  MM  MM  EEEEEEEEE OO      OO  VV     VV  EEEEEEEEE RRRRRRRR')
    stdscr.addstr(4, 0, 'GG     GGG AAAAAAAAA MM   MM   MM EE        OO      OO   VV   VV   EE        RR    RR')
    stdscr.addstr(5, 0, ' GGG  GG G AA     AA MM        MM EE         OO    OO     VV VV    EE        RR     RR')
    stdscr.addstr(6, 0, '  GGGGG  G AA     AA MM        MM EEEEEEEEE   OOOOOO       VVV     EEEEEEEEE RR     RR')

    stdscr.addstr(8, 0, 'YOUR SCORE IS ' + str(score))
    stdscr.addstr(10, 0, 'press ENTER to exit program ......')
    stdscr.refresh()
    stdscr.getch()

if __name__ == '__main__':
    curses.wrapper(main)