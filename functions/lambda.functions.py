# Lambda functions

# Nameless and autonomous functions in python are called as lambda functions
# lambda is a keyword and its not a name

# Uses of lambda functions:
# 1. One time use (they are used for one time use, also called as throw away functions)
# 2. I/O of other functions (they are also passed as inputs or returned as outputs of other higher order functions
# 3. Reduce code size (The body of lambda function is written in a single line)

# How to write lambda functions:
# 1. We need to specify the lambda keyword
# 2. Followed by the arguments
# 3. Followed by the colon
# 4. Followed by the expression (body of lambda function)

# Syntax:
# lambda arguments: expression

# Example:
l1 = lambda x: x * x
print(l1(3))


# Uses:
def slope(x):
    m = 5
    return lambda c: m * x + c

xaxis = 7
output = slope(xaxis)
out = output(5)
print('output', out)

# Uses of lambda in filter:
# Used to filter the given iterables(list,sets etc) with the help of another function passed as an argument to test all
# the elements to be true or false

list1 = [1, 2, 3, 4, 5, 6, 7]
oddlist = list(filter(lambda x: x%2 != 0, list1))
evenlist = list(filter(lambda x: x%2 == 0, list1))

print('odd list', oddlist)
print('even list', evenlist)

# Uses of lambda in map:
# Applies a given function to all the iterables and returns a new list



