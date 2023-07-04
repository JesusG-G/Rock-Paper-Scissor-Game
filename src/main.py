import random

def comparate_option(player_option, computer_option):
    match player_option:
        case 1:
            print("You choose Rock")
            if computer_option == player_option:
                print("The computer choosed Rock")
                print("It's a Tie :/")
            elif computer_option == 2:
                print("The computer choosed Paper")
                print("You loose :(")
            elif computer_option == 3:
                print("The computer choosed Scizor")
                print("You win :)")

        case 2:
            print("You choose Paper")
            if computer_option == player_option:
                print("It's a Tie :/")
            elif computer_option == 3:
                print("The computer choosed Scizor")
                print("You loose :(")
            elif computer_option == 1:
                print("The computer choosed Rock")
                print("You win :)")
        case 3:
            print("You choose Scizor")
            if computer_option == player_option:
                print("It's a Tie :/")
            elif computer_option == 1:
                print("The computer choosed Rock")
                print("You loose :(")
            elif computer_option == 2:
                print("The computer choosed Paper")
                print("You win :)")
        case _:
            print("Please select a valid option")

if __name__ == "__main__":
    print("ROCK, PAPER, SCIZOR GAME")
    print("This game is vs the computer.")
    print("RULES")
    print("-"*20)
    print("""
    Winning Rules of the Rock paper and scissor game as follows:
    rock vs paper->paper wins 
    rock vs scissors->rock wins 
    paper vs scissors->scissors wins    
    """)
    print("-"*20)
    print("Please choose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scizor")
    choosen_option = int(input(">> "))
    computer_chose = random.randint(1,3)
    comparate_option(choosen_option,computer_chose)
    

