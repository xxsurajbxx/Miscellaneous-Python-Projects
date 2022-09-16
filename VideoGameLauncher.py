from os import system
from time import sleep

while(True):
    system("cls")
    print("Enter the game you want to play: ")
    usrinput = input().lower()
    if usrinput == "exit":
        break
    if usrinput == "undertale":
        system("Start C:\\Users\\yoddl\\Downloads\\Games\\Undertale\\UNDERTALE.exe")
        break
    if usrinput == "getting over it":
        system("Start C:\\Users\\yoddl\\Downloads\\Games\\GettingOverIt\\GettingOverIt.exe")
        break
    else:
        system("cls")
        print("Invalid Input")
        print("Try Again")
        sleep(3)
        system("cls")