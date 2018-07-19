import random

def dice_roll():
    return random.randint(1,6)

count = int(input("Enter the number of rolls: "))
number_of_double_dice = 0
results = [0 for x in range(13)]


for i in range(0,count):
    first = dice_roll()
    second = dice_roll()
    sum = first + second

print(sum)

'''
    if(first == second):
        number_of_double_dice = number_of_double_dice + 1
        results[sum] = results[sum] + 1


for x in range (2,13):
    print("{0:d} - {1:d}{2:0.4f}%".format(x, results[x], results[x]/count*100))
    #print("Doubles- {0:d}-{{1:0.6f}%".format(number_of_double_dice,       number_of_double_dice*100))
'''
