from __future__ import print_function

'''
Appending more line to write.txt
'''

more_love = [
        ' ',
        'My fiancee',
        'loves hiking and',
        'cycling.'
        ]

with open('write.txt', 'a') as f:
    f.write('\n'.join(more_love))
