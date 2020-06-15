# For loop
# Uses and purpose of for loop is same in all the languages, just syntax alone varies

import array as arr

values = arr.array('i', range(1, 11))

for x in values:
    print(x)

# You cannot leave for loop as empty, suppose in case if you need an empty for loop usage of pass is mandatory
for x in values:
    pass




