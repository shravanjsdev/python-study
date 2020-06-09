# Tuple datatype

# Ordered, heterogeneous collection of values
# Values at the index cannot be changed (immutable)
# Duplicate entries of values can be present
# Similar to Arrays in JS but tuples are immutable

tuple_var = (1, 2, 3, 1, 'One', 'Two', 'Three', 'One')
print(tuple_var)

# Tuple elements can be accessed using its index numbers, it starts from 0
print(tuple_var[2])

# tuple_var[3] = 'This throws error, tuples are immutable'

# tuple.count(tuple_element) returns the value of number of times the tuple_element is present in the tuple
print(tuple_var.count(1))

# len(tuple) returns the number of elements present in tupe
print(len(tuple_var))

