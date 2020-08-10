# TO-DO: complete the helper function below to merge 2 sorted arrays
import random 
import math

list = []

for _ in range(0,25):
    list.append(random.randint(0,50))

# print(list)

def merge(arrA, arrB):

    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    aIndex = 0
    bIndex = 0
    mergeIndex = 0

    arrB.append(math.inf)
    arrA.append(math.inf)

    while mergeIndex < len(merged_arr):
        if arrA[aIndex] < arrB[bIndex]:
            merged_arr[mergeIndex] = arrA[aIndex]
            mergeIndex += 1
            aIndex += 1
        else:
            merged_arr[mergeIndex] = arrB[bIndex]
            mergeIndex += 1
            bIndex += 1
            
    # Your code here
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    
    if len(arr) > 1:
      lhArr =  merge_sort(arr[0:len(arr)//2])
      rhArr =  merge_sort(arr[len(arr)//2:len(arr)])

      if len(lhArr) > 0 and len(rhArr) > 0:
        arr = merge(lhArr, rhArr)
        
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input



def merge_in_place(arr, start, mid, end):
    # Your code here
  
    while start < mid and mid <= end:
        if arr[start] > arr[mid]:
            arr.insert(start, arr.pop(mid))
            start += 1
            mid += 1
        else:
            start += 1

def merge_sort_in_place(arr, l, r):
    # Your code here
    if abs(l - r) > 1:
        merge_sort_in_place(arr, l, (l+r) //2)
        merge_sort_in_place(arr, (l+r) //2, r)
        merge_in_place(arr, l, (l+r) //2, r)
    else:
        merge_in_place(arr, l, r, r)
    
