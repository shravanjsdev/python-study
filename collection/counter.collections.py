# Counter

# The Counter holds the data in an unordered collection, just like hashtable objects.
# It allows you to count the items in an iterable list.
# Arithmetic operations like addition, subtraction, intersection, and union can be easily performed on a Counter.

from collections import Counter

count = Counter([1, 2, 3, 4, 1, 2, 3, 1, 2, 1])
print(count)
print(list(count.elements()))
print(count.values())
print(count.elements())






