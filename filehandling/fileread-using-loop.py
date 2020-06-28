# Reading file using loop


# It is very efficient and a faster way of reading file

file1 = open('../pattern/diamond.pattern.py', 'r')

# Printing the file pointer
print('file pointer', file1)

for line in file1:
    print('line', line)  # As readline function after reading a line, moves the file pointer to the end of line
    print('readline', file1.readline())  # The next iteration in loop moves the pointer to the beginning of first line

