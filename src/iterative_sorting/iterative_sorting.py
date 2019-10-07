# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        tmp = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = tmp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    j = len(arr) - 1
    while j > 1:
        for i in range(0, j):
            if arr[i] > arr[i + 1]:
                tmp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = tmp
        j -= 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    indexes = []
    result = []
    for _ in range(len(arr)):
        result.append(0)
    for _ in range(maximum + 1):
        indexes.append(0)
    # Add 1 to indexes of corresponding numbers from arr
    for el in arr:
        indexes[el] += 1
    # sum
    for i in range(len(indexes)):
        if i > 0:
            indexes[i] += indexes[i - 1]
    # remove 1 from a correct indexes value
    # add value from arr in correct place in result array based on indexes
    for i in range(len(arr)):
        indexes[arr[i]] -= 1
        result[indexes[arr[i]]] = arr[i]

    return result

print(count_sort([3, 4, 6, 2, 3, 5, 7, 5, 5], 7))