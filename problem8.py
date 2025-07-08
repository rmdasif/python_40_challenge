a = input('Type Play:').lower()
status = True

while status:
    b = input('Player 1:').lower()
    c = input('Player 2:').lower()
    while a == "play":
        if b=="rock" and c=="scissors":
            print("Rock beats scissors")
            break
        elif b=="scissors" and c== "paper":
            print("Scissors beats paper")
            break
        elif b=="paper" and c== "rock":
            print("Paper beats rock")
            break
        elif  c=="rock" and b=="scissors":
            print("Rock beats scissors")
            break
        elif c=="scissors" and b== "paper":
            print("Scissors beats paper")
            break
        elif c=="paper" and b== "rock":
            print("Paper beats rock")
            break
        else:
            print("incorrect input")
            break
    check = input("play again? yes/no: ").lower()
    if check == "no":
        status = False
    elif check == "yes":
        continue
    else:
        print("invalid input type: 'yes' or 'no':  ")



