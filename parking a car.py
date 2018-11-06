#car park

import time
import random

cpark   = [
            ["","","","",""],
            ["","","","",""],
            ["","","","",""],
            ["","","","",""],
            ["","","","",""],
            ]

def displaygrid():
    for i in range(5):
        print(cpark[i])

def makegrid(x,y):
    for i in range(5):
        for j in range(5):
            cpark[x][y] = "0"
    print("")
    print("")

def grid():
    for l in range(5):
            for m in range(5):
                cpark[l][m] = "0"

def reqpspace():
    col = int(input("What column are you parked in?"))
    row = int(input("What row are you parked in?"))
    reg = str.lower(input("Please enter your registration"))
    coll = col - 1
    roww = row - 1
    cpark[coll][roww] = reg
    displaygrid()
    print("")
    print("")

def retcar():
    retract = str.lower(input("Would you like to remove your car?"))
    valid = False
    while valid == False:
        if retract == "yes":
            retreg = str.lower(input("Please enter your registration"))
            for n in range(5):
                for o in range(5):
                    if retreg == cpark[n][o]:
                        cpark[n][o] = "0"
                        displaygrid()
                        valid = True
        else:
            print("Car will remain where it is")
            valid = False

def auto():
    col = random.randint(1,5)
    row = random.randint(1,5)
    reg = str.lower(input("Please enter your registration"))
    coll = col - 1
    roww = row - 1
    if cpark[coll][roww] != "0":
        work = False
        while work == False:
            if cpark[coll][roww] != "0":
                col = random.randint(1,5)
                row = random.randint(1,5)
                coll = col - 1
                roww = row - 1
                if cpark[coll][roww] != "0":
                    work = False
                else:
                    work = True

    cpark[coll][roww] = reg
    displaygrid()
    print("")
    print("")

grid()
displaygrid()

print("Available spaces are shown with a '0'.")

entercar = str.lower(input("Would you like to enter a car to the carpark?"))

while entercar == "yes":
    autopark = str.lower(input("Enter 'yes' to have your car parked by an attendent. If you'd like your car to be driven by you into the car park please enter 'okay'."))

    if autopark == "yes":
        auto()
    else:
        manualpark = str.lower(input("Enter yes if you would you like to drive your own car and park it yourself?"))
        if manualpark == "yes":
            reqpspace()
    time.sleep(1)
    entercar = str.lower(input("Would you like to enter a car to the carpark?"))

time.sleep(5)

ayr = str.lower(input("Are you ready to take your car out yet?"))
time.sleep(2)
while ayr == "no":
    ayr = str.lower(input("Are you ready to take your car out yet?"))
    time.sleep(2)

retcar()



