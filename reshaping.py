import numpy

a=list(map(int,input("enter your list: ").split()))
print(a)
my_array=numpy.array([a])
print(my_array)
print(numpy.reshape(my_array,(3,3)))
