import time


ascii_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k',
              'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '`', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', '0', '-', '=', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Q', 'W', 'E',
              'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"',
              'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']
character_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
                  'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F',
                  'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
character_and_number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i',
                             'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
                             'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
                             'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
number_and_special_character_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', ']', '\\', ';', "'", ',',
                                     '.', '/', '`', '-', '=', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                                     '_', '+', '{', '}', '|', ':', '"', '<', '>', '?']
character_and_special_character_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h',
                                        'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y',
                                        'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C',
                                        'V', 'B', 'N', 'M', '[', ']', '\\', ';', "'", ',', '.', '/', '`', '-', '=', '~',
                                        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':',
                                        '"', '<', '>', '?']
special_character_list = ['[', ']', '\\', ';', "'", ',', '.', '/', '`', '-', '=', '~', '!', '@', '#', '$', '%', '^',
                          '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?']
number_of_combos = 0
thingy = None
failure = True
while True:
    print("How Many Characters are in This Password?")
    num_of_chars = int(input('>>> '))
    print("Does the Password Consist of Letters, Numbers, or Special Characters?")
    print("Type L for letters, N for numbers, SC for special characters and + for a combination of these (no spaces)")
    combo = input(">>> ").upper()
    start_time = time.time()
    if combo == 'L+N+SC' or combo == 'L+SC+N' or combo == 'N+L+SC' or combo == 'N+SC+L' or combo == 'SC+L+N' or \
            combo == 'SC+N+L':
        if num_of_chars == 1:
            for char_1 in ascii_list:
                print(char_1)
        if num_of_chars == 2:
            for char_1 in ascii_list:
                for char_2 in ascii_list:
                    print(char_1, char_2)
        if num_of_chars == 3:
            for char_1 in ascii_list:
                for char_2 in ascii_list:
                    for char_3 in ascii_list:
                        print(char_1, char_2, char_3)
        if num_of_chars == 4:
            for char_1 in ascii_list:
                for char_2 in ascii_list:
                    for char_3 in ascii_list:
                        for char_4 in ascii_list:
                            print(char_1, char_2, char_3, char_4)
        if num_of_chars == 5:
            for char_1 in ascii_list:
                for char_2 in ascii_list:
                    for char_3 in ascii_list:
                        for char_4 in ascii_list:
                            for char_5 in ascii_list:
                                print(char_1, char_2, char_3, char_4, char_5)
        if num_of_chars == 6:
            for char_1 in ascii_list:
                for char_2 in ascii_list:
                    for char_3 in ascii_list:
                        for char_4 in ascii_list:
                            for char_5 in ascii_list:
                                for char_6 in ascii_list:
                                    print(char_1, char_2, char_3, char_4, char_5, char_6)
        number_of_combos = len(ascii_list) ** num_of_chars
        thingy = ''
        failure = False
    if combo == 'L+N' or combo == 'N+L':
        if num_of_chars == 1:
            for char_1 in character_and_number_list:
                print(char_1)
        if num_of_chars == 2:
            for char_1 in character_and_number_list:
                for char_2 in character_and_number_list:
                    print(char_1, char_2)
        if num_of_chars == 3:
            for char_1 in character_and_number_list:
                for char_2 in character_and_number_list:
                    for char_3 in character_and_number_list:
                        print(char_1, char_2, char_3)
        if num_of_chars == 4:
            for char_1 in character_and_number_list:
                for char_2 in character_and_number_list:
                    for char_3 in character_and_number_list:
                        for char_4 in character_and_number_list:
                            print(char_1, char_2, char_3, char_4)
        if num_of_chars == 5:
            for char_1 in character_and_number_list:
                for char_2 in character_and_number_list:
                    for char_3 in character_and_number_list:
                        for char_4 in character_and_number_list:
                            for char_5 in character_and_number_list:
                                print(char_1, char_2, char_3, char_4, char_5)
        if num_of_chars == 6:
            for char_1 in character_and_number_list:
                for char_2 in character_and_number_list:
                    for char_3 in character_and_number_list:
                        for char_4 in character_and_number_list:
                            for char_5 in character_and_number_list:
                                for char_6 in character_and_number_list:
                                    print(char_1, char_2, char_3, char_4, char_5, char_6)
        number_of_combos = len(character_and_number_list) ** num_of_chars
        thingy = 'Character and Digit '
        failure = False
    if combo == 'SC+N' or combo == 'N+SC':
        if num_of_chars == 1:
            for char_1 in number_and_special_character_list:
                print(char_1)
        if num_of_chars == 2:
            for char_1 in number_and_special_character_list:
                for char_2 in number_and_special_character_list:
                    print(char_1, char_2)
        if num_of_chars == 3:
            for char_1 in number_and_special_character_list:
                for char_2 in number_and_special_character_list:
                    for char_3 in number_and_special_character_list:
                        print(char_1, char_2, char_3)
        if num_of_chars == 4:
            for char_1 in number_and_special_character_list:
                for char_2 in number_and_special_character_list:
                    for char_3 in number_and_special_character_list:
                        for char_4 in number_and_special_character_list:
                            print(char_1, char_2, char_3, char_4)
        if num_of_chars == 5:
            for char_1 in number_and_special_character_list:
                for char_2 in number_and_special_character_list:
                    for char_3 in number_and_special_character_list:
                        for char_4 in number_and_special_character_list:
                            for char_5 in number_and_special_character_list:
                                print(char_1, char_2, char_3, char_4, char_5)
        if num_of_chars == 6:
            for char_1 in number_and_special_character_list:
                for char_2 in number_and_special_character_list:
                    for char_3 in number_and_special_character_list:
                        for char_4 in number_and_special_character_list:
                            for char_5 in number_and_special_character_list:
                                for char_6 in number_and_special_character_list:
                                    print(char_1, char_2, char_3, char_4, char_5, char_6)
        number_of_combos = len(number_and_special_character_list) ** num_of_chars
        thingy = 'Digit and Special Character '
        failure = False
    if combo == 'SC+L' or combo == 'L+SC':
        if num_of_chars == 1:
            for char_1 in character_and_special_character_list:
                print(char_1)
        if num_of_chars == 2:
            for char_1 in character_and_special_character_list:
                for char_2 in character_and_special_character_list:
                    print(char_1, char_2)
        if num_of_chars == 3:
            for char_1 in character_and_special_character_list:
                for char_2 in character_and_special_character_list:
                    for char_3 in character_and_special_character_list:
                        print(char_1, char_2, char_3)
        if num_of_chars == 4:
            for char_1 in character_and_special_character_list:
                for char_2 in character_and_special_character_list:
                    for char_3 in character_and_special_character_list:
                        for char_4 in character_and_special_character_list:
                            print(char_1, char_2, char_3, char_4)
        if num_of_chars == 5:
            for char_1 in character_and_special_character_list:
                for char_2 in character_and_special_character_list:
                    for char_3 in character_and_special_character_list:
                        for char_4 in character_and_special_character_list:
                            for char_5 in character_and_special_character_list:
                                print(char_1, char_2, char_3, char_4, char_5)
        if num_of_chars == 6:
            for char_1 in character_and_special_character_list:
                for char_2 in character_and_special_character_list:
                    for char_3 in character_and_special_character_list:
                        for char_4 in character_and_special_character_list:
                            for char_5 in character_and_special_character_list:
                                for char_6 in character_and_special_character_list:
                                    print(char_1, char_2, char_3, char_4, char_5, char_6)
        number_of_combos = len(character_and_special_character_list) ** num_of_chars
        thingy = 'Character and Special Character '
        failure = False
    if combo == 'L':
        if num_of_chars == 1:
            for char_1 in character_list:
                print(char_1)
        if num_of_chars == 2:
            for char_1 in character_list:
                for char_2 in character_list:
                    print(char_1, char_2)
        if num_of_chars == 3:
            for char_1 in character_list:
                for char_2 in character_list:
                    for char_3 in character_list:
                        print(char_1, char_2, char_3)
        if num_of_chars == 4:
            for char_1 in character_list:
                for char_2 in character_list:
                    for char_3 in character_list:
                        for char_4 in character_list:
                            print(char_1, char_2, char_3, char_4)
        if num_of_chars == 5:
            for char_1 in character_list:
                for char_2 in character_list:
                    for char_3 in character_list:
                        for char_4 in character_list:
                            for char_5 in character_list:
                                print(char_1, char_2, char_3, char_4, char_5)
        if num_of_chars == 6:
            for char_1 in character_list:
                for char_2 in character_list:
                    for char_3 in character_list:
                        for char_4 in character_list:
                            for char_5 in character_list:
                                for char_6 in character_list:
                                    print(char_1, char_2, char_3, char_4, char_5, char_6)
        number_of_combos = len(character_list) ** num_of_chars
        thingy = 'Character '
        failure = False
    if combo == 'N':
        if num_of_chars == 1:
            for char_1 in number_list:
                print(char_1)
        if num_of_chars == 2:
            for char_1 in number_list:
                for char_2 in number_list:
                    print(char_1, char_2)
        if num_of_chars == 3:
            for char_1 in number_list:
                for char_2 in number_list:
                    for char_3 in number_list:
                        print(char_1, char_2, char_3)
        if num_of_chars == 4:
            for char_1 in number_list:
                for char_2 in number_list:
                    for char_3 in number_list:
                        for char_4 in number_list:
                            print(char_1, char_2, char_3, char_4)
        if num_of_chars == 5:
            for char_1 in number_list:
                for char_2 in number_list:
                    for char_3 in number_list:
                        for char_4 in number_list:
                            for char_5 in number_list:
                                print(char_1, char_2, char_3, char_4, char_5)
        if num_of_chars == 6:
            for char_1 in number_list:
                for char_2 in number_list:
                    for char_3 in number_list:
                        for char_4 in number_list:
                            for char_5 in number_list:
                                for char_6 in number_list:
                                    print(char_1, char_2, char_3, char_4, char_5, char_6)
        number_of_combos = len(number_list) ** num_of_chars
        thingy = 'Digit '
        failure = False
    if combo == 'SC':
        if num_of_chars == 1:
            for char_1 in special_character_list:
                print(char_1)
        if num_of_chars == 2:
            for char_1 in special_character_list:
                for char_2 in special_character_list:
                    print(char_1, char_2)
        if num_of_chars == 3:
            for char_1 in special_character_list:
                for char_2 in special_character_list:
                    for char_3 in special_character_list:
                        print(char_1, char_2, char_3)
        if num_of_chars == 4:
            for char_1 in special_character_list:
                for char_2 in special_character_list:
                    for char_3 in special_character_list:
                        for char_4 in special_character_list:
                            print(char_1, char_2, char_3, char_4)
        if num_of_chars == 5:
            for char_1 in special_character_list:
                for char_2 in special_character_list:
                    for char_3 in special_character_list:
                        for char_4 in special_character_list:
                            for char_5 in special_character_list:
                                print(char_1, char_2, char_3, char_4, char_5)
        if num_of_chars == 6:
            for char_1 in special_character_list:
                for char_2 in special_character_list:
                    for char_3 in special_character_list:
                        for char_4 in special_character_list:
                            for char_5 in special_character_list:
                                for char_6 in special_character_list:
                                    print(char_1, char_2, char_3, char_4, char_5, char_6)
        number_of_combos = len(special_character_list) ** num_of_chars
        thingy = 'Special Character '
        failure = False
    if failure is True:
        print('Invalid Answer, Try Again')
        continue
    break
print(f"There are {number_of_combos} Combinations for a {num_of_chars} {thingy}Password")
time = int(time.time() - start_time)

hours = time/3600;
time = time%3600;
minutes = time/60;
time = time%60;
seconds = time;
print(f"it took {hours} hours, {minutes} minutes, and {seconds} seconds")
