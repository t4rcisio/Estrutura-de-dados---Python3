#Functional programming

#Lambda functions

def pow(num): 
    return num ** 2

pow_  = lambda num: num**2

print (pow_(10))


fat_ = lambda num: num * fat_(num - 1) if num > 1 else 1
print(fat_(5))


#Map
#execute a algorithm on all membrer of a list

list = [10,20,30]

new_List = map(lambda number:fat_(number), list)

for i in new_List:
    print(i)

#Filter

list = filter(lambda number: number%2 == 0, range(11))

for i in list:
    print(i)

