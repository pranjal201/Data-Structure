# implementing the  SEIVE OF ERATOSTHENES
#this is used to find the prime numbers in a given range

# O(log(log(N)))
def seive_of_eratosthenes(n):
    #n is the range upto which we need to print the prime number
    prime = [True for i in range(n+1)]

    p = 2
    while(p**2 <= n):
        if(prime[p] == True):

            for i in range(p**2,n+1,p):
                prime[i] = False
                
        p+=1

    prime[0] = False
    prime[1] = False

    #printing the prime numbers
    for i in range(n+1):
        if prime[i]:
            print(i)



seive_of_eratosthenes(1000000)
print()
