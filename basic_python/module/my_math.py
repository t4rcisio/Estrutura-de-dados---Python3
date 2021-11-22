
fat_ = lambda num : 1 if(num == 1) else (num * fat_(num-1))

fib_ = lambda num: 1 if( num == 1 or num ==2) else (fib_(num -1)+ fib_(num-2))

pow_ = lambda base, expo: 1 if(expo == 0) else ( base * pow_(base, expo - 1)) 

