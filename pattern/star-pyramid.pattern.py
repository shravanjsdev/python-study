# Star pyramid pattern

# variable declaration
rows = 0

# Input prompt
print("Enter the number of rows: ")
rows = int(input())


# function definition
def invertedtrianglepattern(row):
    pattern = ""
    for i in range(0, row):
        for j in range(0, (2 * row) - i):
            if j <= i:
                pattern = pattern + " "
            else:
                pattern = pattern + "*"
        print(pattern)
        pattern = ""


def invertedtrianglepattern2(row):
    for i in range(0, row):
        for j in range(0, (2 * row) - i):
            if j <= i:
                print(end=" ")
            else:
                print("*", end="")
        print("\r")


# Function call
invertedtrianglepattern(rows)
invertedtrianglepattern2(rows)
