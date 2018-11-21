# binomial expantion
import numpy as np
import math


def collectterms(ncrstore, ApowerArray, BpowerArray):
    terms = []
    for pointer in range (len(ncrstore)):
        individualterm = ncrstore[pointer-1] * ApowerArray[pointer-1] * BpowerArray[pointer-1]
        terms.append(individualterm)
        print(terms)
    terms.remove(0)
    print(terms)

def BXpower(ValueB, ValueZ, operator, ncrstore, ApowerArray):
    BpowerArray = [] # array for the b power
    if operator == 'plus': #if ValueB is positive
        for power in range (0, ValueZ): # for loop to get each power value
            ThePower = pow(ValueB, power) #pow function puts ValueB to the power f power
            BpowerArray.append(ThePower) #adds each power to the end of the list
    elif operator == 'minus': #if ValueB is negative
        numpValueB = np.array(ValueB)# turns array into a numpy to be manipulated
        negnumpValueB = np.negative(numpValueB)
        for counter in range (0, ValueB):
            ThePower = pow(negnumpValueB, counter)
            BpowerArray.append(ThePower)
    collectterms(ncrstore, ApowerArray, BpowerArray)


def Apower(ValueA, ValueZ, ValueB, operator, ncrstore):
    ApowerArray = []# keep array out of loop!
    for power in range (0,ValueZ): #goes from 0 to zvalue
        ThePower = pow(ValueA, power)
        ApowerArray.insert(0,ThePower)#enters each new power t0 start of the array
    BXpower(ValueB, ValueZ, operator, ncrstore, ApowerArray)

def nCr(ValueZ, ValueA, ValueB, operator):#z
    n = ValueZ
    r = -1 #so that r starts at 0
    ncrstore = []
    for i in range (n + 1): #so that it goes right to the end of the n values
        r = r + 1#to step up through values
        f = math.factorial
        ncrtemp = f(n) / f(r) / f(n-r)#nCr formula
        ncrstore.append(ncrtemp)
    Apower(ValueA, n, ValueB, operator, ncrstore)

#find zwithin formula/ list
def findz(splitgenform, ValueA, ValueB, operator):
    for pointer in range (len(splitgenform)): #runs pointer through list to find '^'
        if splitgenform[pointer] == "^":
            zsector = pointer + 1 #makes zsector the value after '^'
            ValueZ = ""
            for counter in range (zsector, len(splitgenform)):#runs frm value til the end of splitgenform
                ValueZ = ValueZ + str(splitgenform[counter])#adds all values to 'ValueZ'
    ValueZ = int(ValueZ)#ints the string
    nCr(ValueZ, ValueA, ValueB, operator)

#finds b in formula
def findb(splitgenform, ValueA): #imports splitgenform
    for pointer in range (len(splitgenform)):
        if splitgenform[pointer] == "+":
            bsectorstart = pointer
            operator = "plus" # for later use t determine sign
        elif splitgenform[pointer] == "-":
            bsectorstart = pointer
            operator = "minus" # for later use to determine sign
        elif splitgenform[pointer] == "x":
            bsectorend = pointer-1 #so the x isnt included
            ValueB = "" #entered into a string
            for counter in range (bsectorstart, bsectorend):
                ValueB = ValueB + str(splitgenform[counter+1]) #loop through and add all digits for b
            ValueB = int(ValueB) #int the string
    findz(splitgenform, ValueA, ValueB, operator)

#only constent is first '(' at position 0

#find a in the formula
def finda(): #imports splitgenform
    #Enters general formula. Should be at least 7 characters long.
    print("Please enter your general formula of binomial you wish to expand. Write in the form of '(a+bx)^z: ")
    genform = input()
    splitgenform = list(genform) #splits genform by character

    for pointer in range (len(splitgenform)):
        if splitgenform[pointer] == "+" or splitgenform[pointer] == "-": ##TURN INTO AN ARRAY
            asectorend = pointer #so the +- isnt included
            ValueA = "" #entered into a string
            for count in range (1,asectorend):
                ValueA = ValueA + (splitgenform[count])#finds whole value of a
    ValueA = int(ValueA) #int the string
    findb(splitgenform, ValueA)

finda()

def logs():
    typelog = input("All logs must be to base 10: Are you entering a simple log in the form 'Log X' if so enter '1' OR a complex log in the form of 'Y Log X' if so enter '2': ")

    if typelog == "1":
        slog = input("Please enter your simple log.Please do not write log, just enter the value of x: ") #slog = simple log
        ansslog = math.log10(slog)#ansslg = answer to simple log
        print(ansslog)

    elif typelog == "2":
        clogy = int(input("Please enter your complex log.Please do not write log, enter in your Y value: "))#clog = complex log
        clogx = int(input("Please enter in your X value"))
        pclog = pow(clogx, clogy)
        ansclog = math.log10(pclog)
        print(ansclog)

def degrad():
    degrees2radians = int(input("Enter your degrees to be turned into radians(to 2 decimal places): "))#converts degrees to radians
    rad = round(math.radians(degrees2radians),2)
    print(rad)

def raddeg():
    radians2degrees = int(input("Enter your radians to be turned into degrees(to 2 decimal places): "))#converts radians to degrees
    deg = round(math.degrees(radians2degrees),2)
    print(deg)
