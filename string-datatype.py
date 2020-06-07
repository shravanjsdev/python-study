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
