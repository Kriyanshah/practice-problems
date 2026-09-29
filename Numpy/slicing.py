#slicing operations
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5]) # index 1 to 4
print(arr[:5]) # index 0 to 4
print(arr[:]) # index first to last (0 to 7)
print(arr[4:]) # index  4 to end (4 to 7)
print(arr[:4]) # index start to 4 (0 to 3)

# negative slicing 
print(arr[-3:-1]) # from back last 2nd to last last 3rd (-1 not included)

# step 
print(arr[1:5:2]) # step =  2 prints numbers at a step of 2
print(arr[::2]) # step = 2 prints numbers from start to end with a step 2
