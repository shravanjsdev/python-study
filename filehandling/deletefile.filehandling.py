# Deleting a file

# To delete a file, we must import os module and use its remove function to delete a file

# Creating 2 sample files for deletion
file1 = open('test1', 'w')
file1.close()

file1 = open('test2', 'w')
file1.close()

# Importing os module
import os

# printing os module
print(os)

# Creating a directory
# os.mkdir creates a directory 'testdir' in the current directory, throws error if it is already there
if not os.path.exists('testdir'):
    os.mkdir('testdir')
else:
    print('Directory with the file name already exists')

# Checking for the presence of file, deleting if it is present (Exception handling)
if os.path.exists('test1'):
    os.remove('test1')
else:
    print('File does not exist')

if os.path.exists('test2'):
    os.remove('test2')
else:
    print('File doe\'s not exist')

# Removes the directory
os.rmdir('testdir')
