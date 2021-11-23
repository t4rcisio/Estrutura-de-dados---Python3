from threading import Thread
import time 


fat_ = lambda num : 1 if(num == 1) else (num * fat_(num-1))

fib_ = lambda num: 1 if( num == 1 or num ==2) else (fib_(num -1)+ fib_(num-2))

pow_ = lambda base, expo: 1 if(expo == 0) else ( base * pow_(base, expo - 1))


def mmany_math(i):
    print("Starting thread %d" % i)
    val = i * 10
    print(fat_(val))
    print(fib_(val))
    print(pow_(val, val))
    print("End of thread %d" % i)

for i in range(5):
    process = Thread(target = mmany_math, args=(i,))
    process.start()
