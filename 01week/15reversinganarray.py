# this is the program for reversing an aray

def reverseit(arr):
    low =0
    high = len(arr)-1
    while(low<high):
        temp = arr[low]
        arr[low]= arr[high]

        arr[high]= temp

        low+=1
        high-=1
        
    return arr

arr= [1,2]

print(reverseit(arr))


# time complexity = O(N)
