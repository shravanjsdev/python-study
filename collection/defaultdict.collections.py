# Default dictionary
# Default dictionary is a dictionary subclass which calls a factory function to supply missing values

# The methods and behaviour of defaultdict is similar to that of normal dictionary, with the difference
# in dictionary when we try to access a value with a missing key/wrong key it throws key is not present error
# but the defaultdict creates a key if it is not present and assign value 0 to it

from collections import defaultdict

# If we specify any datatype as defaultdict(datatype) parameter, then its ground value will be returned for the missing
# keys, example 0 for int, false for bool, and {} for dict. But if we didn't specify any param it will throw an error.

dd = defaultdict(dict)

dd[1] = 'Shravan'
dd[2] = 'Rohit'
dd[3] = 'Krishna'
dd[4] = 'Vijay'
dd[5] = 'Gowtham'
dd['shravan'] = 'Kumar'

print(dd)
print(dd[3])
print(dd['shravan'])


