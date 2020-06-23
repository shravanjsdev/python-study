# Star pyramid pattern

print("Enter the number of rows: ")
row = int(input())


def starpyramidpattern(rows):
    for i in range(1, rows):
        start = rows - i
        end = rows + i
        for j in range(1, end):
            if j <= start:
                print(end=" ")
            elif j <= end:
                print("*", end="")
            else:
                break
        print("\r")


