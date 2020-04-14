"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading.
# Print all the contents of the file, then close the file.
# Note: pay close attention to your current directory when trying to open "foo.txt".

import inspect
import os


def print_header(header):

    print(f'\n--- {header} ---\n')
    return


############################################################

print_header('foo.txt')

# - We can't gaurantee where the user is running this script.
# - We can't outright know the relative path to our data file.
this_file_path = inspect.getframeinfo(inspect.currentframe()).filename
this_dir_path = os.path.dirname(os.path.abspath(this_file_path))

foo_file_path = os.path.join(this_dir_path, 'foo.txt')

with open(foo_file_path, 'r') as file:

    print(file.read())

############################################################

print_header('bar.txt')

# Open up a file called "bar.txt" (which doesn't exist yet) for writing.
# Write three lines of arbitrary content to that file, then close the file.
# Open up "bar.txt" and inspect it to make sure that it contains what you expect it to contain.

bar_file_path = os.path.join(this_dir_path, 'bar.txt')

with open(bar_file_path, 'w+') as file:

    file.writelines([
        'This is the bar file.\n',
        'You cannot buy a drink.\n',
        'But you can leave.\n',
        'Bye!\n',
    ])

with open(bar_file_path, 'r') as file:

    print(file.read())
