

#

handle = open('mbox-short.txt')

count = 0

for line in handle :
    line = line.rstrip()
    if line.find('From') >= 0:
        count = count + 1
        print(count, line)


import re

handle2 = open('mbox-short.txt')

count2 = 0

for line in handle2 :
    line = line.rstrip()
    if re.search('^From', line) :
        count2 = count2 + 1
        print(count2, line)
