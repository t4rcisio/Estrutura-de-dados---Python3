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

# Select by value
list3.remove(6)
print(list3) 

num = 90
# Verify if value is in list
if num in list3:
    print("%d is in list" % num)
else:
    print("%d not found" % num)