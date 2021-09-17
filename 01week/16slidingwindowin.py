# in this we will be implementing the sliding window protocol
#TODO: find the maximum sum for the given consecutive elements in the array
# this is using list slicing for getting the sum of the given array#another method uses list elements to get the highest sum

def sliding_window(arr, window_size):
    if(window_size >= len(arr)): return sum(arr)
    max_sum = 0
    for i in range(0,len(arr)):
        crr_sum = sum(arr[i:i+window_size])
        if(crr_sum > max_sum):
            max_sum = crr_sum
    return max_sum
        


arr=[1,2,4,5,3,1,2,4]
print(sliding_window(arr,3))
