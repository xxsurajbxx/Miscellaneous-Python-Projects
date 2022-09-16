from os import system
from time import sleep


while True:
    print('Press Enter to play')
    print('Type "rules" for an explanation of how the game works')
    print('Type "Exit" to end session')
    start = input(">>>")
    sleep(0.5)
    system("cls")
    if start == "":
        loss = False
        while loss is False:
            # main loop
            pass
    if start == "rules":
        print("""
        
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
