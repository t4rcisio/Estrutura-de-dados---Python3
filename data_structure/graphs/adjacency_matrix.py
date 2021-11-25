
class Graph:
    def __init__(self, vertices):
        if(vertices > 0):
            self.__lenth = vertices
            self.__matrix = [[] for i in range(vertices)]
            self.__stack = []

    def __coordenateVerify(self, row, column):
        return (row>=0 and column >=0 and row < self.__lenth and column < self.__lenth)

    def push(self, row, column):
        if self.__coordenateVerify(row, column):
            if not column in self.__matrix[row]:
                self.__matrix[row].append(column)
            else:
                print("Corner already exist!")
        else:
            print("Invalid row or column parameters")
    
    def pop(self, row, column):
        if  self.__coordenateVerify(row, column):
            if column in self.__matrix[row]:
                self.__matrix[row].remove(column)
            else:
                print("This corner doesn't exist")
        else:
            print("Invalid row or column parameters")
    
    def show(self):
        print('') 
        index = 0
        for row in self.__matrix:
            print('%d: ' % index, end=' ')
            for column in row:
                print("%d " % column, end=' ')
            print('')
            index +=1


    


matrix = Graph(5)
matrix.show()

matrix.push(0,3)
matrix.push(0,4)

matrix.push(1,3)

matrix.push(4,2)

matrix.show()

matrix.pop(4,2)

matrix.show()