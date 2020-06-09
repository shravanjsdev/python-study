# String

# input() method is used to accept input from user
# input() method takes at most 1 arguments from user

x = 'single quoted string'
y = "double quoted string"

labelled_input = input("Enter a value: ")  # labelled input
unlabelled_input = input()  # unlabelled input
var_labelled_input = input(x + " ")  # variable named labelled input
# erroneous_labelled_input = input("string1", "string2")  # max of 1 args is allowed inside input()

print("Strings \n")

print('variable x is a ', x)
print("variable y is a ", y)
print("variable labelled_input is a user input string of value", labelled_input)

# Strings can be accessed using its index number
name = 'Shravan'
print(name[2])

# Strings are immutable
# name[2] = 'Z'

# Strings can be accessed as a collection
name = 'Shravan Kumar'
print(name[2:5])

# Strings are ordered from 0, its index start from 0 and ends in length-1
# len(string) method is used to return the length of the string
print("length of name", len(name))
print("start index value", name[0])
print("end index value", name[len(name) - 1])

# Accessing collection of values out of bound won't throw error
print(name[4:13])

# Accessing string value at an index number out of bound will throw error
# print("wrong end index value", name[len(name)])

# Strings can also be accessed from reverse order using negative values
print(name[-1])

# Converting string to uppercase
name = name.upper()
print(name)

# Converting string to lowercase
name = name.lower()
print(name)


