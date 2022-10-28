import random

"the random module allows me to create a set of dice rolls, created by pseudo-random values"
import math

"the math module is necessary for combinations, aka the nCr formula"

L = [1, 2, 3, 4, 5, 6]
"This list serves as the domain of numbers which I want the random module to choose from."
"Naturally, It's the numbers 1-6, which represent the six die-face values"


def binomcoef(n, k):
    if 0 <= k <= n:
        a = 1
        b = 1
        for t in range(1, min (k, n - k) + 1):
            a *= n
            b *= t
            n -= 1
        return a // b
    else:
        return 0


p1 = random.choice(L)
p2 = random.choice(L)
p3 = random.choice(L)
p4 = random.choice(L)
p5 = random.choice(L)
"This block of code picks pseudo-random numbers, from the previously defined list, and assigns the variables"

R = [p1, p2, p3, p4, p5]
"This new list of random values represents the player's deck"

print(" ")
print("your dice rolls:", "[", *R, "]")

amountone = R.count(1)
amounttwo = R.count(2)
amountthree = R.count(3)
amountfour = R.count(4)
amountfive = R.count(5)
amountsix = R.count(6)
"This block counts the amount of face values on the player's deck, and assigns them variables"


def chanceev(n, k):
    return (binomcoef(n, k)) * ((1 / 6) ** k) * ((5 / 6) ** (n - k))


sublist = []
k = 1
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALone = sum(sublist)

sublist = []
k = 2
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALtwo = sum(sublist)

sublist = []
k = 3
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALthree = sum(sublist)

sublist = []
k = 4
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALfour = sum(sublist)

sublist = []
k = 5
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALfive = sum(sublist)

sublist = []
k = 6
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALsix = sum(sublist)

sublist = []
k = 7
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALseven = sum(sublist)

sublist = []
k = 8
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALeight = sum(sublist)

sublist = []
k = 9
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALnine = sum(sublist)

sublist = []
k = 10
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALten = sum(sublist)

sublist = []
k = 11
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALeleven = sum(sublist)

sublist = []
k = 12
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALtwelve = sum(sublist)

sublist = []
k = 13
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALthirteen = sum(sublist)

sublist = []
k = 14
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALfourteen = sum(sublist)

sublist = []
k = 15
while k < 15:
    sublist.append(chanceev(15, k))
    k += 1

ALfifteen = sum(sublist)

print(" ")
print(" ")
print("===Possibilities of rolling 1's===")
print(" ")


def countingblock(amount, dicenum):
    if amount == 0:
        print("one", dicenum, ":", ALone)
    if amount >= 1:
        print("one", dicenum, ":", 1)

    if amount == 0:
        print("two", dicenum, "'s:", ALtwo)
    if amount == 1:
        print("two", dicenum, "'s:", ALone)
    if amount >= 2:
        print("two", dicenum, "'s:", 1)

    if amount == 0:
        print("three", dicenum, "'s:", ALthree)
    if amount == 1:
        print("three", dicenum, "'s:", ALtwo)
    if amount == 2:
        print("three", dicenum, "'s:", ALone)
    if amount >= 3:
        print("three", dicenum, "'s:", 1)

    if amount == 0:
        print("four", dicenum, "'s:", ALfour)
    if amount == 1:
        print("four", dicenum, "'s:", ALthree)
    if amount == 2:
        print("four", dicenum, "'s:", ALtwo)
    if amount == 3:
        print("four", dicenum, "'s:", ALone)
    if amount >= 4:
        print("four", dicenum, "'s:", 1)


    def display1(x, a, b, c, d, e, f):
        if amount == 0:
            print(x, dicenum, "'s:", f)
        if amount == 1:
            print(x, dicenum, "'s:", e)
        if amount == 2:
            print(x, dicenum, "'s:", d)
        if amount == 3:
            print(x, dicenum, "'s:", c)
        if amount == 4:
            print(x, dicenum, "'s:", b)
        if amount >= 5:
            print(x, dicenum, "'s:", a)


    display1("five", 1, ALone, ALtwo, ALthree, ALfour, ALfive)
    display1("six", ALone, ALtwo, ALthree, ALfour, ALfive, ALsix)
    display1("seven", ALtwo, ALthree, ALfour, ALfive, ALsix, ALseven)
    display1("eight", ALthree, ALfour, ALfive, ALsix, ALseven, ALeight)
    display1("nine", ALfour, ALfive, ALsix, ALseven, ALeight, ALnine)
    display1("ten", ALfive, ALsix, ALseven, ALeight, ALnine, ALten)
    display1("eleven", ALsix, ALseven, ALeight, ALnine, ALten, ALeleven)
    display1("twelve", ALseven, ALeight, ALnine, ALten, ALeleven, ALtwelve)
    display1("thirteen", ALeight, ALnine, ALten, ALeleven, ALtwelve, ALthirteen)
    display1("fourteen", ALnine, ALten, ALeleven, ALtwelve, ALthirteen, ALfourteen)
    display1("fifteen", ALten, ALeleven, ALtwelve, ALthirteen, ALfourteen, ALfifteen)
    display1("sixteen", ALeleven, ALtwelve, ALthirteen, ALfourteen, ALfifteen, 0)
    display1("seventeen", ALtwelve, ALthirteen, ALfourteen, ALfifteen, 0, 0)
    display1("eighteen", ALthirteen, ALfourteen, ALfifteen, 0, 0, 0)
    display1("nineteen", ALfourteen, ALfifteen, 0, 0, 0, 0)
    display1("twenty", ALfifteen, 0, 0, 0, 0, 0)


print(countingblock(amountone, 1))
print(" ")
print(" ")
print("===Possibilities of rolling 2's===")
print(" ")

print(countingblock(amounttwo, 2))

print(" ")
print(" ")
print("===Possibilities of rolling 3's===")
print(" ")

print(countingblock(amountthree, 3))

print(" ")
print(" ")
print("===Possibilities of rolling 4's===")
print(" ")

print(countingblock(amountfour, 4))

print(" ")
print(" ")
print("===Possibilities of rolling 5's===")
print(" ")

print(countingblock(amountfive, 5))

print(" ")
print(" ")
print("===Possibilities of rolling 6's===")
print(" ")

print(countingblock(amountsix, 6))