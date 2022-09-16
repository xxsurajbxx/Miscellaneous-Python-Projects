write = open("Personalinfo.txt", "w")
ans = input('Type "Start" to Start Entering Personal Data: ')
user_info = []
while ans != "exit":
    fname = input("First name: ").lower()
    lname = input("Last name: ").lower()
    email = input("Email: ").lower()
    gender = input("Sex: ").lower()
    dob = input("Date of birth: ").lower()
    person_info = [fname, lname, email, gender, dob]
    print(person_info)
    validity = input("Is this information correct?").lower
    if validity == "no":
        person_info.clear()
        continue
    user_info.append(person_info)
    ans = input('Type "exit" to leave or press enter to continue with the next person: ')
writepersoninfo = str(user_info)
write.write(writepersoninfo)
