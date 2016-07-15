from random import randint

def validInput():
    InValidInput=True
    while(InValidInput):
        try:
            a=int(input("Enter a numerical value between 1-10"))
            if a in range (0,11):
                return a
            else:
                raise IOError

        except ValueError:
            print("You did not enter a numerical number")
        except IOError:
            print("Your number was not in range 1-10")

target = randint(1,11)
c = False

for a in range (0,3):
    guess = validInput()

    if guess == target:
        print("congratulations")
        c = True
        break
    elif target-1 <= guess <= target+1:
        print("hot")
    elif target-2 <= guess <= target+2:
        print ("warm")
    else:
        print("cold")
if c == False:
    print("fail")

