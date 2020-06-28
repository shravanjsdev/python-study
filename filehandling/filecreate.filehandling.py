# File create

# The 'x' - create file mode is used to create a new file with the given name
# Creating a file with a name which is already present will throw an error

file1 = open('testfile.py', 'x')
file1.close()
