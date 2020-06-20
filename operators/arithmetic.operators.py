# Arithmetic operators

# Operations that can be performed using arithmetic operators

# 1. Addition
x = 20
y = 10
my_sum = x + y
# Here the operators are of type int and integers cannot be concatenated with strings like other languages
# There is no implicit conversion, we need to typecast the variable to string explicitly
print("Addition of x: " + str(x) + " and y: " + str(y) + " is: " + str(my_sum))

# 2. Subtraction
my_sub = x - y
print("Difference of x: " + str(x) + " and y: " + str(y) + " is: " + str(my_sub))

# 3. Multiplication
my_prod = x * y
print("Product of x: " + str(x) + " and y: " + str(y) + " is: " + str(my_prod))

# 4. Quotient (Division)
my_quot = x / y
print("Quotient of x: " + str(x) + " and y: " + str(y) + " is: " + str(my_quot))

# 5. Remainder (Modulus)
my_mod = x % y
print("Remainder of x: " + str(x) + " and y: " + str(y) + " is: " + str(my_mod))

# 6. Exponent
my_exp = x ** y
print("Exponent of x (" + str(x) + ") to the power ^ y (" + str(y) + ") is: " + str(my_prod))

# 7. Float division
x = 20.20
y = 10.45
my_float_div = x // y
print("Float division of x: " + str(x) + " and y: " + str(y) + " is: " + str(my_float_div))
