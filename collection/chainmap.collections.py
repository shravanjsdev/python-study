# Chainmap

# It is used to store the collection of dictionaries in a single view
# It is used to encapsulate multiple dictionaries in a single unit.

from collections import ChainMap

personal_data = {'name': 'Shrvan', 'age': 24}
official_data = {'id': 7330, 'role': 'MTS', 'name': 'Zoho'}

chainmap = ChainMap(personal_data, official_data)
print(chainmap)
