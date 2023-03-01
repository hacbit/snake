__author__ = 'hacbit'
__doc__ = '''
Copyright (C) 2023- hacbit
'''

from os import system, name
from numpy import sum
from random import randint
from pynput.keyboard import Key, Listener
import curses

class Snake:
    def __init__(self, __level = 3, __placeWidth = 20, __placeHeight = 20):
        self.__level = __level
        self.__time = self.__setLevel()
        self.__snakeDirection = 'r'
        self.__bodyAxis = [[1, 1], [1, 2]]
        self.__placeWidth = __placeWidth
        self.__placeHeight = __placeHeight
        self.__placeData = self.__initPlace()
        self.__snakeDirectionDict = {
                'l':[-1,0],
                'r':[1,0],
                'u':[0,1],
                'd':[0,-1]
            }
        
        
    def __setLevel(self):
        return [0.4, 0.2, 0.1][self.__level-1]

    def __initPlace(self):
        arr = []
        for _ in range(self.__placeHeight + 2):
            arr.append('  ' * self.__placeWidth)
        return arr

    def LoadPlace(self):
        print(' ' + '--'*self.__placeWidth + '-')
        for i in self.__placeData:
            print('| ' + i + '|')
        print(' ' + '--'*self.__placeWidth + '-')
    
    def crawl(self):
        nextAxis = self.__addAxis(self.__bodyAxis[0], 
                                self.__snakeDirection)
        self.__bodyAxis = nextAxis + \
            self.__bodyAxis[:self.getLength()+self.__isEat()-1]

    def putScore(self):
        score = self.getLength()-2
        print('----------GAMEOVER----------')
        print('YOUR SCORE IS ', score, ' pt')

    def __draw(self, sth, axis):
        dic = {'food':'$',
                'obstacle':'#',
                'head':'@',
                'trunk':'*'
            }
        if not self.__isInBody() and sth in dic:
            self.__placeData[axis[0]][axis[1]] = sth[0] + ' '

    def __getRandomAxis(self):
        return [randint(0, self.getWidth()-1),
                randint(0, self.getHeight()-1)]

    def __addAxis(self, axis, direction):
        return sum([axis, direction], axis=0).tolist()

    def __nextStep(self):
        if self.__snakeDirection in self.__snakeDirectionDict:
            return self.__snakeDirectionDict[self.__snakeDirection]
    
    def __isInBody(self, sth):
        return sth in self.__bodyAxis
    
    def __isCollide(self):
        return self.__nextStep() in self.__bodyAxis[1:-1]

    def __isEat(self):
        return self.__placeData[self.__bodyAxis[0][0]]\
                                [self.__bodyAxis[0][1]] == '$'
    
    def getLength(self):
        return len(self.__bodyAxis)
    
    def getHeadAxis(self):
        return self.__bodyAxis[0]

    def getWidth(self):
        return self.__placeWidth

    def getHeight(self):
        return self.__placeHeight

    def Direction_change(self, key):
        return self.__snakeDirectionDict[key]
    
# ===== class Snake end =====


keylist = ['l', 'r', 'u', 'd', 
           'a', 'd', 'w', 's',
           Key.left, Key.right, Key.up, Key.down]
direction = curses.KEY_RIGHT

def CLEAR():
    system('cls' if name == 'nt' else 'clear')

def on_press(key):
    global direction
    if key == 'a' and not direction == curses.KEY_RIGHT:
        direction = curses.KEY_LEFT
    elif key == 'd' and not direction == curses.KEY_LEFT:
        direction = curses.KEY_RIGHT
    elif key == 'w' and not direction == curses.KEY_DOWN:
        direction = curses.KEY_UP
    elif key == 's' and not direction == curses.KEY_UP:
        direction = curses.KEY_DOWN


if __name__ == '__main__':
    screen = curses.initscr()
    curses.curs_set(0)      # hide the cursor
    curses.noecho()         # turn off echo
    curses.filter()         # ignore all character input
    screen.keypad(True)
    screen.addstr(0, 0, "-----WELCOME TO SNAKE-----")
    screen.addstr(1, 0, "using 'W A S D' or '↑ ↓ ← →' to contorl")
    screen.addstr(2, 0, 'press enter to continue ......')
    screen.refresh()
    screen.getstr(3, 0)     # wait before press enter
    screen.addstr(4, 0, 'Now choose your game level (1.EASY  2.MEDIUM  3.HARD)')
    screen.refresh()
    while True:
        k = screen.getch()
        if k == ord('1'):
            screen.addstr(5, 0, 'YOU CHOOSE 1st LEVEL')
            break
        elif k == ord('2'):
            screen.addstr(5, 0, 'YOU CHOOSE 2nd LEVEL')
            break
        elif k == ord('3'):
            screen.addstr(5, 0, 'YOU CHOOSE 3rd LEVEL')
            break
    screen.refresh()
    curses.napms(2000)
    
    # DO SOMETHING
    
    screen.clear()
    screen.addstr(0, 0, '-----GAMEOVER-----')
    screen.addstr(1, 0, 'press any key to exit program')
    screen.refresh()
    screen.keypad(False)
    screen.getch()
    curses.endwin()