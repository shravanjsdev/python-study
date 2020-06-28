# Nested function

# The childfunctions are visible only inside their parent function
# And only inside the parent function its child functions can be invoked


def parentfunction1():
    print('This is a parent function')

    def childfunction1():
        print('This is the first child function')

    def childfunction2():
        print('This is the second child function')

    childfunction1()
    childfunction2()


parentfunction1()

