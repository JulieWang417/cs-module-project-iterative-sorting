# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # Iterate through array
    
    for i in range(0, len(arr)-1):
        # Find the minimum element in remaining  
        # unsorted array
        min_index = i
        # Iterate from 'i'+1 to end of array
        for j in range(i+1, len(arr)):
            #Set min-index to 'j' if less than index-'i'
            if (arr[j] < arr[min_index]):
                min_index = j
        # Swap the found minimum element with the first element 
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # Iterate through array
    n = len(arr)
    # Perform n-1 bubble operations on the sequence, Traverse through all array elements
    for i in range(n - 1) : # range(n) also work but outer loop will repeat one time more than needed. 
        # Bubble the largest item to the end.
        for j in range(0, n-i-1): # Last i elements are already in place 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here
    # Handle edge cases (empty arrays and negative numbers)
    if len(arr) < 1:
        return arr
    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"
    # Create count array and hold each number's count
    count = [0 for _ in range(max(arr)+1)]
    for i in arr:
        count[i] += 1
    print(count)
    # Have count array store total counts up to each index
    total = 0
    for i in range(len(count)):
        count[i], total = (total, count[i]+total)
    print(count)
    # Set out array in order by each number's value in the count array
    arr_out = [0]*len(arr)
    for i in arr:
        arr_out[count[i]] = i
        count[i] += 1

    return arr

"""
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index] 
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
            alist[position]=currentvalue
"""