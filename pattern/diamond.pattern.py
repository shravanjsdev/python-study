# Diamond pattern

print("Enter the number of rows: ");
row = int(input())


def printdiamond(rows):
    printupperdiamond(rows)
    printlowerdiamond(rows)


def printupperdiamond(rows):
    for i in range(0, rows):
        start = rows - i - 1
        end = rows + i + 1
        for j in range(0, end):
            if j <= start:
                print(end=" ")
            elif j <= end:
                print("*", end="")
            else:
                break
        print("\r")


def printlowerdiamond(rows):
    for i in range(0, rows):
        for j in range(0, (2 * rows) - i):
            if j <= i:
                print(end=" ")
            else:
                print("*", end="")
        print("\r")


printdiamond(row)
