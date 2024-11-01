'''
The code is correct but just need to add some checks to make sure the input is correct.
'''


def bubble_sort(arr):
    '''
    Check if arr is an array first
    '''
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    '''
    Check if all elements in arr are numbers
    '''
    for i in arr:
        if not isinstance(i, (int, float)):
            raise TypeError("All elements in the list must be numbers")

    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we skip them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
