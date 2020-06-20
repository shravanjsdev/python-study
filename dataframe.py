# Dataframe
# Dataframe is a 2 dimensional data structure that contains columns of various datatypes
# It is very similar to python's dictionary
# Dictionaries can be converted to panda's dataframe

import pandas

# Normal dictionary
employee_database_schema = [{
    'name': 'Shravan',
    'id': 7330,
    'age': 24,
    'team': 'Zoho streamline',
    'role': 'Member Technical Staff',
    'exp': '2 years',
    'salary': '65000',
    'workscore': '90/100',
    'org': 'Zoho'
    },
    {
        'name': 'Shahul',
        'id': 5704,
        'age': 25,
        'team': 'Zoho streamline',
        'role': 'Member Technical Staff',
        'exp': '3 years',
        'salary': '75000',
        'workscore': '99/100',
        'org': 'Zoho'
    }]

print('Employee schema dictionary: ', employee_database_schema)

# Pandas dataframe
employee_dataframe_schema = pandas.DataFrame(employee_database_schema)
print(employee_dataframe_schema)

