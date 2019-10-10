#Radians and degrees
import math
from math import pi
from fractions import Fraction

def degrad():
    degrees2radians = int(input("Enter your degrees to be turned into radians: "))
    print("input: degree=",degrees2radians)
    rad = round((degrees2radians/180),5)
    rad = str(rad)
    radianfractionlength = list(str(Fraction(rad)))
    if (len(radianfractionlength)) > 7:
        print("output: ", degrees2radians,"/",180,"\u03C0")
    else:
        print(str(Fraction(rad)), "\u03C0")


def raddeg():
    radians2degrees = str(input("Enter your radians in it's pi form but without pi to be turned into degrees. All entries must be in fraction form i.e. 1 = 1/1: "))
    radianslength = list(radians2degrees)
    print("input: radian=",radians2degrees)
    neumorator = []    #arrays set and ready to be appended to
    denominater = []
    if "/" in radianslength:
        for pointer in range (len(radianslength)):
            if radianslength[pointer] == "/" :
                neumoratorEnd = pointer
                #print(neumoratorEnd)

                for count in range (0,neumoratorEnd):
                    neumorator.append(radianslength[count])
                for index in range (neumoratorEnd + 1 , len(radianslength)):
                    denominater.append(radianslength[index])

        singleNeumorator = int("".join(map(str, neumorator)))        #maps each value as a string and adds it
        singleDenominater = int("".join(map(str, denominater)))      #into the array. then turns it into an integer to be manipulated
        deg = round(((singleNeumorator)/(singleDenominater)*180))
        print("output: ",deg)

    else:
        print("ERROR RE-ENTER YOUR FRACTION")
        raddeg()  #recursion

degrad()