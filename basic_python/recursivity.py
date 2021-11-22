#factorial

fat_ = lambda num : num * fat_(num - 1) if (num> 1) else 1

print(fat_(50))


#Fibonacci

def fib (n):
    if( n == 1 or n == 2 ):
        return 1
    else:
        return fib(n-1) + fib(n-2)

print("Fibonacci[10] = %d" % fib(10))

fib_ = lambda num:  1 if (num == 1 or num ==2) else (fib_(num -1) + fib_(num-2))

print("Fibonacci[12] = %d" % fib_(12))


#Pow

def pow(base, expo):
    if(expo == 0):
        return 1
    else:
       return  base * pow(base, expo- 1)

print("9^6 = %d" % pow(9,6))
    
