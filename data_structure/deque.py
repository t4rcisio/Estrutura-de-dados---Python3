class Deque:
    def __init__(self):
        self.__deque = []
        self.__deque_lenght = 0

    def putTop(self, val):
        self.__deque.append(val)
        self.__deque_lenght +=1
    
    def putBotton(self, val):
        
        self.__deque.insert(0,val)
        self.__deque_lenght +=1
    
    def popTop(self):
        if(self.__deque_lenght != 0):
            self.__deque.pop()
            self.__deque_lenght -=1
        else:
            print("Nothing to do. Deque empty")
    
    def popBotton(self):
        if(self.__deque_lenght != 0):
            self.__deque.pop(0)
            self.__deque_lenght -=1
        else:
            print("Nothing to do. Deque empty")

    def top(self):
        return self.__deque[-1]
    
    def botton(self):
        return self.__deque[0]
    
    def lenght(self):
        return self.__deque_lenght
    
    def deque(self):
        return self.__deque



deque = Deque()

for i in range(15):
    deque.putTop(i)
    deque.putBotton(-i)

print(deque.deque())
print(deque.top())
print(deque.botton())

print(deque.lenght())

deque.popBotton()
deque.popTop()

print(deque.deque())
