# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for idx, el in enumerate(arr):
    if el == target:
      return idx

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  while high != low:
    idx = (low + high) // 2
    if arr[idx] == target:
      return idx
    elif arr[idx] < target:
      low = idx
    else:
      high = idx

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

print(binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], 1))