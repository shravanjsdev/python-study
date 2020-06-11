# Named tuple

# It returns a tuple with named entry, which means there will be a name assigned to each elements in the tuple
# It overcomes the disadvantage of tuple, by allowing to modify the tuple by using its name rather its index number

from collections import namedtuple

# namedtuple('name_of_the_tuple', 'arg1, arg2, arg3, .... arg n)
# The number of values given in namedtuple instance should be exactly equal to the number of args in namedtuple class.
list_var = ['shravan', 7330, 'Dataprep', 'Morning', 'MLS', 'JS']

# same name can be given to multiple namedtuple example: personal_info
# this stores the entire list 'list_var' in the namedtuple entity 'name'
nt = namedtuple('personal_info', 'name')
ntup = nt(list_var)  # Output: personal_info(name=['shravan', 7330, 'Dataprep', 'Morning', 'MLS', 'JS'])

print(nt)
print(ntup)

# This throws an error stating missing 5 required positional arguments: 'id', 'team', 'shift', 'posting', and 'language'
nt1 = namedtuple('personal_info', 'name, id, team, shift, posting, language')
# ntup1 = nt1(list_var)

# But this works, this takes the values from the list given in namedtuple instance and assign it to the namedtuple class
ntup1 = nt1._make(list_var)

print(nt1)
print(ntup1)



