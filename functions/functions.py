# Functions

# First class object: In python everything is treated as an object including all the data types, functions too.
# Therefore a function is also known as first class object, and it can also be passed as an argument

# Inner functions: In python, it is possible to define a function inside a function, which is called as inner function


def func1(name):  # Parametrized function
    return f"Hello {name}"  # f is used in prefix to insert dynamic params to the return string


def func2():  # Non parametrized function
    return "Hello world"


def func3():
    return "Shravan"


print(func1('Shravan'))  # Function that returns a string with dynamic value
print(func2())  # Function that returns a static string
print(func1(func3()))  # func3() returns a string which is sent as an input to func1()


