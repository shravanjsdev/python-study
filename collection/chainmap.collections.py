# Chainmap

from collections import ChainMap

personal_data = {'name': 'Shrvan', 'age': 24}
official_data = {'id': 7330, 'role': 'MTS', 'name': 'Zoho'}

chainmap = ChainMap(personal_data, official_data)
print(chainmap)
