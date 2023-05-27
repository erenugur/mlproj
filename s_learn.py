import numpy as np

# Difference between an Array and a List:
    # The elements of an array are all of the same type, while lists can have different types of elements.

# Accessing all available functions in Numpy
print('In VS Code, To access all of the functions available in Numpy, type your array, a dot, then scroll.\n')

# "Zero" Array
zeroarray = np.zeros(3)
print(f'The "Zero" Array is {zeroarray}.')
print(f'The shape of the "Zero" Array is {zeroarray.shape}.')
print(f'The first value of the "Zero" Array is {zeroarray[0]}.\n')

# "One" Array
onearray = np.ones(3)
print(f'The "One" Array is {onearray}.')
print(f'The shape of the "One" Array is {onearray.shape}.')
print(f'The first value of the "Zero" Array is {onearray[0]}.\n')

# Manipulating the shape of an array
onearray.shape = (3, 1)
print(f'The shape of the "One" Array is now {onearray.shape}.')
print(f'Printing, the "One" Array now looks like: {onearray}.\n')

# Creating a "pattern" array
pattern_array = np.linspace(2, 10, 5)
print(f'Here is an array: {pattern_array}.')
print(f"The array's first element is 2.0, and its last element is 10.0.")
print(f"Furthermore, the array has 5 elements.\n")

# Creating a one-dimensional array
array = np.array([1.0, 3.0, 4.0, 21.0])
print(f"You can create a one-dimensional array like this one: {array}.")

# Creating a multi-dimensional array
array_2D = np.array([[1.0, 3.0, 4.0, 21.0], [1.0, 3.0, 4.0, 21.0]])
print(f"You can also create a multi-dimensional array like this one: {array_2D}.")
print(f"Make sure to enclose the multiple arrays with brackets when creating the multi-dim. array.\n")

# Creating random arrays
np.random.seed() # This might be optional
random_array = np.random.randint(10, size=6)
print(f"Here is a random array: {random_array}.")
print(f'In the function, "10" means the elements can only be 0 through 9.')
print(f'In the function, "size=6" means the size of the array is 6 elements.')



