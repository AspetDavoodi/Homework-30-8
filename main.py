def getvariables():

    while True:
        numberofVar = input("How many integers would you like to input?")

        if numberofVar.isnumeric():
            Variablelist = []
            while int(numberofVar) != 0:
                while True:
                    number = input("Please input number in list")
                    if number.isnumeric():
                        Variablelist.append(int(number))
                        numberofVar = int(numberofVar) - 1
                        break
                    else:
                        print ("Invalid input!")
            break
        else:
            print("INVALID INPUT!")

    return Variablelist

def memberSum(givenlist):
    summedlist = []
    prevmember = 0
    for member in givenlist:
        nextmember = prevmember + member
        prevmember = member
        summedlist.append(nextmember)

    return summedlist

def main():
    listofVar = getvariables()
    sumList = memberSum(listofVar)
    print (sumList)

main()
