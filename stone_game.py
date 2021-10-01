# ----stone paper scissor-----
def whole_proram():
    import random

    list = ['stone','paper','scissor']

    print("""
    -----stone paper scissor game-----
    
    press s for stone 
    press p for paper
    press c or scissor
    """)
    no_of_chances  = 0
    chances = 10
    human_point = 0
    pc_point = 0

    while no_of_chances < chances:
        print("*****************************************\n")
        _input= str(input("enter your choice \n"+"Stone paper or scissor : "))
        _random = random.choice(list)

        #if user enters "S"

        if _input ==  's' and _random == 'scissor':
            print(f"computer choice : {_random}")
            print("=========================================")
            print("You won")
            print("=========================================")
            human_point = human_point + 1
            print(f'\nYour point : {human_point}',f"\ncomputer's point : {pc_point}\n")


        elif _input == 's' and _random == 'stone':
            print(f"computer choice : {_random}")
            print("=========================================")
            print("tie")
            print("=========================================")
            print(f'\nYour point : {human_point}', f"\ncomputer's point : {pc_point}\n")


        elif _input == 's' and _random == 'paper':
            print(f"computer choice : {_random}")
            print("=========================================")
            print("you lose")
            print("=========================================")
            pc_point = pc_point + 1
            print(f'\nYour point : {human_point}', f"\ncomputer's point : {pc_point}\n")

        #when user input is paper

        elif _input == 'p' and _random == 'scissor':
            print(f"computer choice : {_random}")
            print("=========================================")
            print("you lose")
            print("=========================================")
            pc_point = pc_point + 1
            print(f'\nYour point : {human_point}', f"\ncomputer's point : {pc_point}\n")

        elif _input == 'p' and _random == 'paper':
            print(f"computer choice : {_random}")
            print("=========================================")
            print("tie")
            print("=========================================")
            print(f'\nYour point : {human_point}', f"\ncomputer's point : {pc_point}\n")

        elif _input == 'p' and _random == 'stone':
            print(f"computer choice : {_random}")
            print("=========================================")
            print("You won")
            print("=========================================")
            human_point = human_point + 1
            print(f'\nYour point : {human_point}',f"\ncomputer's point : {pc_point}\n")

        #when user input is scissor [C]

        elif _input == 'c' and _random == 'stone':
            print(f"computer choice : {_random}")
            print("=========================================")
            print("you lose")
            print("=========================================")
            pc_point = pc_point + 1
            print(f'\nYour point : {human_point}', f"\ncomputer's point : {pc_point}\n")


        elif _input == 'c' and _random == 'paper':
            print(f"computer choice : {_random}")
            print("=========================================")
            print("You won")
            print("=========================================")
            human_point = human_point + 1
            print(f'\nYour point : {human_point}',f"\ncomputer's point : {pc_point}\n")


        elif _input == 'c' and _random == 'scissor':
            print(f"computer choice : {_random}")
            print("=========================================")
            print("tie")
            print("=========================================")
            print(f'\nYour point : {human_point}', f"\ncomputer's point : {pc_point}\n")

        else:
            print("Invalid choice input")

        no_of_chances = no_of_chances + 1

        print(f"your left chances :  {chances - no_of_chances} out of {chances}")
    if pc_point < human_point:
        print("\nFINAL RESULT : YOU WON")
    elif pc_point > human_point:
        print('\nFINAL RESULT : YOU LOSE')
    else:
        print("\nFINAL RESULT : TIE")
    again()
def again():
    x = str(input("Do you want to again run the progarm [Y/N] : "))
    if x == 'y':
        whole_proram()
    elif x == "Y":
        whole_proram()
    elif x == 'N':
        quit()
    elif x == 'n':
        quit()
    else:
        again()
whole_proram()