class Node:
    def __init__(self, label):
        self.__label = label
        self.__next = None
        self.__before = None

    def setLabel(self, label):
        self.__label = label
    
    def getLabel(self):
        return self.__label
    
    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next
    
    def setBefore(self, before):
        self.__before = before
        
    def getBefore(self):
        return self.__before


class Linked_list:
    def __init__(self):
        self.__head = None
        self.__botton = None
        self.__list_lenght = 0

    def putNode(self, node):# Sequential insertion node
        if(self.__head == None): # Root of list
            self.__head = node
            self.__botton = node
            self.__list_lenght +=1
        else:# Next element
            node.setBefore(self.__botton) # set the reference to before node on new node
            self.__botton.setNext(node) #set on actual botton node, the referento to next
            self.__botton = node 
            self.__list_lenght +=1
    
    def putIndex(self, node, index):
        if(index == self.__list_lenght + 1):
            self.putNode(node)
        elif(index == 0):
            self.__head.setBefore(node)
            node.setNext(self.__head)
            self.__head = node
            self.__list_lenght +=1
        elif(index > 0 and index <= self.__list_lenght):
            current_node = self.__head
            for i in range(index+1):
                s_node = current_node
                current_node = current_node.getNext()
                                                # A < - > B < - > C      put (D)
            s_node.getBefore().setNext(node)    # Change the A reference 'next' B to  D
            node.setBefore(s_node.getBefore())  # Set A reference 'before' on D
            s_node.setBefore(node)              # Change reference 'before' on B, assingn D 
            node.setNext(s_node)                # Set 'netx' reference B on D'
            self.__list_lenght +=1
        else:
            print("Invalid index [%d]" % index)

    def popBotton(self):
        if(self.__list_lenght > 0):
            self.__botton.setBefore(None)
            self.__list_lenght -=1
        else:
            print("Empty list. Nothing to do")

    def popIndex(self, index):
        if(index == self.__list_lenght):
            self.popBotton()
        if(index == 0):
            self.__head.getNext().setBefore(None)
            self.__head = self.__head.getNext()
            self.__list_lenght -=1
        elif(index > 0 and index < self.__list_lenght):
            current_node = self.__head
            for i in range(index+1):
                s_node = current_node
                current_node = current_node.getNext()
            
            s_node.getBefore().setNext(s_node.getNext())
            s_node.getNext().setBefore(s_node.getBefore())
            self.__list_lenght -=1
    
    def printList(self):
        current_node = self.__head
        for i in range(self.__list_lenght):
                print("Node: %d" % i)
                print("Label: %s" % current_node.getLabel())
                current_node = current_node.getNext()




tree = Linked_list()
node = Node("tarcisio")
tree.putNode(node)
node = Node("João")
tree.putNode(node)
node = Node("Maria")
tree.putNode(node)
tree.printList()

print("1----------------------")
node = Node("Pedro")
tree.putIndex(node,1)
tree.printList()

print("2----------------------")
tree.popIndex(1)
tree.printList()

print("3----------------------")
node = Node("Ana")
tree.putIndex(node,0)
tree.printList()

print("4----------------------")
tree.popIndex(0)
tree.printList()