import numpy as np


def count_inversions(array):
    # Handle base case
    n = len(array)
    if n == 1:
        return array, 0

    # Split the array
    array1 = array[:n/2]
    array2 = array[n/2:]

    # Sort both sides with recursive calls
    sorted_array1, inv1 = count_inversions(array1)
    sorted_array2, inv2 = count_inversions(array2)

    # Merge while counting inversions
    sorted_array = np.empty(n)
    i, j = 0, 0
    inv = 0
    while i < n/2 and j < n-n/2:
        # If we already finished array 1, insert from array 2
        if i == n/2:
            sorted_array[i + j] = sorted_array2[j]
            j += 1

        # If we already finished array 2, insert from array 1
        elif j == n-n/2:
            sorted_array[i + j] = sorted_array1[i]
            i += 1

        # If both arrays are not yet finished, compare current values
        else:
            if sorted_array1[i] < sorted_array[j]:
                sorted_array[i + j] = sorted_array1[i]
                i += 1
            else:
                sorted_array[i + j] = sorted_array2[j]
                j += 1
                # Count inversions
                inv += n/2 - i

    # Return sorted array and the sum of inversions in array 1, array 2
    # and split inversions
    return sorted_array, inv + inv1 + inv2

array = np.loadtxt('IntegerArray.txt')
sorted_array, inv = count_inversions(array)
print(inv)
