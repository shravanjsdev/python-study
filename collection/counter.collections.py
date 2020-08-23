"""
Collection: Counter

The Counter holds the data in an unordered collection, just like hashtable objects.
It allows you to count the items in an iterable list.
Arithmetic operations like addition, subtraction, intersection, and union can be easily performed on a Counter.
"""

from collections import Counter

count = Counter([1, 2, 3, 4, 1, 2, 3, 1, 2, 1])

# prints the counter in dictionary format with its value as key and its count as value
print(count)

# Prints all the counter items in a list by grouping the keys like [1,1,1,2,2,3,...]
print(list(count.elements()))

# prints the counter as list in [ (key, count), (key2, count2)...] fashion
print(count.most_common())

# prints the values of the keys in list in a non-repetitive manner [1,2,3,4]
print(count.values())

# Returns the chain object and its location
print(count.elements())

# Subtraction in counter
sub = {2: 2, 4: 1, 5: 1}

print(count.subtract(sub))  # It returns none
print(count.most_common())






