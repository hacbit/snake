from os import system
from time import sleep
from numpy import sum
from random import randint
from keyboard import wait
from pynput.keyboard import Key, Listener, GlobalHotKeys


class Snake:
    def __init__(self, __velocity = 3, __placeWidth = 20, __placeHeight = 20):
        self.__velocity = __velocity
        self.__placeData = []
        self.__snakeDirection = 'r'
        self.__bodyAxis = [[1, 1], [1, 2]]
        self.__placeWidth = __placeWidth
        self.__placeHeight = __placeHeight
        self.__snakeDirectionDict = {
                'l':[-1,0],
                'r':[1,0],
                'u':[0,1],
                'd':[0,-1]
            }

    def initPlace(self):
        self.__placeData = []
        for _ in range(self.__placeHeight + 2):
            self.__placeData.append('  ' * self.__placeWidth)

    def LoadPlace(self):
        print(' ' + '--'*self.__placeWidth + '-')
        for i in self.__placeData:
            print('| ' + i + '|')
        print(' ' + '--'*self.__placeWidth + '-', end='')
    
    def crawl(self):
        nextAxis = self.addAxis(self.__bodyAxis[0], 
                                self.__snakeDirection)
        self.__bodyAxis = nextAxis + \
            self.__bodyAxis[:self.getLength()+self.isEat()-1]

    def setGameLevel(self):
        arr = [1, 2, 3, ]

    def putScore(self):
        score = self.getLength()-2
        print('----------GAMEOVER----------')
        print('YOUR SCORE IS ', score, ' pt')

    def draw(self, sth, axis):
        dic = {'food':'$',
                'obstacle':'#',
                'head':'@',
                'trunk':'*'
            }
        if not self.isInBody() and sth in dic:
            self.__placeData[axis[0]][axis[1]] = sth[0] + ' '

    def getRandomAxis(self):
        return [randint(0, self.getWidth()-1),
                randint(0, self.getHeight()-1)]

    def addAxis(self, axis, direction):
        return sum([axis, direction], axis=0).tolist()

    def nextStep(self):
        if self.__snakeDirection in self.__snakeDirectionDict:
            return self.__snakeDirectionDict[self.__snakeDirection]
    
    def isInBody(self, sth):
        return sth in self.__bodyAxis
    
    def isCollide(self):
        return self.nextStep() in self.__bodyAxis[1:-1]

    def isEat(self):
        return self.__placeData[self.__bodyAxis[0][0]]\
                                [self.__bodyAxis[0][1]] == '$'
    

# -*-*-*-*-*-*-api-*-*-*-*-*-
    def getLength(self):
        return len(self.__bodyAxis)
    
    def getHeadAxis(self):
        return self.__bodyAxis[0]

    def getWidth(self):
        return self.__placeWidth

    def getHeight(self):
        return self.__placeHeight

    def Direction_change(self):
        pass


def CLEAR():
    system('cls')

keylist = [Key.left, Key.right, Key.up, Key.down, 
           'a', 'd', 'w', 's']

def on_press(key):
    try:
        if key in keylist or key.char in keylist:
            pass
    except:
        return
    
def on_release(key):
    if key == Key.esc:
        return False

isStop = False
level = 3

def actionAfterHotKey(key):
    ls = ['1st', '2nd', '3rd']
    print('YOU CHOOSE', ls[key-1], 'LEVEL')
    global isStop, level
    isStop = True
    level = key

def put1by1(str, t, end='\n'):
    for i in range(len(str)):
        print(str[:i], end='\r')
        sleep(t)
    print(str, end=end)


if __name__ == '__main__':
    with Listener(on_press=on_press, 
                  on_release=on_release,
                  suppress=True) as listener:

        CLEAR()
        put1by1("-----WELCOME TO SNAKE-----", 0.02)
        put1by1("using 'W A S D' or '↑ ↓ ← →' to contorl", 0.02)
        put1by1('press enter to continue', 0.02, end='\r')
        for i in range(6):
            print('press ENTER to continue', '.'*(i+1), end='\r')
            sleep(0.15)
        wait('enter')

        print('Now choose your game level (1.EASY  2.MEDIUM  3.HARD)')
        with GlobalHotKeys({
            '1': lambda:actionAfterHotKey(1),
            '2': lambda:actionAfterHotKey(2),
            '3': lambda:actionAfterHotKey(3)}) as h:
            while not isStop:
                pass
            h.stop()

        game = Snake(level)
        game.initPlace()
        game.LoadPlace()

        listener.join()