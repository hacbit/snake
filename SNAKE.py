import time
import random


class Snake:
    def __init__(self, __velocity):
        self.__length = 2
        self.__nextSteAxis = 'r'
        self.__bodyAxis = [[1, 1], [1, 2]]
        self.__velocity = __velocity

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
        for _ in range(self.__placeHeight + 2):
            self.__placeData.append('  ' * self.__placeWidth)

    def LoadPlace(self):
        # print wall
        print('--'*self.__placeWidth + '---')
        # print gamePlace
        for i in self.__placeData:
            print('| ' + i + '|')
        
        print('--'*self.__placeWidth + '---')

    def setSth(self, axis, sth):
        self.__placeData[axis[0]][axis[1]] = sth[0] + ' '

    def getWidth(self):
        return self.__placeWidth

    def getHeight(self):
        return self.__placeHeight


class Game(Snake, Place):
    def __init__(self):
        self.__foodAxis = [5, 5]

    def __setRandomAxis(self):
        axis = []
        axis.append(random.randint(0, self.getWidth-1),
                    random.randint(0, self.getHeight-1))
        return axis

    def put(self, sth):
        dic = {'food':'$',
            'obstacle':'#'}
        axis = self.__setRandomAxis
        if not self.isInBody and sth in dic:
            self.setSth(axis, dic[sth])


if __name__ == '__main__':
    snake = Snake(1)
    p = Place()


