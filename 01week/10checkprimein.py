import math
def isPrime(num):
    for i in range(2,math.ceil(math.sqrt(num))):
        if(num % i == 0): return False

    return True

# O(N.sqrt(N))

def printPrime(n):
    if n<2: return False

    for i in range(2,n+1):
        if isPrime(i):
            print(i)


printPrime(1000000)
