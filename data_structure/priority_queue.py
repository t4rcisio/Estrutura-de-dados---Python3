class Person:
    def __init__(self, name, priority):
        self.__name =  name
        self.__priority = priority

    def getName(self):
        return self.__name

    def getPriority(self):
        return self.__priority


class PriorityQueue:
    def __init__(self):
        self.__queue = []
        self.__queue_lenght = 0

    def push(self, person):
        if(self.__queue_lenght == 0):
            self.__queue.append(person)
            self.__queue_lenght +=1
        else:
            index = 0
            for person_queue in self.__queue:
                if(person_queue.getPriority() < person.getPriority()):
                    self.__queue.insert(index, person)
                    self.__queue_lenght +=1
                    index = 0
                    break

                index +=1
            
            if(index!=0):
                self.__queue.append(person)
                self.__queue_lenght +=1

    def pop(self):
        self.__queue.pop(0)
    
    def show(self):
        for person_queue in self.__queue:
            print("%s " % person_queue.getName(), end=" ")               

            
queue = PriorityQueue()

person = Person('tarcisio', 15)
queue.push(person)
person = Person('João', 15)
queue.push(person)
person = Person('Pedro', 22)
queue.push(person)
person = Person('Marcos', 18)
queue.push(person)
person = Person('Anna', 3)
queue.push(person)
person = Person('Bernardo', 45)
queue.push(person)

queue.show()

print("\n")

queue.pop()
queue.pop()

queue.show()