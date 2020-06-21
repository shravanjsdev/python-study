# Membership operators

# 1. IN operator
# Returns true if the sequence with the specified value is present in the object
# It is used to check whether a value in present in the list
# Only one value at a time can be checked using in from list only

list_var = [10, 20, 30, 40, 50]

print("10 in list_var", 10 in list_var)  # True
print("60 in list_var", 60 in list_var)  # False
print("[10,20] in list_var", [10, 20] in list_var)  # False
print("[40,30,20] in list_var", [40, 30, 20] in list_var)  # False
print("[10,70] in list_var", [10, 70] in list_var)  # False

# 2. NOT IN operator
# Returns true if the sequence with the specified value is not present in the object

print("10 in list_var", 10 not in list_var)  # False
print("60 in list_var", 60 not in list_var)  # True
print("[10,20] in list_var", [10, 20] not in list_var)  # True
print("[40,30,20] in list_var", [40, 30, 20] not in list_var)  # True
print("[10,70] in list_var", [10, 70] not in list_var)  # True

