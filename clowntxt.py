print('clowntxt.py')

fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'

handle = open(fname)
for line in handle :
    line = line.rstrip()
    print(line)
    words = line.split()
    print(words)
    for w in words :
        print(w)
