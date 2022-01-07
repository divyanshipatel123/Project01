import random
number = random.randint(1,9)
chance = 0
print('Welcome to the number guessing game')
print('Guess a number between 1-9')
#print(number) get the number to test
while chance < 5:
    num = int(input('Enter Your number: '))
    if num!=number:
        if num < number:
            print('Youre number was too low. Try higher than '+ str(num))
            chance+=1
        if num > number:
            print('youre number is too high. try lower than '+str(num))
            chance+=1
    elif num == number:
        print('Congratulations !! ')
        print('You won !! The number was ' + str(number))
        break
if not chance < 5:
    print('You lose the number was ' + str(number))