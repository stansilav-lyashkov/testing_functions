import doctest



def buble_sort(array):
    """
    >>> buble_sort([3,0, 10])
    [0, 3, 10]
    >>> buble_sort([])
    []
    """



    sorted_array = array
    for j in range(len(array)):
        for i in range(len(array)-1):
            if sorted_array[i] > sorted_array[i+1]:
                sorted_array[i], sorted_array[i+1] = sorted_array[i+1], sorted_array[i]

    return sorted_array







doctest.testmod()