# Arrays

# Homogeneous collection of datatypes
# Its definition and purpose is same in all languages
# Its stores same type of values, and in python it needs to be imported and used in the file, these are the only 2
# differences between list and array in python

# We can import arrays in 3 types
# 1. without alias: import array
# 2. with alias: import array as arr
# 3. using *: from array import *

# without alias,
# import array -> importing the array package/module/class
# array.array -> using the array constructor
# usually we call constructor either using its instance_name = new Constructor() or
# classname.constructor (in case of a static class)
# static_class_name.constructor_name('datatype', [comma separated values])

# import array
# arr = array.array('i', [1, 2, 3, 4, 5])
# print(arr)

# with alias
# import array as arr -> Importing the array class and referring the class using its alias name
# alias_name_of_static_class.constructor_name('datatype', [comma separated values])

# import array as arr
# myArray = arr.array('i', [1, 2, 3, 4, 5])
# print(myArray)

# importing using *
# from array import *
# we can directly access the constructor of the class without any classname or alias since all of the array was imported

from array import *
a = array('i', range(1, 100))
print(a)

# Accessing array elements
# array elements can be accessed using its index numbers, and there are two types of indexing, postive and negative
# positive indexing: 0 to length-1 index [traverse from left to right of the array]
# negative indexing: -1 to -100 index [traverse from right to left of the array]

print(a[5])
print(a[-94])

# Basic array operations
# 1. finding length of an array
# 2. adding/changing elements of an array
# 3. removing/deleting elements of an array
# 4. array concatenation
# 5. slice
# 6. looping through an array

# Finding length of an array
length = len(a)
print('length of the array is', length)

# Adding elements to an array
print('Array before insertion', a)

a.insert(3, 100)  # Add an element at a specific position of an array  # array.insert(position, value)
print('Array after insertion', a)

a.extend([50, 51, 52])  # Used to add more than one elements at the end of the array
print('Array after extend', a)

a.append(53)  # Used to add a single element at the end of the array
print('Array after append', a)

# Removing elements from an array
a.remove(100)  # Used for deleting an element from the array, without returning its value  #array.remove(value)
a.pop()  # Used for deleting an element of the array, and to return the deleted value #array.pop(), array.pop(index)
a.pop(3)  # Removes the 4th element in the array

# Array concatenation
arr1 = array('d', [1.0, 1.1, 1.2, 1.3])
arr2 = array('d', [1.4, 1.5, 1.6, 1.7])
arr3 = array('d', [5.0, 5.1])

arr3 = arr1 + arr2

print('array 1: ', arr1)
print('array 2: ', arr2)
print('Sum of the array (Concatenation): ', arr3)

# Slicing the array
# An array can be sliced using the : symbol, it returns the range of elements specified by the [start_index:end_index]
spliced_array = arr3[0:3]  # Returns 3 elements from 0 to 2
print(spliced_array)

# Returning the reverse of array using slice
print(spliced_array[::-1])  # Returns the reversed array but wont modify the array, it will just returns reverse values


