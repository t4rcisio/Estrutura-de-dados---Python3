class Graph:
    def __init__(self, vertices):
        if(vertices > 0):
            self.__lenth = vertices
            self.__matrix = [[] for i in range(vertices)]
            self.__stack = []
            self.__visited = []

    def __coordenateVerify(self, row, column):
        return (row>=0 and column >=0 and row < self.__lenth and column < self.__lenth)

    def push(self, row, column):
        if self.__coordenateVerify(row, column):
            if not column in self.__matrix[row]:
                self.__matrix[row].append(column)
                #self.__matrix[column].append(row)
            else:
                print("Corner already exist!")
        else:
            print("Invalid row or column parameters")
    
    def pop(self, row, column):
        if  self.__coordenateVerify(row, column):
            if column in self.__matrix[row]:
                self.__matrix[row].remove(column)
                self.__matrix[column].remove(row)
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

    def __showList(self):
        print("Visited: ", self.__visited, "\t\t\tStack: ", self.__stack)
    
    def __visit(self, node):
        row =  self.__matrix[node]

        #row = list(set(row) - set(self.__stack)) 
        #row = list(set(row) - set(self.__visited))

        if(len(row)!= 0 and not node in self.__visited):

            self.__stack = self.__stack + row
            self.__showList() #Print list
            self.__stack.pop(0)
            self.__visited.append(node)
            self.__showList() #Print list
            for item in self.__stack:
                if(not item in self.__visited):
                    self.__visit(item)

            if(len(self.__stack)!=0):
                self.__visit(self.__stack[0])
        else:
            self.__visited.append(self.__stack[0])
            self.__stack.pop(0)
            self.__showList() #Print list
            return 1
            
            


    def visit(self, head):
        if (head < self.__lenth and head >= 0):
            self.__stack.append(head)
            self.__visit(head)
        else:
            print("head invalid")



graph = Graph(5)

graph.push(0,1)
graph.push(0,2)

graph.push(1,3)
graph.push(1,4)

graph.push(3,4)

graph.show()

graph.visit(0)