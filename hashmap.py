# Hashmap
# Hashmap or hashtable is a type of data structure that maps keys to its value pairs
# It implements the abstract array datatype
# It makes use of a function that computes a value as as index using which it stores/ retrieves / manipulates data
# It makes it easy and faster access to data

# In general hashtable, holds a key value pair in which the key is computed by the hash function

# Hashmap is implemented using dictionary, in other words dictionary is a datatype and its background process is hashmap

dictionary = dict()
print('empty dictionary', dictionary)

dictionary['name'] = 'Shravan'
dictionary['ID'] = 7330
dictionary['Salary'] = 50000
dictionary['Team'] = 'Streamline'
dictionary['Reporting_to'] = 'Baskar'

print('First iteration: Looping through dictionary items so its items are referred using its key name')
for x in dictionary:
    print(x)

print('Second iteration: Looping through dictionary key names for this we can use the first iteration technique also')
for x in dictionary.keys():
    print(x)

print('Third iteration: Looping through the dictionary key\'s values')
for x in dictionary.values():
    print(x)

print('Fourth iteration: Looping through the dictionary and printing its key and value')
for x in dictionary:
    print(x, dictionary[x])

for x, y in dictionary.items():
    print(x, y)






