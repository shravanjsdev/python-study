# Star pyramid pattern

print("Enter the number of rows: ")
row = int(input())


def starpyramidpattern(rows):
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


starpyramidpattern(row)


