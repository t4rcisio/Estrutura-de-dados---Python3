from collections import defaultdict

class Product:
    def __init__(self, weight, value):
        self.__weight = weight
        self.__value = value

    def getValue(self):
        return self.__value

    def getWeight(self):
        return self.__weight

class Knapsack:
    def __init__(self):
        self.__graph = defaultdict(list)
        self.__index = 0
            
    def pushObject(self, object):
        self.__graph[object.getWeight()/object.getValue()] = object

    def show(self):
        for row in self.__graph:
            print( row, end=' ')
        print('')


teste = Knapsack()

p1 = Product(1,10)

teste.pushObject(p1)

teste.show()
