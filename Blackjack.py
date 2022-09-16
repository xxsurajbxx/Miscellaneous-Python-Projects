from random import randint
from os import system
from time import sleep


def add_up_cards(player_cards):
    card_values = {
        "Ace of Clubs": 1,
        "Ace of Diamonds": 1,
        "Ace of Hearts": 1,
        "Ace of Spades": 1,
        "Ace of Clubs1": 11,
        "Ace of Diamonds1": 11,
        "Ace of Hearts1": 11,
        "Ace of Spades1": 11,
        "King of Clubs": 13,
        "King of Diamonds": 13,
        "King of Hearts": 13,
        "King of Spades": 13,
        "Queen of Clubs": 12,
        "Queen of Diamonds": 12,
        "Queen of Hearts": 12,
        "Queen of Spades": 12,
        "Jack of Clubs": 11,
        "Jack of Diamonds": 11,
        "Jack of Hearts": 11,
        "Jack of Spades": 11,
        "10 of Clubs": 10,
        "10 of Diamonds": 10,
        "10 of Hearts": 10,
        "10 of Spades": 10,
        "9 of Clubs": 9,
        "9 of Diamonds": 9,
        "9 of Hearts": 9,
        "9 of Spades": 9,
        "8 of Clubs": 8,
        "8 of Diamonds": 8,
        "8 of Hearts": 8,
        "8 of Spades": 8,
        "7 of Clubs": 7,
        "7 of Diamonds": 7,
        "7 of Hearts": 7,
        "7 of Spades": 7,
        "6 of Clubs": 6,
        "6 of Diamonds": 6,
        "6 of Hearts": 6,
        "6 of Spades": 6,
        "5 of Clubs": 5,
        "5 of Diamonds": 5,
        "5 of Hearts": 5,
        "5 of Spades": 5,
        "4 of Clubs": 4,
        "4 of Diamonds": 4,
        "4 of Hearts": 4,
        "4 of Spades": 4,
        "3 of Clubs": 3,
        "3 of Diamonds": 3,
        "3 of Hearts": 3,
        "3 of Spades": 3,
        "2 of Clubs": 2,
        "2 of Diamonds": 2,
        "2 of Hearts": 2,
        "2 of Spades": 2
    }
    card_val = 0
    for c in player_cards:
        card_val += card_values.get(c)
    return card_val


def blackjack():
    loss = False
    user_cards = []
    deck = []
    aces = []
    is_nigger = False
    suits = ["Diamonds", "Spades", "Clubs", "Hearts"]
    face_cards = ["Jack", "Queen", "King"]
    for suit in suits:
        deck.append(f"Ace of {suit}")
        aces.append(f"Ace of {suit}")
        for faces in range(len(face_cards)):
            deck.append(f"{face_cards[faces]} of {suit}")
        for card in range(2, 11):
            deck.append(f"{card} of {suit}")
    while True:
        system('cls')
        print('Press Enter to play')
        print('Type "rules" for an explanation of how the game works')
        print('Type "Exit" to end session')
        start = input(">>>")
        sleep(0.5)
        system("cls")
        if start == "":
            for x in range(2):
                card = deck[randint(0, len(deck)-1)]
                deck.remove(card)
                print(card)
                if card in aces:
                    while True:
                        print(f"Would you like the {card} to be 1 or 11?")
                        user_answer = input(">>>")
                        sleep(0.5)
                        system('cls')
                        if user_answer == '1':
                            user_cards.append(card)
                            break
                        if user_answer == '11':
                            user_cards.append(card + "1")
                            break
                        else:
                            print('Please enter a valid answer')
                            continue
                else:
                    user_cards.append(card)
            system('cls')
            user_score = add_up_cards(user_cards)
            while loss is False:
                user_score = add_up_cards(user_cards)
                for i in range(len(user_cards)):
                    print(user_cards[i])
                print("Hit or Stand?")
                user_answer = input(">>>")
                sleep(0.5)
                system('cls')
                if user_answer == "hit":
                    card = deck[randint(0, len(deck)-1)]
                    deck.remove(card)
                    if card in aces:
                        while True:
                            print(f"Would you like the {card} to be 1 or 11?")
                            user_ans = input(">>>").lower()
                            sleep(0.5)
                            system('cls')
                            if user_ans == "1":
                                user_cards.append(card)
                                break
                            if user_ans == "11":
                                user_cards.append(card.append("1"))
                                break
                            else:
                                print('Please enter a valid answer')
                                sleep(1)
                                system('cls')
                                continue
                    else:
                        user_cards.append(card)
                if user_answer == "stand":
                    user_score = add_up_cards(user_cards)
                    if is_nigger is True:
                        print("You Won")
                        print("Congratulations")
                        sleep(3)
                        system('cls')
                        user_score = 0
                        user_cards = []
                        is_nigger = False
                        break
                    if user_score == 21:
                        print("You Won")
                        print("Congratulations")
                        sleep(3)
                        system('cls')
                        user_score = 0
                        user_cards = []
                        break
                    if 18 < user_score < 21:
                        win_or_loss = randint(1, 5)
                        if win_or_loss < 5:
                            print("You Won")
                            print("Congratulations")
                            sleep(3)
                            system('cls')
                            user_score = 0
                            user_cards = []
                            break
                        else:
                            print("You Lost")
                            print("Feels Bad")
                            sleep(3)
                            system('cls')
                            loss = True
                            user_score = 0
                            user_cards = []
                            break
                    if 15 < user_score <= 18:
                        win_or_loss = randint(1, 2)
                        if win_or_loss == 1:
                            print("You Won")
                            print("Congratulations")
                            sleep(3)
                            system('cls')
                            user_score = 0
                            user_cards = []
                            break
                        else:
                            print("You Lost")
                            print("Feels Bad")
                            sleep(3)
                            system('cls')
                            loss = True
                            user_score = 0
                            user_cards = []
                            break
                    if 10 < user_score <= 15:
                        win_or_loss = randint(1, 4)
                        if win_or_loss == 1:
                            print("You Won")
                            print("Congratulations")
                            sleep(3)
                            system('cls')
                            user_score = 0
                            user_cards = []
                            break
                        else:
                            print("You Lost")
                            print("Feels Bad")
                            sleep(3)
                            system('cls')
                            loss = True
                            user_score = 0
                            user_cards = []
                            break
                    if 5 < user_score <= 10:
                        win_or_loss = randint(1, 10)
                        if win_or_loss == 1:
                            print("You Won")
                            print("Congratulations")
                            sleep(3)
                            system('cls')
                            user_score = 0
                            user_cards = []
                            break
                        else:
                            print("You Lost")
                            print("Feels Bad")
                            sleep(3)
                            system('cls')
                            loss = True
                            user_score = 0
                            user_cards = []
                            break
                    if user_score <= 5:
                        win_or_loss = randint(1, 20)
                        if win_or_loss == 1:
                            print("You Won")
                            print("Congratulations")
                            sleep(3)
                            system('cls')
                            user_score = 0
                            user_cards = []
                            break
                        else:
                            print("You Lost")
                            print("Feels Bad")
                            sleep(3)
                            system('cls')
                            loss = True
                            user_score = 0
                            user_cards = []
                            break
                    if user_score > 21:
                        print("You Lost")
                        print("Feels Bad")
                        print(f"your score was {user_score}")
                        sleep(3)
                        system('cls')
                        loss = True
                        user_score = 0
                        user_cards = []
                        break
                if user_answer == 'nigger':
                    print('Taco')
                    sleep(1)
                    print('Burrito')
                    sleep(1)
                    print('Large Niggerito')
                    sleep(1)
                    system('cls')
                    is_nigger = True
                if user_answer != 'hit' and user_answer != 'stand' and user_answer != 'nigger':
                    print("Please enter a valid answer")
                    sleep(1)
                    system('cls')
        if start == "rules":
            print("""
            You will be dealt 2 cards
            You will then be faced with a choice
            Hit or Stand
            if you hit, you will get another card with the risk of losing
            if you stand then your cards will be compared with that of your opponent
            the winner is whoever gets 21 or gets closest to 21
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


# TODO: Fix bug, after first game, the game starts bugging out, saying invalid answer or constantly restarting game
blackjack()