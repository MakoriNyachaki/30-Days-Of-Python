from __future__ import print_function

'''
witelines and concatinating lines into a text file
'''

lines = [
        'Kenya', ' is a great democartic country. ',
        'Many have taken every opportunity to be a venture, ',
        'making it a capitalist country.'
        ]

with open('write1.txt', 'w') as f:
    f.writelines(lines)
    # Treating each element of the list as a new line
    f.write('\n')
    f.write('\n'.join(lines))
