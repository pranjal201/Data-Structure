# Rotatation of an array
#arrsize = 6, d(number of rotation)= 2
#[1,2,3,4,5,6] <input>
#[2,3,4,5,6,1]
#[3,4,5,6,1,2]<output>

# In this we are using the juggling algo approach
# time complexity = O(N) and space commplexity = O(1)
import math

def rotate_array(lists,N,K):
    stop =0
    count = math.gcd(N, K)
    for i in range(0, count):
        temp = lists[i]
        j=i
        while(j+count < N):
            lists[j] = lists[j+count]
            j=j+count
            stop=j



        lists[stop] = temp

    return lists


arr = [1,2,3,4,5,6,7,8,9,10,11,12]

print(rotate_array(arr, len(arr), 3))


