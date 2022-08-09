import random

x = random.randint(0, 5)

count = 0

for count in range(0,4):
    guess = int(input("Please guess a number between number 1 and 15 "))
except SyntaxError:
        print("Dont be a dumbass ask a number")
    
    if guess == x:
        print("you won!")
        quit()
    
                    
    else:
        guess = int(input("guess again "))
    count += 1

else:
        print("you lost this time, try again soon ")
        quit()




