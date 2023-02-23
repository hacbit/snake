import time
import random
import os


class Snake:
    def __init__(self):
        self.__length = 2
        self.__nextSteAxis = 'r'
        self.__bodyAxis = [[1, 1], [1, 2]]
        #self.__velocity = __velocity

    def isCollide(self):
        return self.__nextSteAxis in self.__bodyAxis[1:-1]

    def isInBody(self, sth):
        return sth in self.__bodyAxis
    
    def crawl(self):
        pass

    def lengthGrow(self):
        self.__length += 1

    def getLength(self):
        return self.__length

    def getHeadAxis(self):
        return self.__bodyAxis[0]


class Place:
    def __init__(self, __placeWidth = 20, __placeHeight = 20):
        self.__placeWidth = __placeWidth
        self.__placeHeight = __placeHeight
        self.__placeData = []

    def initPlace(self):
        self.__placeData = []
        for _ in range(self.__placeHeight + 2):
            self.__placeData.append('  ' * self.__placeWidth)

    def LoadPlace(self):
        # print wall
        print('--'*self.__placeWidth + '---')
        # print gamePlace
        for i in self.__placeData:
            print('| ' + i + '|')
        
        print('--'*self.__placeWidth + '---', end='')

    def setSth(self, axis, sth):
        self.__placeData[axis[0]][axis[1]] = sth[0] + ' '

    def getWidth(self):
        return self.__placeWidth

    def getHeight(self):
        return self.__placeHeight

# -*-*-*-*-*-

def setRandomAxis(place):
    return [random.randint(0, place.getWidth()-1),
            random.randint(0, place.getHeight()-1)]

def set_food0rObsta(self, snake, ch):
    dic = {'food':'$',
        'obstacle':'#'}
    axis = setRandomAxis()
    if not snake.isInBody() and ch in dic:
        snake.setSth(axis, dic[ch])

def putScore(snake):
    score = snake.getLength()-2
    print('----------GAMEOVER----------')
    print('YOUR SCORE IS ', score, ' pt')

def CLEAR():
    os.system('cls')


if __name__ == '__main__':
    p = Place()
    s = Snake()

    #print(s.getLength())
    #print(setRandomAxis(p))
