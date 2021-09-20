import random

colour = ["Red", "Green", "Blue", "Orange", "Yellow", "Purple"]


def ans_gen():  # This function is used to generate the answers of the game
    ans = [colour[random.randint(0, 5)], colour[random.randint(0, 5)], colour[random.randint(0, 5)],
           colour[random.randint(0, 5)]]
    return ans


answer = ans_gen()


print(answer)  # This is for testing purposes and supposed to be commented out in the final version


def get_ans():  # This function is used to get input from the user and store it in a list.
    ans1 = input("Please input a colour and capitalize the first letter of the colour. E.g:Red.")
    ans2 = input("Please input a colour and capitalize the first letter of the colour. E.g:Red.")
    ans3 = input("Please input a colour and capitalize the first letter of the colour. E.g:Red.")
    ans4 = input("Please input a colour and capitalize the first letter of the colour. E.g:Red.")
    return [ans1, ans2, ans3, ans4]


def game():  # This is main game function used to contain the game logic and variables
    tries = 1
    while True:
        player_ans = get_ans()
        correct_ans = 0
        correct_colour = 0
        ans_check = []
        check2 = []

        for pos_check in range(0, len(answer)):  # This for loop is used to check whether the answer has the correct
            # position and colour.
            if player_ans[pos_check] == answer[pos_check]:
                correct_ans = correct_ans + 1

        for color_check in range(0, 4):  # This loop is used to iterate answers into ans_check and compare with
            # answers each time it loops
            if player_ans[color_check] in answer and player_ans[color_check] != answer[color_check]:
                ans_check.append(player_ans[color_check])
                check2.append(answer[color_check])

        for i in range(len(check2)):
            if ans_check[i] in check2 and ans_check[i] != check2:
                correct_colour = correct_colour + 1

        if [player_ans] == [answer]:    # To validate the answer so that it is the same as the generated combination
            print()
            print("Congratulations, your answers are all correct. You took " + str(tries) + " tries to finish the game.")
            break
        else:
            print("Please guess again.")
            print("Correct colour in the correct place:" + str(correct_ans))
            print("Correct colour but in the wrong place:" + str(correct_colour))
            tries = tries + 1


def main_menu():  # This function is used to create a main menu and user interface for the Mastermind game.
    print("This is a Mastermind game.The colours used in this game is Red, Green, Blue, Orange, Yellow, Purple.")
    print("Press 1 to start the game, 2 to learn how to play the game and, 3 to quit the game.")

    while True:
        try:
            run = int(input())  # Allows the user to type in numbers to run the game.
            if run == 1:
                game()
            elif run == 2:
                print(
                    "Mastermind is played by guessing the 4 colours generated  in the correct order. There will be "
                    "clues provided to assist you in guessing the correct answer. There is repeated colors in the game")
                print()
                main_menu()
            elif run == 3:
                print("The game will now exit.")
                exit()
            else:
                print("Please enter a valid number.")
                main_menu()

        except ValueError:
            print("Please do not type anything other than numbers.")


while True:
    main_menu()
