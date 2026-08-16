import sys

print("Welcome to the Quiz Game")
count = 0
while True:
    play = input("Do you want to play? (y/n): ")
    if play.lower() == "y":
        print("Okay let's play the game!!")

        answer = input("What does CPU stands for?: ")
        if answer.lower() == "central processing unit":
            print("Correct!!")
            count+1
        else:
            print("Incorrect!!")

        answer = input("What does GPU stands for?: ")
        if answer.lower() == "graphical processing unit":
            print("Correct!!")
            count+1
        else:
            print("Incorrect!!")

        answer = input("What does NPU stands for?: ")
        if answer.lower() == "neural processing unit":
            print("Correct!!")
            count+1
        else:
            print("Incorrect!!")


        print(f"Your total mark is: {count}/3")

    elif play.lower() == "n":
        sys.exit()
    else:
        print("Enter valid choice!")


