# Dictionary datatype

# It is an unordered collection of heterogeneous data
# It can be changed by using it key
# No duplicate entries are present, adding a value to key whose name is already present will replace the keys value
# It is similar to Objects in JS

# Defining the dictionary
org = 'org_name'
designation_number = 130597

dictionary_var = {
    'name': 'Shravan',
    'emp_id': 7330,
    org: 'Zoho',
    designation_number: '7CLE-7330',
    7330: 9176080504
}
print(dictionary_var)

# Accessing dictionary elements using its key
print(dictionary_var['name'])
print(dictionary_var.get('name'))

# Setting values to dictionary elements using its key
dictionary_var[org] = 'Amazon'
print(dictionary_var)

# There is no set method for dictionary
# dictionary_var.set('designation_number', 'MTS-MLE')  # This throws an error

# Keys method is used to return the dictionary keys
print(dictionary_var.keys())

# len(dictionary) is used to find the length of the dictionary
print(len(dictionary_var))


