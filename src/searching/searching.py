def linear_search(arr, target):
    # Your code here
    for i,num in enumerate(arr):
        # if the target is in the ith element,return True
        if num == target:
            return i  

    return -1   # False, if not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Start with the entire sequence of elements.
    low = 0
    high = len(arr) - 1
    # Repeatedly subdivide the sequence in half until the target is found.
    while low <= high :
        # Find the midpoint of the sequence.
        mid = (high + low) // 2
        # Does the midpoint contain the target?
        if arr[mid] == target : 
            return mid
        # Or does the target precede the midpoint? Narrow it down to the lower half of current section
        elif target < arr[mid] : 
            high = mid - 1
        # Or does it follow the midpoint? Narrow it down to the upper half of current section
        else :
            low = mid + 1
    # If the sequence cannot be subdivided further, we're done.
    return -1


"""
# Write an recursive implementation of Binary Search
def binarySearch_recursive(arr, item): 
    if len(arr) == 0 :
        return False 
    else:
        mid = len(arr)//2
        if arr[mid] == item:
            return True 
        else:
            if item < arr[mid]:
                return binarySearch (arr[:mid],item)
            else:
                return binarySearch (arr[mid+1:],item)
test_arr = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(test_arr, 3)) 
print(binarySearch(test_arr, 13))

"""