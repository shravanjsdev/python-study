# File read
# Files that are opened in read mode alone supports read operation like read, readline, readlines etc..
file1 = open('../pattern/diamond.pattern.py', 'r')

# File read n characters (File.read() operation is supported only if the file is opened in read mode)
print(file1.read(18))  # Reads the file from 0 to 18th position, then the file pointer will be set in the 18th position

# File read n characters
print(file1.read(18))  # Reads the file from 18th to 36th index, now the file pointer will be in 36th position

# File read rest of the data
print(file1.read())  # Read the rest of the file fully starting from 36th position

# Close the file, this will close the file and set the pointer again to 0
file1.close()

file1 = open('../pattern/diamond.pattern.py', 'r')
print(file1.readline())  # Line by line output, reads the first line
print(file1.readline())  # reads the second line
print(file1.readline())  # reads the third line
print(file1.readline())  # reads the fourth line

print(file1.readlines())  # Prints all lines of the file in a single line separated by comma enclosed by quotes
# test ['\n', '\n', 'def printdiamond(rows):\n', ' printupperdiamond(rows)\n', 'printlowerdiamond(rows)\n', '\n', '\n',
# 'def printupperdiamond(rows):\n', 'for i in range(0, rows):\n', 'start = rows - i - 1\n', ' end = rows + i + 1\n','
# for j in range(0, end):\n', 'if j <= start:\n','print(end=" ")\n', 'elif j <= end:\n', 'print("*", end="")\n', '
# else:\n', ' break\n', 'print("\\r")\n', '\n', '\n', 'def printlowerdiamond(rows):\n', ' for i in range(0, rows):\n',
# 'for j in range(0, (2 * rows) - i):\n', 'if j <= i:\n', 'print(end=" ")\n', 'else:\n', 'print("*", end="")\n', '
# print("\\r")\n', '\n', '\n', 'printdiamond(row)\n']

print(file1.readline(6))  # Reads only the 3rd line of the code

file1.close()
