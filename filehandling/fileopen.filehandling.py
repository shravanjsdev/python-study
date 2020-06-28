# File open

# Opening file:
# The files can be opened using python with the below syntax:
# open(filename, mode submode)
#     - filename: The file name that we want to open using python
#     - mode: We can open the files in python using the below 4 modes, which sets the actions that can be performed on
#             that file, example if the file is created in read mode, then the user can't modify the file.
#             Below, are the set of rules and properties that are present for the file open modes, they are:
#                * "r" - (Read), Default value, Opens a file for reading, will throw error if the file does not exist
#                * "a" - (Append), Opens a file for appending, if not present will create a new file
#                * "w" - (Write), Opens (Overwrites) file for writing, if not present will create a new file.
#                * "x" - (Create), Creates a specified file, if it is already present will throw error.
#     - submode: Other than these 4 modes, there are another 2 submodes present in python which tells more to python
#                  * "t" - (Text) - Default value. Performs the mode operation (r, a, w, x) in text mode
#                    * "b" - (Binary) - Binary mode. Performs the mode operations as binary format

# Example: open('shravan.py', wt) - Write in the file names shravan.py in text format

# File open
file1 = open('../pattern/diamond.pattern.py', 'r')

# File close
file1.close()  # This commands resets the file pointer clears the file instance from memory prevents memory leakage
