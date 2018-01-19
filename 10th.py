#Interate Loop "While"

print('10th.py')

while True :
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)

print('Done')
