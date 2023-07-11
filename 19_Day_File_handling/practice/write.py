from __future__ import print_function

line = ['I', 'love', 'you', 'so', 'much']

with open('write.txt', 'w') as f:
    for li in line:
        f.write(li)
        f.write('\n')
