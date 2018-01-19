#15th.py

counter = 0
sum = 0

print('Starting with ' , counter , sum)

for value in [9, 41, 12, 3, 74, 15] :
    counter = counter + 1
    sum = sum + value
    print(counter , '..' , sum , value)

print('Average is ' , sum / counter)
