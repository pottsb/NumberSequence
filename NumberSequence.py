# Written by Peter B

def calculateSequence(inputNumber):
    print(inputNumber)
    oldNumber = inputNumber
    for x in range(5):
        newNumber = 0.5 * (oldNumber+(2/oldNumber))
        print("%.6f" % newNumber)
        oldNumber = newNumber

def getNumber():
    while True:
        try:
            inputNumber = float(input("Pick a number between 0.5 and 5.5: "))
            if inputNumber < 0.5:
                print("That number is too small.")
            elif inputNumber > 5.5:
                print("That number is too big.")
            else: 
                break
        except ValueError:
            print("That doesn't look like a number to me.")
    return inputNumber

calculateSequence(getNumber())