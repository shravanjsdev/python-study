# Ordered dictionary


# It is a dictionary subclass, which remembers the order in which the entries were done
# Even if the value of a key is changed, the order remains unaltered in which it was created
# The methods for this is similar to the methods of normal dictionary

from collections import OrderedDict

od = OrderedDict({'name': 'Shravan', 'age': 24})
od['id'] = 7330
od['org'] = 'Zoho'

print(od)

# Getting the values of keys
print(od.keys())

#  Getting the values
print(od.values())

