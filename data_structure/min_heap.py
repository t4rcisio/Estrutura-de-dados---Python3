class Node:
    def __init__(self, label):
        self.__label = label
        self.__id    = None
        self.__left  = None
        self.__right = None
        self._above  = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def getLabel(self):
        return self.__label

    def getLeft(self):
        return self.__left
    
    def setLeft(self, node):
        self.__left = node
    
    def getRight(self):
        return self.__right
    
    def setRight(self, node):
        self.__right = node
    
    def getAbove(self):
        return self.__above
    
    def setAbove(self, node):
        self.__above = node


class MinHeap:
    def __init__(self):
        self.__heap = []
        self.__heap_lenght = 0
        self.__head = None
        self.__index = None



    def __insert(self, current_node, node):

        if(current_node.getLeft()  == None):
            node.setId(self.__heap_lenght-1)
            node.setAbove(current_node)
            current_node.setLeft(node)
            self.__heap.append(node)

        elif(current_node.getRight()  == None):
            node.setId(self.__heap_lenght-1)
            node.setAbove(current_node)
            current_node.setRight(node)
            self.__heap.append(node)
        
        else:
            self.__index = (self.__index + 1)
            print("Index = %d" % self.__index )
            self.__insert(self.__heap[self.__index], node)
    


    def push(self, node):
        if(self.__heap_lenght== 0):
            node.setId(0)
            self.__heap.append(node)
            self.__heap_lenght +=1
            self.__head = node
            self.__index = 0
        else:
            self.__insert(self.__heap[self.__index], node)


    def __show(self, node):
        if(node != None):
            print("%d " % node.getLabel(), end= " ")
            self.__show(node.getLeft())
            self.__show(node.getRight())
        

    def show(self):
        self.__show(self.__head)

        
heap = MinHeap()

node = Node(12)
heap.push(node)

node = Node(7)
heap.push(node)

node = Node(6)
heap.push(node)

node = Node(10)
heap.push(node)

node = Node(8)
heap.push(node)

node = Node(20)
heap.push(node)

heap.show()