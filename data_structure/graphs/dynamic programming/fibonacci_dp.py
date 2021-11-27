
class Fibonacci:
    def __init__(self):
        self.__mem = []

    def __fib(self, n):
        if (self.__mem[n - 1] != -1):
            return self.__mem[n-1]
        self.__mem[n-1] = self.__fib(n-1) + self.__fib(n-2)
        return self.__mem[n-1]



    def fib(self, index):
        self.__mem = [-1 for i in range(index) ]
        self.__mem[0] = self.__mem[1] = 1
        return self.__fib(index)


fibo = Fibonacci()

print(fibo.fib(40))


