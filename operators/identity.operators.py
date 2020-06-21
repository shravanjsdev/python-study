# Identity operators

# 1. IS
x = {'name': 'Shravan', 'age': 24}
y = x
z = {'name': 'Kumar', 'age': 24}

# IS operator returns true if both the comparing objects share same memory address not value
print(" x is y", x is y)
print(" x is z", x is z)

# 2. IS NOT
print(" x is not y", x is not y)
print(" x is not z", x is not z)

