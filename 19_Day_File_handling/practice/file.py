from __future__ import print_function

'''
Second option to opening a file and closing it automatically
'''
with open("test.txt") as f:
    content = f.read()  # Reads the content of the file
    line = f.readline()  # Reads the first line of the file
    lines = f.read().splitlines()  # Reads each line and creates a list for them
    print("\nFILE CONTENT\n\n", content)
    print("\nREAD LINE\n\n", line)
    print("\nREAD LINES\n\n", lines)
