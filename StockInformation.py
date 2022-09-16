from pandas_datareader import DataReader
from datetime import datetime, timedelta
from matplotlib.pyplot import show
from os import system


end = datetime.now()
providestimeframe = False
understand = False
while understand is False:
    print("Welcome to Suraj's Intuitive Stock Market API")
    usrinpt = input()
    if usrinpt.lower() == "help":
        print("First Type List or Show, Then Enter the ticker, After That, Enter the timeframe that you would like\nFor Example, List ATVI 10 years")
        system("pause")
        system("cls")
    else:
        break
usrinpt = usrinpt.split()
for x in range(len(usrinpt)-1):
    if usrinpt[x+1].lower() == "years" or usrinpt[x+1].lower() == "year":
        start = datetime.now() - timedelta(days=int(usrinpt[x])*365)
        providestimeframe = True
        break
    if usrinpt[x+1].lower() == "weeks" or usrinpt[x+1].lower() == "week":
        start = datetime.now() - timedelta(days=int(usrinpt[x])*7)
        providestimeframe = True
        break
    if usrinpt[x+1].lower() == "days" or usrinpt[x+1].lower() == "day":
        start = datetime.now() - timedelta(days=int(usrinpt[x]))
        providestimeframe = True
        break
if providestimeframe is False:
    start = datetime.now() - timedelta(days=1)
df = DataReader(usrinpt[1].upper(), "yahoo", start, end)
if usrinpt[0].lower() == "list":
    print(df)
if usrinpt[0].lower() == "show":
    df["Close"].plot()
    show()