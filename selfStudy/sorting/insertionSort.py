# time complexity is O(n^2)
# space complexity is O(1)
def insertionSort(input)-> list:
    length = len(input)
    i = 1
    while i < length:
        key = input[i]
        j = i-1
        while j >= 0 and input[j] > key:
            input[j+1] = input[j]
            j =j- 1

        input[j+1] = key
        i += 1
    return input

if __name__ == "__main__":
    input = [5,3,4,7,2,1,56,24,43,78,43]
    print(insertionSort(input))
