
class Graph:
    def __init__(self, vertices):
        if(vertices > 0):
            self.__vertices  = vertices
            self.__matrix = [[0 for i in range(vertices)] for i in range(vertices)]

    def __coordinateVerify(self, row, column):
        return (row >= 0 and column >=0 and row < self.__vertices and column < self.__vertices)
    
    def push(self, row, column):
        if self.__coordinateVerify(row,column):
            self.__matrix[row][column] = 1
            self.__matrix[column][row] = 1
        else:
            print("Invalid line or column paramers")

    def show(self):
        print('')
        for row in self.__matrix:
            for column in row:
                print("%d " % column, end=" ")
            print('')

    def pop(self, row, column):
        if self.__coordinateVerify(row,column):
            self.__matrix[row][column] = 0
            self.__matrix[column][row] = 0
        else:
            print("Invalid line or column paramers")
        
    def hasCorner(self, row, column):
        if self.__coordinateVerify(row, column):
            return self.__matrix[row][column] == 1
        else:
            return False


matrix = Graph(5)

matrix.show()


matrix.push(1,3)
matrix.push(3,4)
matrix.push(2,3)

matrix.show()

print(matrix.hasCorner(3,4))
print(matrix.hasCorner(1,2))