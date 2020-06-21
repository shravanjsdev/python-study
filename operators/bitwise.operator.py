# Bitwise operator

# They are used to compare binary numbers

# 1. Bitwise AND operator
# Returns 1 if both the bits are 1
# Returns 0 if one or both the bits are 0

x = 8      # 1000  -> 8
y = 10     # 1010  -> 10
z = x & y  # 1000  -> 8
print("x (" + str(x) + ") & y(" + str(y) + ") is", z)

# 2. Bitwise OR operator
# Returns 1 if one or all of the bits are 1
# Returns 0 if both the bits are 0

x = 8      # 1000  -> 8
y = 10     # 1010  -> 10
z = x | y  # 1010  -> 10
print("x (" + str(x) + ") | y(" + str(y) + ") is", z)

# 3. Bitwise XOR operator
# Returns 1 if only one of the bit is 1 (returns 1 if both the bits are different)
# Returns 0 if both the bits are either 1 or 0 (returns 0 if both the bits are same)

x = 8      # 1000  -> 8
y = 10     # 1010  -> 10
z = x ^ y  # 0010  -> 2
print("x (" + str(x) + ") ^ y(" + str(y) + ") is", z)

# 4. Bitwise NOT operator
# Invert the bits

x = 10      # 1010  -> 8
z = ~ x     # 0101  -> 6
print("z = ~ x(" + str(x) + ") is", z)

# 5. Left shift operator
# Shift the number to its left side

x = 11      # 1011
z = x << 2  # 101100  # Adds 2 zeros to the right of the number hence shifting the original number to left
print("x (" + str(x) + ") << y(" + str(y) + ") is", z)

# 6. Right shift operator
# Shift the number to its right side

x = 11      # 1011
z = x >> 2  # 001011  # Adds 2 zeros to the left of hence shifting the number to right and removing last 2 digits
print("x (" + str(x) + ") >> y(" + str(y) + ") is", z)

