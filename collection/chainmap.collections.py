"""
Collection: Chainmap
---------------------

It is used to store the collection of dictionaries in a single view
It is used to encapsulate multiple dictionaries in a single unit.

Operations on ChainMap
1. keys() :- This function is used to display all the keys of all the dictionaries in ChainMap.
2. values() :- This function is used to display values of all the dictionaries in ChainMap.
3. maps :- This function is used to display keys with corresponding values of all the dictionaries in ChainMap.
4. new_child() :- This function adds a new dictionary in the beginning of the ChainMap.
5. reversed() :- This function reverses the relative ordering of dictionaries in the ChainMap.
"""

from collections import ChainMap

personal_data = {'name': 'Shravan', 'age': 24}
official_data = {'id': 7330, 'role': 'MTS', 'name': 'Zoho'}
new_data = {'team': 'Dataprep', 'exp': 2}

# Creating chainmap
chainmap = ChainMap(personal_data, official_data)

# Adding dictionary to chainmap
chainmap = chainmap.new_child(new_data)

# Printing keys
print(chainmap.keys())

# Printing values
print(chainmap.values())

# Printing dictionaries inside the chainmap, enclosing it using an array.
print("Chainmap:", chainmap.maps)

# Reversing chainmap
chainmap.maps = reversed(chainmap.maps)

# Printing reversed chainmap instance
print("Reversed chainmap:", chainmap)

"""
NOTES:
* new_child(dict) prepends the child dictionary to the chainmap
* keys() and values() returns the view object of the chainmap which cannot be accessed only it can be viewed. So it is
  used inside the list to access the keys and values.
* chainmap.maps should be used to reverse the chainmap and store the chainmap, then only chainmap can be directly 
  accessed, and after reversing chainmap can be used but its keys, values, maps cannot be used.
"""





