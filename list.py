print('list.py')

x = list()
type(x)
dir(x)

# Create a list (empty)
stuff = list()

# Append some data to this list
stuff.append('book')
stuff.append('99')
print(stuff)
stuff.append('cookie')
print(stuff)


# Find something in the list
x = (1,2,3,3,4,5,6,7,8,8,99,0)
y = 50 in x
print(y)


# Sort a list
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)

# Only show item in list at index 2
print(friends[2])

#
nums = [1,2,3,4,5,6,7,8,99,9,0]
print('How many items in the list?', len(nums))
print('What is the largest item?', max(nums))
print('What is the smallest Item?', min(nums))
print('What is the total of all items?' ,sum(nums))
print('What is the average', sum(nums)/len(nums))       # len applies to the number of items in the list
