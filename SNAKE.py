from time import sleep
from random import randint
from os import system
from numpy import sum
import keyboard


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
        print('--'*self.__placeWidth + '---')
        for i in self.__placeData:
            print('| ' + i + '|')
        print('--'*self.__placeWidth + '---', end='')

    def lengthGrow(self):
        self.__length += 1
    
    def crawl(self):
        pass

    def putScore(self):
        score = self.getLength()-2
        print('----------GAMEOVER----------')
        print('YOUR SCORE IS ', score, ' pt')

    def set_food0rObstacle(self, sth):
        dic = {'food':'$',
                'obstacle':'#'
            }
        self.__foodAxis = [randint(0, self.getWidth()-1),
                randint(0, self.getHeight()-1)]
        if not self.isInBody() and sth in dic:
            self.__placeData[self.__foodAxis[0]][self.__foodAxis[1]] = sth[0] + ' '

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
        return self.__bodyAxis[0] == self.__foodAxis

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

def key2direct(k):
    if k.event_type == 'down':
        if k.name == 'left' or k.name == 'a':
            return 'l'
        elif k.name == 'right' or k.name == 'd':
            return 'r'
        elif k.name == 'up' or k.name == 'w':
            return 'u'
        elif k.name == 'down' or k.name == 's':
            return 'd'
        else:
            pass
    else:
        pass



if __name__ == '__main__':
    print("-----WELCOME TO SNAKE-----")
    print("using 'W A S D' or '↑ ↓ ← →' to contorl")
    for i in range(60):
        print('press ENTER to continue', '.'*(i%6 + 1), '     \r', end='')
        sleep(0.2)
        
    
    
    game = Snake()

    
