import random
randomNumber = random.randrange(0,80)
print("The random number has been generated")
guessed = False
while guessed==False:
     userInput = int(input("Take your guess!"))
if userInput==randomNumber:
        guessed = True
        print("Well done!")
elif userInput>80:
    print ("below 80 please")
elif userInput<0:
    print ("Try higher")
elif userInput>randomNumber:
    print("Try again!")
elif userInput<randomNumber:
    print ("Try higher!")

print("game over!")
