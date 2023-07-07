from __future__ import print_function

f = open('test.txt')
content = f.read() # Reads the contents of the file
first_seven = f.read(7) # Reads the first seven characters
first_line = f.readline() # Reads the first line
all_lines = f.readlines() # Reads line by line creating a list of lines
print("\nFIRST SEVEN CHARACTERS\n\n", first_seven)
print("\nFILE OPERATION TYPE\n\n",type(content))
print("\nFILE CONTENT\n\n", content)
print("\nFILE DETAILS\n\n", f)
print("\nFIRST LINE TYPE\n\n", type(first_line))
print("\nFIRST LINE\n\n", first_line)
print("\nTYPE OF ALL LINES\n\n", type(all_lines))
print("\nALL LINES IN A LIST\n\n", all_lines)
f.close()

