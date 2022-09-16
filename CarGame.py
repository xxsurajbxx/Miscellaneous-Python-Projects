user_input = ""
caron = False
while True:
    user_input = input().lower()
    if user_input == "start":
            if caron:
                print("Car is already on")
            else:
                caron = True
                print("car is starting")
    elif user_input == "stop":
        if not caron:
            print("Car is already off")
        else:
            caron = False
            print("Car has stopped")
    elif user_input == "help":
        print("to start car, type start")
        print("to stop car, type stop")
        print("type quit to exit")

    elif user_input == "quit":
        break
    elif user_input == "broke ass nibba":
        print("get rich nibba")
    else:
        print("This is not a valid input")
        print('for list of commands, type "help"')