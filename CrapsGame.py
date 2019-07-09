
import random

def main():



    response = raw_input("Do you want to play craps (y/n)?")

    if response == 'y':
        instructions = raw_input("Do you need instructions (y/n)")
        if instructions == 'y':
            print("Instruction!")
    while response == 'y':
        pause = raw_input("press <Enter> to roll the dice!")
        firstroll = random.randrange(6)+1 + random.randrange(6) +1
        print ("you rolled a", firstroll)
        if firstroll == 7 or firstroll == 11:
            print("You won!")
        elif firstroll == 2 or firstroll == 3 or firstroll == 12:
            print("You lost!")
        else:
            print ("We're going to try to roll the point!")
            point = firstroll
            newroll = random.randrange(6)+1 + random.randrange(6) +1
            print("you roll a", newroll)

            while newroll != point and newroll != 7:
                print ("Try again to roll your point!")
                pause = raw_input("press <Enter> to try to roll the point!")
                newroll = random.randrange(6) + 1 + random.randrange(6) + 1
                print("you roll a", newroll)
            if newroll == point:
                print ("You won!")
            else:
                print ("You lost!")

            response = raw_input("Do you want to play craps again (y/n)?")
        print ("Okay, see you next time!")



if __name__ == "__main__":
    main()



