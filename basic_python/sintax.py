"""
comments

"""

#list
list = [1, 3.14, "joão"]
#mutable

#tuple
tupla = (1,3,6)
#unmutable

#Strings aren't mutablebe 
name = "tarcisio"

# name[0] = "T" - error

#dictionary
dic = {'name': "tarcsio", 'age': 21}

print(len(dic))

#Loops
for chave in dic:
    print(dic[chave])

num = 11

if (num % 2 == 0):
    print("Even number")
    
else:
    print("Odd number")


while( num < 20):
    print(num)
    num += 1


#functions

def is_even (number):
    return (number % 2 == 0)


print(is_even(15))
print(is_even(8))

list = [1,3,5,9,4,15,33,7,88]

for i in range(len(list)):
    print(list[i])

for i in range(10): # Range function generate a list of 0...n-1
    print(i)

for i in range(1,10): # 1 to 10-1
    print(i)

for i in range(0,10,2): # step 2
    print(i)

#Classes
class Person: 
    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

person1 = Person("Tarcisio", 21)
person2 = Person("João", 32)
person3 = Person("Maria", 15)
person4 = Person("Carlos", 45)

people = []

people.append(person1)
people.append(person2)
people.append(person3)
people.append(person4)

for person in people:
    print("Name: %s" % person.getName())
    print("Age: %d" % person.getAge())

#Generating even numbers
even = [num for num in range(101) if (num%2 == 0)]
print(even)