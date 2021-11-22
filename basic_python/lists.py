
#lists 

list1 = [num for num in range(10) if num%2 == 0]
list2 = [num for num in range(10,30) if num%3 == 0]

list3 = list1+ list2
print(list3)

# Select by index 
#remove element from list
list3.pop(4)
print(list3)

#Removing last elemment 
list3.pop(len(list3) - 1)
print(list3)

# Add a new element
#In last position

list3.append(5)
print(list3)

#In expecific position
#     (position, value)
list3.insert(10,0)
print(list3)

# Select by value
list3.remove(6)
print(list3) 

num = 90
# Verify if value is in list
if num in list3:
    print("%d is in list" % num)
else:
    print("%d not found" % num)

# Convert list to Tuple
l_tuple = tuple(list3)
print(type(l_tuple))

#Ordene the list
list3.sort()
print(list3)

#Get a last element
print(list3[-1])

#Get a interval from list
#[start, end-1]
sub_list = list3[4:8]
print(sub_list)

#invert a list 
inverted_list = list3[::-1]
print(inverted_list)

#Unpacking lists
list4 = sub_list
a, b, c, d  = list4
print(list4)
print(a)
print(b)
print(c)
print(d)

#Returnin n values from a frunction

def pow(a, b):
    return a**2, b**2

print(pow(10,15))

a, b = pow(10,15)

print(a)
print(b)

#Defaul parameters


def pow(a, b = 5):
    return a**2, b**2

print(pow(10))

a, b = pow(10)

print(a)
print(b)


import random
# return a value from 0 to n-1
print(random.randrange(5))

#This function include the limtis of range
print(random.randint(5,15))

#select random element from list
print(random.choice(list4))

#Shuffle the list
print(list4)
random.shuffle(list4)
print(list4)

#Get a random sequence from list
#(source, size)
print(random.sample(list4,3))

#Generating a float number
# range 0 to 1
print(random.random())

#define the interval
print(random.uniform(5,10))

