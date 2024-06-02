import random


def main():
    while True:
        print("\nHome Menu")
        print("1. Treasure Island Game")
        print("2. Rock, Paper, & Scissor game")
        print("3. Quit")
              
        pilihan = input("Choose Options (1-3): ")

        if pilihan == '1':
            treasure_island()
        elif pilihan == '2':
            rock_paper_scissor()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
    


# Game Treasure Island
def treasure_island():   
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 

    #https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
    print("You are at a crossroad. Where do you want to go 'Left' or 'Right'?")
    direction = input("Type 'left' or 'right': ").lower()
    if direction == "left":
            print("You have come to a lake. There is an island in the middle of the lake. Type 'wait' or 'swim'")
            direction = input("Type 'wait' or 'swim': ").lower()
            
            if direction == "wait":
                        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and blue. Which colour do you choose?")
                        direction = input("Type 'red', 'yellow' or 'blue': ").lower()
                        
                        if direction == "red":
                            print("It's a room full of fire. Game Over.")
                        elif direction == "yellow":
                            print("You found the treasure! You Win!")
                        else:
                            print("It's a room full of snake. Game Over.")
                                
            else:
                print("You get attacked by an angry trout. Game Over.")
                                
    elif direction == "right":
        print("You fell into a hole. Game over!")
    else:
        print("Please Type Right or Left")
        


#Game Rock, Paper, & Scissor      
def rock_paper_scissor():
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    game_images = [rock, paper, scissors]
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    if user_choice == 0:
        print(game_images[0])
    elif user_choice == 1:
        print(game_images[1])
    elif user_choice == 2:
        print(game_images[2])
    else:
        print("Invalid choice")

    ran_num = random.randint(0, 2) #random number of computer choice
    if ran_num == 0:
        print("Computer chose:\n" + game_images[0])
    elif ran_num == 1:
        print("Computer chose:\n" + game_images[1])
    elif ran_num == 2:
        print("Computer chose:\n" + game_images[2])

    # Logic result
    if user_choice == 0 and ran_num == 2:
        print("You win!")
    elif user_choice == 1 and ran_num == 0:
        print("You win!")
    elif user_choice == 2 and ran_num == 1:
        print("You win!")
    elif user_choice == ran_num:
        print("It's a draw")
    else:
        print("You lose")
        
if __name__ == "__main__":
    main()
