from time import sleep
from random import randint
from os import system
from numpy import sum
from pynput.keyboard import Key, Listener
from keyboard import wait


class Snake:
    def __init__(self, __placeWidth = 20, __placeHeight = 20):
        self.__length = 2
        self.__velocity = 10
        self.__placeData = []
        self.__foodAxis = []
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

    def lengthGrow(self):
        self.__length += 1
    
    def crawl(self):
        pass

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

    def isCollide(self):
        return self.nextStep() in self.__bodyAxis[1:-1]

    def isInBody(self, sth):
        return sth in self.__bodyAxis

    def isEat(self):
        return self.__placeData[self.__bodyAxis[0][0]]\
                                [self.__bodyAxis[0][1]] == '$'

# -*-*-*-*-*-*-api-*-*-*-*-*-
    def getLength(self):
        return self.__length

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

keylist = ['left', 'right', 'up', 'down', 
           'a', 'd', 'w', 's']

def key2direct(k):
    if k.event_type == 'down':
        if k.name in keylist:
            return keylist[keylist.index(k.name) % 4][0]
        else:
            pass
    else:
        pass

def put1by1(str, t, end='\n'):
    for i in range(len(str)):
        print(str[:i], end='\r')
        sleep(t)
    print(str, end=end)


if __name__ == '__main__':
    CLEAR()
    put1by1("-----WELCOME TO SNAKE-----", 0.02)
    put1by1("using 'W A S D' or '↑ ↓ ← →' to contorl", 0.02)
    put1by1('press enter to continue', 0.02, end='\r')
    for i in range(6):
        print('press enter to continue', '.'*(i+1), end='\r')
        sleep(0.15)
    wait('enter')

    game = Snake()
    game.initPlace()
    game.LoadPlace()

