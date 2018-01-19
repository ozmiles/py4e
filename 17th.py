#Exercise 5

counter = 0
total = 0.0

while True :
    entry = input('Enter a number: ')
    if entry == 'done' :
        break

    try :
        entry = float(entry)
    except :
        print('Invalid input')
        continue
    #print(entry)
    counter = counter + 1
    total = total + entry

#print ('All Done!')

print('-- counter:' , counter , '-- total:' , total , '-- Average:', total / counter , '--')
