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
    stdscr = curses.initscr()
    curses.curs_set(0)      # hide the cursor
    curses.noecho()         # turn off echo
    curses.filter()         # ignore all character input
    stdscr.keypad(True)
    stdscr.addstr(0, 0, "--------- WELCOME TO SNAKE ---------")
    stdscr.addstr(1, 0, "using 'W A S D' or '↑ ↓ ← →' to contorl")
    stdscr.addstr(2, 0, 'press enter to continue ......')
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
    curses.napms(2000)
    stdscr.clear()
    stdscr.addstr(0, 0, '--------- LEVEL ' + str(level) + '---------')
    stdscr.addstr(1, 0, "using 'W A S D' or '↑ ↓ ← →' to contorl")
    stdscr.refresh()
    '''
    set the interface to fit the window size
    it better to leave a size of 20 by 40
    '''
    height, width = stdscr.getmaxyx()
    if height*2 <= width:
        win = curses.newwin(height-2, (height-2)*2, 2, 0)
    else:
        win = curses.newwin(width//2-1, (width//2-1)*2, 2, 0)
    win.border()
    win.refresh()

    listener = Listener(on_press=on_press)
    listener.start()
    g = Snake(level)
    
    win.addch(8, 8, '$')
    win.refresh()
    curses.napms(3000)
    listener.stop()

    stdscr.clear()
    stdscr.addstr(0, 0, '--------- GAMEOVER ---------')
    stdscr.addstr(1, 0, 'press any key to exit program')
    stdscr.refresh()
    stdscr.keypad(False)
    stdscr.getch()
    curses.endwin()