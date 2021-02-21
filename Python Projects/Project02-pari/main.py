import random
ramdNamber = random.randint(1, 100)
print(ramdNamber)

userGuess = None
Guesses = 0




while(userGuess != ramdNamber):
    userGuess = int(input("Enter your Guess-->:"))
    Guesses += 1
    if(userGuess==ramdNamber):
        print("Your guess it right!")
    else:
        if(userGuess>ramdNamber):
            print("Enter a smaller number")
        else:
            print("Enter a lerger number")
        

print(f"You guess the number in {Guesses} guesses")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(Guesses<hiscore):
    print("You have just broken the hiscore!")
    with open("hiscore.txt", "w") as f:
        f.write(str(Guesses))