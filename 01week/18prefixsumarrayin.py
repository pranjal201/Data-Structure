# This is  a prefix sum array problem
# [10, 20, 10, 30, 40]
# [10, 30, 40, 70, 110]

def prefix_sum(arr):
    arr_sum=[]
    if(len(arr)<=1):
        arr_sum = arr.copy()
        return arr_sum
    arr_sum.append(arr[0])
    for i in range(1,len(arr)):
        arr_sum.append(arr[i] + arr_sum[i-1])
    
    return arr_sum

    

arr = [10,20,30,40,50]
print(prefix_sum(arr))
