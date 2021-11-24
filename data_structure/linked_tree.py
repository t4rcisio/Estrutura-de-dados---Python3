class Node:
    def __init__(self, label):
        self.__label = label
        self.__left  = None
        self.__right = None
        self.__above = None

    def setLabel(self, label):
        self.__label = label
    
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


class Tree:
    def __init__(self):
        self.__head = None
        self.__lenght_tree = 0
        self.__lower_node = None

    def __push(self, current_node, node):
        if(current_node.getLabel() < node.getLabel()):
            if(current_node.getRight() == None):
                node.setAbove(current_node)
                current_node.setRight(node)
                self.__lenght_tree +=1
            else:
                self.__push(current_node.getRight(), node)

        elif(current_node.getLabel() > node.getLabel()):
            if(current_node.getLeft() == None):
                node.setAbove(current_node)
                current_node.setLeft(node)
                self.__lenght_tree +=1
            else:
                self.__push(current_node.getLeft(), node)
        
        else:
            print("This node already exist!")

    def put(self, node): # Insert  a new node
        if(self.__head == None):
            self.__head = node
            self.__lenght_tree +=1
        else:
            self.__push(self.__head, node)


    def __findNode(self, current_node, node):
        if(current_node.getLabel() == node.getLabel()):
            return (True, current_node)

        elif(current_node.getLabel() < node.getLabel()):
            if(current_node.getRight() == None):
                return (False, None)
            else:
                return self.__findNode(current_node.getRight(), node)

        elif(current_node.getLabel() > node.getLabel()):
            if(current_node.getLeft() == None):
                return (False, None)
            else:
                return self.__findNode(current_node.getLeft(), node)

    
    def find(self, node):
        data =  self.__findNode(self.__head, node)
        return data[0]

    def __show(self, node):
        if(node != None):
            print("%d " % node.getLabel(), end=' ' )
            self.__show(node.getLeft())
            self.__show(node.getRight())
    
    def show(self):
            self.__show(self.__head)


    def __lower(self, node, lower_node):
        if(node != None):
            if(node.getLabel() <= lower_node.getLabel()):
                lower_node = node
                self.__lower_node = lower_node

            self.__lower(node.getLeft(), lower_node)
            self.__lower(node.getRight(), lower_node)
    
    def pop(self, node):
        data =  self.__findNode(self.__head, node)
        current_node = data[-1]
        if(current_node.getLeft() == None and current_node.getRight() == None):
            above_node = current_node.getAbove()
            self.__lenght_tree -=1
            if(above_node.getLabel() > current_node.getLabel()):
                above_node.setLeft(None)
            else:
                above_node.setRight(None)
        
        elif(current_node.getLeft() != None and current_node.getRight() == None):
            above_node = current_node.getAbove()
            left_node = current_node.getLeft()
            left_node.setAbove(above_node)
            self.__lenght_tree -=1
            if(above_node.getLabel() > current_node.getLabel()):
                above_node.setLeft(left_node)
            else:
                above_node.setRight(left_node)

        elif(current_node.getLeft() == None and current_node.getRight() != None):
            above_node = current_node.getAbove()
            right_node = current_node.getRight()
            right_node.setAbove(above_node)
            self.__lenght_tree -=1
            if(above_node.getLabel() > current_node.getLabel()):
                above_node.setLeft(right_node)
            else:
                above_node.setRight(right_node)
        
        elif(current_node.getLeft() != None and current_node.getRight() != None):
                lower_node = current_node.getRight()
                self.__lower(lower_node, lower_node)
                lower_node = self.__lower_node
                self.__lenght_tree -=1
                if(current_node.getLabel() != self.__head.getLabel()):
                    above_node = current_node.getAbove()
                    above_node_lower = lower_node.getAbove()
                    above_node_lower.setLeft(None)

                    lower_node.setAbove(above_node)
                    if(above_node.getLabel() > lower_node.getLabel()):
                        above_node.setLeft(lower_node)
                    else:
                        above_node.setRight(lower_node)
                    
                    lower_node.setLeft(current_node.getLeft())
                    lower_node.setRight(current_node.getRight())
                else:
                    left_node = current_node.getLeft()
                    left_node.setAbove(lower_node)
                    lower_node.setAbove(None)
                    lower_node.setLeft(left_node)
                    self.__head = lower_node


                

                

        


tree = Tree()
node = Node(10)
tree.put(node)

node = Node(15)
tree.put(node)

node = Node(5)
tree.put(node)

node = Node(20)
tree.put(node)

node = Node(4)
tree.put(node)

node = Node(8)
tree.put(node)

node = Node(25)
tree.put(node)

node = Node(26)
tree.put(node)

node = Node(22)
tree.put(node)

node = Node(19)
tree.put(node)

tree.show()

node = Node(10)
tree.pop(node)
print("\n")
tree.show()