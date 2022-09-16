from os import system
from time import sleep


def spin_skull():
    while True:
        print("""
          _____
         /     \\
        | () () |
         \\ ^  /
          |||||
          |||||
        """)
        sleep(0.125)
        system('cls')
        print("""
          _____
         /     \\
        |   ()  |
         \\__ ^ |
             |||
             |||
        """)
        sleep(0.125)
        system('cls')
        print("""
          _____
         /     \\
        |       |
         \\____  >
               |
               |
        """)
        sleep(0.125)
        system('cls')
        print("""
          _____
         /     \\
        |       |
         \\    /
          |||||
          |||||
        """)
        sleep(0.125)
        system('cls')
        print("""
          _____
         /     \\
        |       |
        <  ____/ 
         |
         |
        """)
        sleep(0.125)
        system('cls')
        print("""
          _____
         /     \\
        |  ()   |
        | ^  __/
         |||
         |||
        """)
        sleep(0.125)
        system('cls')
        ans = input().lower()
        if ans == "":
            continue
        if ans == 'stop':
            break


def spin_stick():
    while True:
        print("/")
        sleep(0.125)
        system('cls')
        print("-")
        sleep(0.125)
        system('cls')
        print("""\\""")
        sleep(0.125)
        system('cls')
        print("-")
        sleep(0.125)
        system('cls')
        ans = input().lower()
        if ans == "":
            continue
        if ans == 'stop':
            break
