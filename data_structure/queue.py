class Queue:
    def __init__(self):
        self.__queue = []
        self.__queue_lenght = 0
    
    def put(self, val):
        self.__queue.append(val)
        self.__queue_lenght +=1
    
    def pop(self):
        if(self.__queue_lenght != 0):
            self.__queue.pop(0)
            self.__queue_lenght -=1
        else:
            print("Nothing to do. Queue empty")
    
    def lenght(self):
        return self.__queue_lenght
    
    def botton(self):
        return self.__queue[0]

    def top(self):
        return self.__queue[-1]


queue = Queue()
queue.pop()
queue.put(5)
print(queue.lenght())
print(queue.botton())
queue.put(9)
queue.pop()
queue.put(15)
queue.put(8)
print(queue.lenght())
print(queue.botton())
print(queue.top())