import numpy as np


def quicksort(array, pivot_mode='random'):
    # Handle base case
    n = len(array)
    if n == 0:
        # Add one comparison in this case to make up for the fact that only
        # one partition was made
        return array, 1
    if n == 1:
        return array, 0

    # Choose pivot
    if pivot_mode == 'random':
        # Select pivot randomly and put it in first array position
        idx = np.random.choice(range(n))
        temp = array[0]
        array[0] = array[idx]
        array[idx] = temp

    elif pivot_mode == 'final':
        idx = n-1
        temp = array[0]
        array[0] = array[idx]
        array[idx] = temp

    elif pivot_mode == 'median':
        three = [array[0], array[n/2], array[n-1]]
        idx = np.array([0, n/2, n-1])[np.argsort(three)[1]]
        temp = array[0]
        array[0] = array[idx]
        array[idx] = temp

    pivot = array[0]

    # Partition around pivot
    i = 1
    for j in range(1, n):
        if array[j] < pivot:
            # Swap array[i] and array[j]
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

            # Increase i to reflect change in the partition division
            i += 1

    # Final swap to insert the pivot in the correct position
    array[0] = array[i-1]
    array[i-1] = pivot

    # Make recursive calls on the partitions
    array1, comp1 = quicksort(array[:i-1], pivot_mode)
    array2, comp2 = quicksort(array[i:], pivot_mode)

    return array1+[pivot]+array2, comp1+comp2+n-3

array = np.loadtxt('QuickSort.txt')
sorted_array, comp = quicksort(array, pivot_mode='median')
