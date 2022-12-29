import numpy as np
list_a = [1,2,3,4]
list_b = [5,6,7,8]
print(list_a + list_b)
#
numpy_a = np.array([1,2,3,4])
numpy_b = np.array([5,6,7,8])
print(numpy_a)
print(numpy_a*numpy_b)


#common properties
numpyBasic_array=np.array([1,2,3,4,9.6])
print(numpyBasic_array.dtype)
print(numpyBasic_array.itemsize)
print(numpyBasic_array.size)

numpyBasic_array1=np.array([1,2,3,4.5,"a"])
print(numpyBasic_array1.dtype)
print(numpyBasic_array1.itemsize)
print(numpyBasic_array1.size)

#2D arrays
array_2D = np.array([[1,2,3],[3,4,5],[6,7,8]])
print(array_2D)
print("Dimensions: {}".format(array_2D.ndim))
print("Shape: {}".format(array_2D.shape))
print("Array Dtype: {}".format(array_2D.dtype))

array_2D = np.array([1,2,3],dtype='float64')
print(array_2D)
print(array_2D.itemsize)
print(array_2D.dtype)


#3D arrays
array_3D = np.array([[[1,2,3],[3,4,5],[6,7,8],[9,1,2]]])
print(array_3D)
print("Dimensions: {}".format(array_3D.ndim))
print("Shape: {}".format(array_3D.shape))
print("Array Dtype: {}".format(array_3D.dtype))

#accessing  arrays
array_x = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(array_x)
print(array_x.size)
print(array_x[1,2])
print(array_x[0,2])
print(array_x[:,2])
print(array_x[:,-3])
#step -start:end: stepsize
print(array_x[0, 0:4:2])
print(array_x[:, 0:4:2])
array_x[0,2] = 10
array_x[:,2] = 10
print(array_x)

#3d arrays
array_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(array_3d)
#selecting the particular elements from 3d arrays
print(array_3d[0,1,0])
print(array_3d[:,1,0])
#updating 3d array
array_3d[:,0,:]=100
print(array_3d)

array_3d[:,0,:]=[[10,10],[20,20]]
print(array_3d)
print("\n")

#common array's
#one's two's empty
print(np.zeros(3))
print(np.ones(3))
print("\n")
two_d = np.zeros((3,3))
print(two_d)
print("\n")
three_d=np.zeros((2,3,3))
print(three_d)
print("\n")
print("\n")
four_d=np.zeros(((3,2,2,3)))
print(four_d)
print("\n")
print(np.full((3,3),[1,2,3]))
print(np.full((3,3),[1,2,3],dtype="float32"))
print("\n")
array_a=[1,2,3]
print(np.full_like(array_a,4))

print("\n")

#repeat
array_r = [[1,2,3],[4,5,6]]
array_repeat = np.repeat(array_r,2, axis=1)
print(array_repeat)
print("\n")

array_zeros = np.zeros((3,3))
array_zeros[1,1]=7
print(array_zeros)
print("\n")

update_array = np.zeros((5,5))
update_array[1:-1,1:-1] = array_zeros
print(update_array)
#copy
array_y = ([1,2,3,4])
array_z = array_y
array_y[0] =7
print(array_y)
print(array_z)

#math operations
array_math = np.array([1,2,3])
print(np.sin(45))
print("declared array:{}".format(array_math))
print("add 10 to array:{}".format(array_math+10))
print("sub 2 from array:{}",format(array_math-2))
print("raise to pow array:{}".format(array_math**2))
print("multiply array:{}".format(array_math*5))
print("divide array by 2:{}".format(array_math/2))

#algebra with numpy
arr_a = np.ones((2,3))
arr_b = np.full((3,2),2)
print(arr_b)
print(arr_a)
print(np.matmul(arr_a,arr_b))
#statistics
n_a=[[1,1,1,1],[0,0,0,0,0,0,0]]
print(n_a)
print(np.array([np.ones(4),np.zeros(7)]))

print(("\n"))
#axis 1 checks row (horizontally)
#axis 0 checks colum(vertically)
array_stats = [[1,2,3], [4,5,-6]]

print(np.min(array_stats))
print(np.min(array_stats, axis= 0))
print(np.min(array_stats, axis= 1))
print(("\n"))

print(np.max(array_stats))
print(np.max(array_stats, axis= 0))
print(np.max(array_stats, axis= 1))
print(("\n"))

print(np.sum(array_stats, axis=0))
print(np.sum(array_stats, axis=1))
print(("\n"))

# reshape

array_stats =np.array( [[1,2,3,7], [4,5,-6,4]])

print(array_stats.reshape((4,2)))
#arrange - array range
one_d = np.arange(6)
print(one_d)
print(("\n"))

two_d = np.arange(12).reshape(4,3)
print(two_d)
print(two_d.shape)
print(("\n"))


three_d = np.arange(24).reshape(2,3,4)
print(three_d)
print(three_d.shape)
print(("\n"))

# stacking

a_v1 = np.array([1,2,3,4])

a_v2 = np.array([1,2,3,4])

print(np.array([a_v1, a_v2]))


print(np.hstack([a_v1, a_v2]))

print(("\n"))

#
import numpy as np
data_from_Text_File=np.genfromtxt('Numpy_File.txt',delimiter=',')
print(data_from_Text_File)
print(("\n"))

data_from_Text_File=data_from_Text_File.astype('int32')
print(data_from_Text_File)
print(("\n"))

print(data_from_Text_File>6)
print(("\n"))
print(data_from_Text_File[data_from_Text_File > 0])
print(("\n"))

print(data_from_Text_File[data_from_Text_File < 0])
print(("\n"))




#
def numpy_function(x,y,z):
    return 10*x+y+z
b = np.fromfunction(numpy_function, (4,2,6), dtype=int )

print(b)

