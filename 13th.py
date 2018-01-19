
#Adding the largest Number

largest_so_far = -1
counter = 0

print('Before' , largest_so_far)

for the_number in [9, 41, 12, 3, 74, 15] :
    counter = counter + 1
    if the_number > largest_so_far :
        largest_so_far = the_number
    print(counter , '..', largest_so_far , the_number)

print('Total Steps: ' , counter)
print('After' , largest_so_far)

print('-------------------')


#Finding the smallest Number

smallest_so_far = 100
counter = 0

print('Before' , smallest_so_far)

for the_number in [9, 41, 12, 3, 74, 15] :
    counter = counter + 1
    if the_number < smallest_so_far :
        smallest_so_far = the_number
    print(counter , '..', smallest_so_far , the_number)

print('Total Steps: ' , counter)
print('Smallest so far is' , smallest_so_far)
