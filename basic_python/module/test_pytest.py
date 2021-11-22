
#install pytest
#Write your functons
#By deafult the file must be named test_*.py, where * is anything 

fat_ = lambda num : 1 if(num == 1) else (num * fat_(num-1))

fib_ = lambda num: 1 if( num == 1 or num ==2) else (fib_(num -1)+ fib_(num-2))

pow_ = lambda base, expo: 1 if(expo == 0) else ( base * pow_(base, expo - 1))


# The functions must flow the same rule from file name 

def test_fat_():
    asset f(0) = 1

# To execte the test, get the pytest from source file location.
# On windows, is on 