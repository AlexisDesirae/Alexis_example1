import random
n = input("Enter the number of sides of the dice:") #6
m = input("How many times are you playing?") #5000
a = input("Roll a total of what in a play?") #7
b = input("what counts as a win?") #6
c = input("In how many rolls? ") #10

win = 0
for i in range (m):
    count = 0
    for j in range (c):
        num = random.randint(1, n)
        if num == b:
            count = count + 1
            #print count
    if count >= a:
        win = win + 1
#score = win/m
print = win
