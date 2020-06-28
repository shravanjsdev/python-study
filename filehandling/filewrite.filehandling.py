# File write

# To write to an existing file we can use either of the 2 params in open mode
# If there is no file present at the given location with the file name, it will create a new file with the given name
# 'a' - Append mode - will append to the end of the file
# 'w' - Write mode  - Will delete the entire content of file, and overwrite the file, from the starting of the file

# This deletes the content of the file, and writes it from the file starting point
file1 = open('../pattern/diamond-test.pattern.py', 'w')
file1.write('\n#This is purely for testing purpose')
file1.close()

# This appends the input to the file, without deleting the existing contents
file1 = open('../pattern/diamond-test.pattern.py', 'a')
file1.write('\n#This is purely for testing purpose')
file1.close()

# This is same as first example
file1 = open('../pattern/diamond-test.pattern.py', 'wt')
file1.write('\n#This is purely for testing purpose')
file1.close()

# This throws an error, as if write type if set to binary, then we should provide a byte-stream as input
# In binary write, providing string as input will throw TypeError: a bytes-like object is required, not 'str'
file1 = open('../pattern/diamond-test.pattern.py', 'wb')
# file1.write('\n#This is purely for testing purpose')
file1.close()

# This writes to the file in binary format, the below code copies contents from one file to another file
file = open('../pattern/diamond.pattern.py', 'rb')
file1 = open('../pattern/diamond-test.pattern.py', 'wb')

for line in file:
    file1.write(file.readline())

file.close()
file1.close()



