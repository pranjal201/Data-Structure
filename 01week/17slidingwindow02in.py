# in this we will be implementing the sliding window protocol
#TODO: find the maximum sum for the given consecutive elements in the array
# this is using list slicing for getting the sum of the given array#another method uses list elements to get the highest sum

def sliding_window(arr, window_size):
    if(window_size >= len(arr)): return sum(arr)
    crr_sum = sum(arr[0:window_size])
    max_sum = crr_sum
    i=1
    while(i < len(arr)-window_size):
        crr_sum = (crr_sum + arr[i-1+window_size])-arr[i-1]
        if(crr_sum > max_sum):
            max_sum = crr_sum
        i+=1

    return max_sum

arr=[1,2,4,5,3,1,2,4,8,1]
print(sliding_window(arr,3))
