# List datatype

# Ordered, heterogeneous collection of values
# Values at the index can be changed
# Duplicate entries of values can be present
# Similar to Arrays in JS

list_var = [1, 'One', 2, 'Two', 'Three', 3, 1, 'One']
print(list_var)

# Accessing list using its index number
list_var[6] = 4
list_var[7] = 'Four'
print(list_var)

# Accessing list using range
print(list_var[3:7])

# Accessing list using range with out of range values
print(list_var[3:10])

# Accessing list using negative index number
print(list_var[2:-1])
print(list_var[-2: 4])  # first number should not be negative, returns empty array

# Accessing list using its index number out of range
# list_var[8] = 5  # throws error: list assignment out of range
# list_var[10] = 6

# Appending elements to the list
list_var.append(6)
list_var.append('Six')
print(list_var)

# list index starts from 0
# Insert elements to the list
list_var.insert(8, 5)  # list.insert(index, value)
list_var.insert(9, 'Five')  # It inserts the value 'Five' in the 9th index and shifts the elements further to right.,
# list_var = [1, 'One', 2, 'Two', 3, 'Three', 4, 'Four', 5, 'Five', 6, 'Six']
# list_var index = [0 - 11] 12 elements

# Trying to insert elements with index out of range just appends the value to the list at last
list_var.insert(150, 'Should trow error1')  # It inserts 'Should trow error1' at 12th index (appends)
list_var.insert(100, 'Should trow error2')  # It inserts 'Should trow error1' at 13th index (appends)
list_var.insert(170, 'Should trow error3')  # It wont see the index number at which we insert if it is out of range
print(list_var)

# Reversing the list
list_var.reverse()
print(list_var)  # Reverse the list

# This will not work, reverse() will reverse the values in the list, but it will not return the reversed list
# So the next time when you print the list_var it will be printed in reverse
print(list_var.reverse())  # This prints None , None is returned by list_var.reverse()




