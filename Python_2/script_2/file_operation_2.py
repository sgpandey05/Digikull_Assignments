
from typing import Counter

while True:
    select = int(input("enter number between 1 to 10 :"))
    if select in range(1, 11):
        print("You have selected {}".format(select))
        f = open("numbers/{}.txt".format(select), "r")
        print(f.read())
        break

    elif select >10 or select <1:
        print("Incorrect Input")
        print("Please select number between 1 and 10 : {}".format(select))
