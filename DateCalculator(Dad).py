class Date:
    def __init__(self, month, day, year, daystoadd, nxtmonth, nxtday, nxtyear):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        self.daystoadd = int(daystoadd)
        self.nxtmonth = int(nxtmonth)
        self.nxtday = int(nxtday)
        self.nxtyear = int(nxtyear)
    def isLeapYear():        if self.year%400==0:            return True        if self.year%100==0:            return False        if self.year%4==0:            return True    
    def valid(self):
        if self.year > 0 and isinstance(self.year, int) is True:
            if self.month <= 12:
                thirtyone = [1, 3, 5, 7, 8, 10, 12]
                thirty = [4, 6, 9, 11]
                if self.day <= 31 and self.month in thirtyone:
                    return True
                if self.day <= 30 and self.month in thirty:
                    return True
                if self.day <= 29 and self.month == 2 and self.isLeapYear() is True:
                    return True
                if self.day <= 28 and self.month == 2:
                    return True
                else:
                    return False

    def adddays(self):
        thirtyone = [1, 3, 5, 7, 8, 10, 12]
        thirty = [4, 6, 9, 11]
        self.day += self.daystoadd
        while (self.day > 31 and self.month in thirtyone
               or self.day > 30 and self.month in thirty
               or self.day > 29 and self.month == 2 and self.isLeapYear() is True
               or self.day > 28 and self.month == 2 and self.isLeapYear() is False):
            if self.day > 31 and self.month in thirtyone:
                self.day -= 31
                self.month += 1
            if self.day > 30 and self.month in thirty:
                self.day -= 30
                self.month += 1
            if self.day > 29 and self.month == 2 and self.isLeapYear() is True:
                self.day -= 29
                self.month += 1
            if self.day > 28 and self.month == 2 and self.isLeapYear() is False:
                self.day -= 28
                self.month += 1
            if self.month > 12:
                self.month -= 12
                self.year += 1
                continue
        print(f"{self.month}/{self.day}/{self.year}")

   # def daysuntil(self):



print("Enter a date")
usrmon = input("Month>>")
usrday = input("Day>>")
usryr = input("Year>>")
usradd = input("Add days>>")
usrdate = Date(usrmon, usrday, usryr, usradd, 0, 0, 0)
print("""To use date functions enter:
    Validation
    Show Future Date
    Days Until""")
print("If You Made A Mistake, Press Enter")
usraccuracy = False
while usraccuracy is False:
    response = input("""    >>""").lower()
    if response == "validation":
        validity = usrdate.valid()
        if validity is True:
            print("Date is Valid")
            break
        if validity is not True:
            print("Date is Not Valid")
            break
    if response == "show future date":
        usrdate.adddays()
        break
    if response == "days until":
        usrnxtmon = input("Second Date Month>>")
        usrnxtday = input("Second Date Day>>")
        usrnxtyr = input("Second Date Year>>")
        usrdate = Date(usrmon, usrday, usryr, usradd, usrnxtmon, usrnxtday, usrnxtyr)
        usrdate.daysuntil()
    else:
        print("Error, Write Your Command Again")
        usraccuracy = False
