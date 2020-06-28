# Decorators

# Decorators in python are very powerful, it modifies the behaviour of the function without modifying the behaviour of
# the function permanently.
# It basically wraps another function, since both functions are callable it returns a callable


# Calling function1() will return the wrapper function
def function2(function1):
    def wrapper():
        print("Beginning of wrapper")
        function1()
        print("End of wrapper")
    return wrapper


def fn1():
    print("Function 1")


# function2(fn1)  # This returns the wrapper function with inserting fn1() inside it in place of function1()

# Method 1
function2(fn1)()

# Method2
fn2 = function2(fn1)
fn2()

# Actual usage of decorator
# Method3  # This will modify the definition of fn1() temporarily until its assignment is reverted/modified
fn1 = function2(fn1)
fn1()


@function2  # In short decorator can be used using the @ operator with function name that is going to be decorated
def fn3():
    print("Function 3")


fn3()

