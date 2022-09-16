from os import system
from time import sleep


def print_character(number_of_lives):
    if number_of_lives == 5:
        print("""
+---+
|   |
    |
    |
    |
    |
=========
        """)
    if number_of_lives == 4:
        print("""
+---+
|   |
O   |
    |
    |
    |
=========
""")
    if number_of_lives == 3:
        print("""
+---+
|   |
O   |
|   |
    |
    |
=========
""")
    if number_of_lives == 2:
        print("""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""")
    if number_of_lives == 1:
        print("""
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========
""")


def list_to_string(lst):
    str(lst)
    string = ''.join(lst)
    return string


def isvalid(user_answer):
    if len(user_answer) == 1 and isinstance(user_answer, str) is True:
        return True
    else:
        return False


def check(user_answer='', list_of_blanks=None, letters=None):
    if letters is None:
        letters = []
    if list_of_blanks is None:
        list_of_blanks = []
    edited_list_of_letters = letters
    x = False
    for letter in letters:
        if letter == user_answer:
            list_of_blanks[edited_list_of_letters.index(user_answer)] = user_answer
            edited_list_of_letters[edited_list_of_letters.index(user_answer)] = '_'
            x = True
    if x is False:
        return False
    elif x is True:
        str(list_of_blanks)
        list_of_blanks = ''.join(list_of_blanks)
        return list_of_blanks


def hangman():
    while True:
        print('Press Enter to play')
        print('Type "Rules" for an explanation of how the game works')
        print('Type "Exit" to end session')
        start = input(">>>")
        sleep(0.5)
        system("cls")
        if start == "":
            print('Enter the secret word or phrase')
            answer = input('>>>')
            sleep(0.5)
            system('cls')
            letter_list = list(answer)
            blanks_list = list(answer)
            copy_of_blanks_list = list(answer)
            for letter_from_list in letter_list:
                if letter_from_list != ' ':
                    blanks_list[blanks_list.index(letter_from_list)] = '_'
                    copy_of_blanks_list[copy_of_blanks_list.index(letter_from_list)] = '_'
            blanks_string = list_to_string(blanks_list)
            lives = 5
            while True:
                if copy_of_blanks_list == letter_list:
                    print('You Won')
                    print('Congratulations')
                    sleep(1)
                    system('cls')
                    break
                if lives == 0:
                    print("You Lost")
                    print("Feels Bad")
                    sleep(0.5)
                    system('cls')
                    break
                print_character(lives)
                print(blanks_string)
                while True:
                    print('Enter your guess')
                    guess = input('>>>')
                    sleep(0.5)
                    system('cls')
                    validity = isvalid(guess)
                    if validity is False:
                        print('Please enter a valid answer')
                        sleep(1)
                        system('cls')
                        continue
                    if validity is True:
                        break
                correctness = check(guess, blanks_list, letter_list)
                if correctness is False:
                    print("Incorrect")
                    print("Feels Bad")
                    lives -= 1
                    sleep(0.5)
                    system('cls')
                else:
                    print("Correct")
                    print("Congratulations")
                    blanks_string = correctness
                    sleep(0.5)
                    system('cls')
        if start == "rules":
            print("""
    You will choose a phrase or word
    You have 5 guesses to guess a letter in the phrase or word
    If your guess is in the phrase or word then you don't lose a guess for that attempt
    If not, you will have one less guess and your character gets one step closer to hanging himself
            """)
            sleep(10)
            system('cls')
        if start == 'exit':
            break
        elif start != 'exit' and start != 'rules' and start != '':
            print("Please enter a valid answer")
            sleep(1)
            system('cls')
    system("cls")
    print("Peace Out Wigga")
