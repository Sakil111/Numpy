import numpy

def arrays(arr):
    arr.reverse()
    a=numpy.array(arr,float)
    return a
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)