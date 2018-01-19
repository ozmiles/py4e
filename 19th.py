import random


counter = 0
random_num = random.randrange(0,100)

while random_num != 15 :
    print(random_num)
    counter = counter + 1
    random_num = random.randrange(0,100)
print('Number of atempts:',counter)
