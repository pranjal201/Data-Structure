# Input:
#     N = 5(size of the array), K = 3(size of the sub_size)
#     arr[] = {1,2,3,4,5}
#     Output: 3 2 1 5 4

def reverseit(arr, size, sub_size):
    if(sub_size == 1):
        return arr 
# ^^^^^because each element will be an individual sub_size hence the array will be same

# ^^^^^^^^^their will be CEIL(len(arr)/sub_size) - sub array's

    i =0
    while(i<size):
        left = i
        right = min(i+sub_size-1,size-1)

        while(left < right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        i += sub_size
            
    return arr

if __name__ == "__main__":

    arr1 =[1,2,3,4,5,6,7,8,9,10,11,12]
    arr2 =[1,4,6,7,8]
    arr3 =[1,2,3,4,5,11,12]
    print(reverseit(arr1, len(arr1),3))
    print(reverseit(arr2, len(arr2),2))
    print(reverseit(arr3, len(arr3),3))
    

