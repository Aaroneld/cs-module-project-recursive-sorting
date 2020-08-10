# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    if end < start:
        return -1

    middle = (start + end) // 2

    if arr[middle] == target:
        return middle
    
    elif (target < arr[middle]):
        return binary_search(arr, target, start, middle -1)
    else: 
        return binary_search(arr, target, middle + 1, end)

list = [1,2,3,4]
print(binary_search(list, 2, 0, 3))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

    start = 0
    end = len(arr) - 1
    middle = None

    ascending = True if arr[start] < arr[end] else False

    middle = len(arr) // 2

    while start != end:

        if arr[middle] == target:
            return middle

        if(target < arr[middle]):
            if ascending:
                end = middle
                middle = len(arr[start:end]) // 2
            else:
                start = middle + 1
                middle = (start + end) // 2
        else:
            if ascending:
                start = middle + 1
                middle = (start + end) // 2
            else:
                end = middle
                middle = len(arr[start:end]) // 2
       
    return -1
