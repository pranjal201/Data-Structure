# arr[] = {4,0,2,0,4}
# are represents the hight of the wall and we have to find the total water that can be trapped in the wall
# if arr[] = {3,4,2} there will be no water retaining inside the wall

tests = []

# TODO: TO CHECK THE PROBLEM IN THE LEFT MAX ARRAY

tests.append([{
    'input': [4,0,3,0,3],
    'output': 6}])

#----------------------Total complexity of O(n*n)
#--------------- TEST CASES--------------- 

def find_max(start, end, arr): #----------complexity of O(n)
    max_val = 0
    for i in range(start, end):
        if(arr[i] > max_val):
            max_val = arr[i]

    return max_val



def trapped_water(arr):

    #to check whether there are elements in the array or not.
    if(len(arr) <= 2): return -1

    total_vol = 0 # these will be returned at last
    iterator= 1 #starting to check from 

    while(iterator<len(arr)-1): #----------------------complexity of O(n)
        left_max = find_max(0, iterator, arr)#----------------------complexity of O(n)
        right_max = find_max(iterator+1, len(arr), arr)#----------------------complexity of O(n)
        
        vol_per_index = min(left_max, right_max) - arr[iterator]
        if(vol_per_index < 0):
            vol_per_index = 0
            total_vol = total_vol + vol_per_index
        else:
            total_vol = total_vol + vol_per_index

        iterator += 1

    return total_vol

print(tests[0][0])
print(trapped_water(tests[0][0]['input']))


