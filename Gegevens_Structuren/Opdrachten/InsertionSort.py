import random
val = input("Enter the amount of random numbers: ")
randomlist = []
counter = 0

for i in range(0,int(val)):
    n = random.randint(1,100)
    randomlist.append(n)

for i in range(0, int(val)):
    j = i
    while j > 0 and randomlist[j-1] > randomlist[j]:
        counter = counter + 1
        randomlist[j-1], randomlist[j] = randomlist[j], randomlist[j-1]
        j = j-1
    
print(randomlist)
print(counter)