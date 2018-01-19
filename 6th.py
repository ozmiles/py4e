print('       ')
print('       ')
print('       ')

amount = input('How much? ')
type(amount)

if float(amount) < 2 :
    print('Less than 2')

elif float(amount) < 5 :
    print('Less than 5')

elif float(amount) < 10 :
    print('Less than 10')

elif float(amount) < 20 :
    print('Less than 20!')

else :
    print('More than 20')

print('All done!')
