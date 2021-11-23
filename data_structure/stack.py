class Stack:
    def __init__(self):
        self.__stack = []
        self.__size = 0  # Store size of stack

    def push(self, val): # Add a new element on stack top
        self.__stack.append(val)
        self.__size += 1

    def pop(self):       # Remove top element from stack
        if (self.__size != 0):
            self.__stack.pop(self.__size-1)
            self.__size -=1
        else:
            print("Nothing to remove. Stack is empty")

    def top(self):      # Return stack top
        return self.__stack[-1]

    def stack(self):    # Return full stack
        return self.__stack

    def lenght(self):   # Return stack lenght
        return self.__size


stack = Stack()
stack.pop()
print("Size = %d" % stack.lenght())
stack.push(10)
stack.push(15)
print(stack.stack())
stack.push(9)
stack.push(12)
print("Size = %d" % stack.lenght())
print(stack.top())
stack.push(24)
print(stack.stack())
stack.pop()
print("Size = %d" % stack.lenght())
print(stack.stack())
print(stack.top())
