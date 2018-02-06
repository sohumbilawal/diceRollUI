from random import *
import heapq
import time

from tkinter import *

window = Tk()

d1 = 0
d2 = 0
d3 = 0

#i = 0


aDice = []
dDice = []

def diceRollA(num):
    i = 0
    while (i < num):
        die = randint(1,6)
        aDice.extend([die])
        i += 1
    #aDice.extend([max(aDice)])
    aRollT.insert(END, aDice)
    return aDice

def diceRollD(num):
    i = 0
    while (i < num):
        die = randint(1,6)
        dDice.extend([die])
        i += 1
    #aDice.extend([max(aDice)])
    dRollT.insert(END, dDice)
    return dDice

#aDice = [d1, d2, d3]

#for die in aDice:
#    die = randint(1,6)
#    aDice[i] = die
#    i +=1
#x = randint(1,6)

#d1 = aDice[0]
#d2 = aDice[1]
#d3 = aDice[2]
def resolve():

    global aTroops, dTroops, delay
    aTroops = int(aTroopsIn.get())
    dTroops = int(dTroopsIn.get())
    delay = int(delayIn.get())

    while aTroops >= 0 or dTroops >= 0:

    #    if aTroops > 3:
    #        numADice = 3
    #    elif aTroops <= 3:
    #        numADice = aTroops
    #    print(numADice, aTroops)

    #    if dTroops > 2:
    #        numDDice = 2
    #    elif dTroops <= 2:
    #        numDDice = dTroops
    #    print(numDDice, dTroops)

        if aTroops >= 3 and dTroops >= 2:
            aDice = []
            dDice = []

            #statusT.insert(END, "Rolling 3 attacking dice: " + diceRollA(3))
            #statusT.insert(END, "Rolling 2 defending dice: " + diceRollD(2))
            aDice = diceRollA(3)
            dDice = diceRollD(2)

            #aRollT.insert(END, aDice)

            highA = heapq.nlargest(2, aDice[0:len(aDice)])

            maxA = highA[0]
            max2A = highA[1]
            #statusT.insert(END, "The highest attacker roll is: {0}, and second highest is: {1}".format(maxA, max2A))
            maxAT.insert(END, maxA)
            max2AT.insert(END, max2A)

            highD = heapq.nlargest(2, dDice[0:len(dDice)])
            maxD = highD[0]
            max2D = highD[1]

            maxDT.insert(END, maxD)
            max2DT.insert(END, max2D)

            #print("The highest defender roll is: {0}, and second highest is: {1}".format(maxD, max2D))

            if maxD >= maxA and max2D >= max2A:
                aTroops = aTroops - 2
            elif maxD >= maxA and max2D < max2A:
                aTroops = aTroops - 1
                dTroops = dTroops - 1
            elif maxD < maxA and max2D >= max2A:
                dTroops = dTroops - 1
                aTroops = aTroops - 1
            elif maxD < maxA and max2D < max2A:
                dTroops = dTroops - 2

            statusT.insert(END, "aTroops" + "dTroops")

        elif aTroops >= 3 and dTroops == 1:
            aDice = []
            dDice = []

            print("Rolling 3 attacking dice: ", diceRollA(3))
            print("Rolling 1 defending dice: ", diceRollD(1))

            highA = heapq.nlargest(2, aDice[0:len(aDice)])
            maxA = highA[0]
            max2A = highA[1]
            print("The highest attacker roll is: {0}, and second highest is: {1}".format(maxA, max2A))

            maxD = max(dDice)
            print("The highest defender roll is: {0}".format(maxD))

            if maxD >= maxA:
                aTroops = aTroops - 1
            elif maxD < maxA:
                dTroops = dTroops - 1

            print (aTroops, dTroops)

        elif aTroops == 2 and dTroops == 2:
            aDice = []
            dDice = []

            print("Rolling 2 attacking dice: ", diceRollA(2))
            print("Rolling 2 defending dice: ", diceRollD(2))

            highA = heapq.nlargest(2, aDice[0:len(aDice)])
            maxA = highA[0]
            max2A = highA[1]
            print("The highest attacker roll is: {0}, and second highest is: {1}".format(maxA, max2A))

            highD = heapq.nlargest(2, dDice[0:len(dDice)])
            maxD = highD[0]
            max2D = highD[1]
            print("The highest defender roll is: {0}, and second highest is: {1}".format(maxD, max2D))

            if maxD >= maxA and max2D >= max2A:
                aTroops = aTroops - 2
            elif maxD >= maxA and max2D < max2A:
                aTroops = aTroops - 1
                dTroops = dTroops - 1
            elif maxD < maxA and max2D >= max2A:
                dTroops = dTroops - 1
                aTroops = aTroops - 1
            elif maxD < maxA and max2D < max2A:
                dTroops = dTroops - 2

            print (aTroops, dTroops)

        elif aTroops == 2 and dTroops == 1:
            aDice = []
            dDice = []

            print("Rolling 2 attacking dice: ", diceRollA(2))
            print("Rolling 1 defending dice: ", diceRollD(1))

            highA = heapq.nlargest(2, aDice[0:len(aDice)])
            maxA = highA[0]
            max2A = highA[1]
            print("The highest attacker roll is: {0}, and second highest is: {1}".format(maxA, max2A))

            maxD = max(dDice)
            print("The highest defender roll is: {0}".format(maxD))

            if maxD >= maxA:
                aTroops = aTroops - 1
            elif maxD < maxA:
                dTroops = dTroops - 1

            print (aTroops, dTroops)

        elif aTroops == 1 and dTroops == 2:
            aDice = []
            dDice = []

            print("Rolling 1 attacking die: ", diceRollA(1))
            print("Rolling 2 defending dice: ", diceRollD(2))

            maxA = max(aDice)
            print("The highest attacker roll is: {0}".format(maxA))

            highD = heapq.nlargest(2, dDice[0:len(dDice)])
            maxD = highD[0]
            max2D = highD[1]
            print("The highest defender roll is: {0}, and second highest is: {1}".format(maxD, max2D))

            if maxD >= maxA:
                aTroops = aTroops - 1
            elif maxD < maxA:
                dTroops = dTroops - 1

            print (aTroops, dTroops)

        elif aTroops == 1 and dTroops == 1:
            aDice = []
            dDice = []

            print("Rolling 1 attacking die: ", diceRollA(1))
            print("Rolling 1 defending dice: ", diceRollD(1))

            maxA = max(aDice)
            print("The highest attacker roll is: {0}".format(maxA))

            maxD = max(dDice)
            print("The highest defender roll is: {0}".format(maxD))

            if maxD >= maxA:
                aTroops = aTroops - 1
            elif maxD < maxA:
                dTroops = dTroops - 1

            print (aTroops, dTroops)

        else:
            break

        time.sleep(delay)

    if aTroops > dTroops:
        resultT.insert(END, "Attacking army wins!")
        aTroopsS = str(aTroops)
        result2T.insert(END, "Troops left: " + aTroopsS)
        #print("Attacking army wins! Troops left: {0}".format(aTroops))
    elif dTroops > aTroops:
        resultT.insert(END, "Defending army wins!")
        dTroopsS = str(dTroops)
        result2T.insert(END, "Troops left: " + dTroopsS)
        #print("Defending army wins! Troops left: {0}".format(dTroops))




aTroopsIn = IntVar()
aTroopsEn = Entry(window, textvariable = aTroopsIn)
aTroopsEn.grid(row = 0, column = 0)

dTroopsIn = IntVar()
dTroopsEn = Entry(window, textvariable = dTroopsIn)
dTroopsEn.grid(row = 0, column = 1)

delayIn = IntVar()
delayEn = Entry(window, textvariable = delayIn)
delayEn.grid(row = 1, column = 0)
#numADice = 3
#numDDice = 2
resolve = Button(window, text = "Resolve Battle", command = resolve)
resolve.grid(row = 2, column = 1)


aRollT = Text(window, height = 1, width = 20)
aRollT.grid(row = 3, column = 0)

dRollT = Text(window, height = 1, width = 20)
dRollT.grid(row = 4, column = 0)

maxAT = Text(window, height = 1, width = 20)
maxAT.grid(row = 3, column = 1)

max2AT = Text(window, height = 1, width = 20)
max2AT.grid(row = 3, column = 2)

maxDT = Text(window, height = 1, width = 20)
maxDT.grid(row = 4, column = 1)

max2DT = Text(window, height = 1, width = 20)
max2DT.grid(row = 4, column = 2)

statusT = Text(window, height = 1, width = 20)
statusT.grid(row = 5, column = 0)

resultT = Text(window, height = 1, width = 20)
resultT.grid(row = 6, column = 0)

result2T = Text(window, height = 1, width = 20)
result2T.grid(row = 6, column = 1)

window.mainloop()
#aHeap = heapq.heapify(aDice)
#highA = heapq.nlargest(2, aDice[0:len(aDice)])
#maxA = highA[0]
#max2A = highA[1]
#print("The highest attacker roll is: {0}, and second highest is: {1}".format(maxA, max2A))
#print(aDice)

#print(aDice)
#print(d1, d2, d3)
#print("MAX: " , max(aDice))
