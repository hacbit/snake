import time
import random

class Snake:
    def __init__(self, __velocity, __bodyAxis = [[1, 1], [1, 2]]):
        self.__length = 2
        self.__nextSteAxis = 'r'
        self.__bodyAxis = [[1, 1], [1, 2]]
        self.__velocity = __velocity

    def isCollide(self):
        return self.__nextSteAxis in self.__bodyAxis[1:-1]
    
    def crawl(self):
        pass

    def eat(self):
        pass

    def score(self):
        print("Score: ", self.__length - 2, end='')


class Place:
    def __init__(self, __placeWidth = 20, __placeHeight = 20):
        self.__placeWidth = __placeWidth
        self.__placeHeight = __placeHeight
        self.__placeData = []

    def initPlace(self):
        for _ in range(self.__placeHeight + 2):
            self.__placeData.append('  ' * self.__placeWidth)

    def LoadPlace(self):
        # print wall
        print('--'*self.__placeWidth + '---')
        # print gamePlace
        for i in self.__placeData:
            print('| ' + i + '|')
        
        print('--'*self.__placeWidth + '---')

    

if __name__ == '__main__':
    snake = Snake(1)
    p = Place()
    p.initPlace()
    p.LoadPlace()
