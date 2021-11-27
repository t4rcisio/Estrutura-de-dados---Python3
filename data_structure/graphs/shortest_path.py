import sys

'''
Shortest path problem

'''


class Graph:
    def __init__(self, nodes):
        self.__matrix =[[] for i in range(nodes)]
        self.__matrix_distances = [[] for i in range(nodes)]
        self.__matrix_way = [[] for i in range(nodes)]
        self.__stack = []
        self.__matrix_lenght = nodes


    def __check(self, a, b):
        return a >= 0 and b>=0 and a < self.__matrix_lenght and b < self.__matrix_lenght 

    def push(self, pointA, pointB, a2b_distance):
        if self.__check(pointA, pointB) and a2b_distance > 0:
            self.__matrix[pointA].append(pointB)
            self.__matrix_distances[pointA].append(a2b_distance)
        else:
            print("Invalid parameters")

    def removeRecurrence(self, val):
        for row in self.__matrix_way:
            if val in row:
                row.remove(val)

    def __showGraph(self):
        for row in self.__matrix_way:
            print(row)

    def __showWayDynamic(self ,index, list, end):
        if len(list) == 0:
            self.__stack.remove(index)
            return
        else:
            for column in list:
                self.__stack.append(column)
                if column != end:
                    self.__showWayDynamic(column, self.__matrix_way[column], end)
                else:
                    return True
    
    def __showWay(self, begin, end):
        list = self.__matrix_way[begin]
        self.__stack.append(begin)
        self.__showWayDynamic(begin, list, end)


    def bestWay(self, begin, end):
        less = begin
        self.__queue = [sys.maxsize for i in range(self.__matrix_lenght)]
        self.__queue[less] = 0

        index = 0

        while(1):
            index = 0
            for i in self.__matrix[less]:
                #print(self.__queue)
                distance = self.__matrix_distances[less]
                if self.__queue[i] > distance[index] + self.__queue[less]:
                    self.__queue[i] = distance[index] + self.__queue[less]
                    self.removeRecurrence(i)# Se um camnho menor for encontrado, o atual é removido 
                    self.__matrix_way[less].append(i) # O melhor caminho é inserido na tabela
                index +=1


            min = sys.maxsize
            self.__queue[less] = 0
            #print(self.__queue)
            for i in range(len(self.__queue)):
                if self.__queue[i] < min and self.__queue[i] > 0:
                    min = self.__queue[i]
                    less = i

            if min == sys.maxsize:
                print("Way doesn't exist")
                break

            if(less == end):
                self.__showWay(begin, end) #Build way
                if len(self.__stack) > 0:
                    print("Distance: ", self.__queue[less])
                    print("Way: ", self.__stack)


    
    def show(self):
        index = 0
        for row in self.__matrix:
            print("-------------------------------")
            print(index, "\t : ", row)
            print("Distances: ", self.__matrix_distances[index])
            index +=1
        print('') 


matrix = Graph(5)
matrix.push(0,3,3)
matrix.push(0,4,10)
matrix.push(1,2,5)
matrix.push(2,4,1)
matrix.push(3,2,2)
matrix.push(3,4,6)

matrix.bestWay(0,1)



print()