import heapq

class Person:
    def __init__(self, name, priority):
        self.__name = name
        self.__priority = priority

    
    def getName(self):
        return self.__name
    
    def getPriority(self):
        return self.__priority
    
    def __repr__(self):
        return self.__name
    

class PriorityQueue:
    def __init__(self):
        self.__queue = []
        self.__index = 0

    
    def push(self, person):
        ## if priority is negative, generated a max heap, if positive, generate a min heap 
        heapq.heappush(self.__queue,(person.getPriority(), self.__index, person))
        self.__index +=1

    def pop(self):
        return heapq.heappop(self.__queue)[-1]


queue = PriorityQueue()

person = Person("Tarcisio", 20)
queue.push(person)

person = Person("Pedro", 16)
queue.push(person)

person = Person("João", 25)
queue.push(person)

person = Person("Maria", 20)
queue.push(person)

print(queue.pop())
