import random

win = 0
for i in range (50000):
    count=0
    for j in range(10):
        num = random.randint (1,6)
        if (num==6):
            count = count + 1
           # print count:

        if (count>=7):
            win = win + 1

#score = win
print (win)

