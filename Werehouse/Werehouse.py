helmet = 0
rifle = 0
medkit = 0

print('Hello in our werehouse')
while True:
    print("We have: " + str(helmet) + " helmets, " + str(rifle) + " rifles, and " + str(medkit) + " medkits"  )
    Temp = input("Type 1 to add or 2 for out item: ")
    if Temp == "1":

        Temp1 = input("Type item to add : ")
        if Temp1 == "helmet":
            Temp2 = input("how many helmets would You like to add :")
            helmet += int(Temp2)
        elif Temp1 == "rifle":
            Temp2 = input("how many rifles would You like to add :")
            rifle += int(Temp2)
        elif Temp1 == "medkit":
            Temp2 = input("how many medkits would You like to add :")
            medkit += int(Temp2)
        else:
            print("You give wrong imput, use: helmet, rifle or medkit, try again")

    elif Temp == "2":
        Temp1 = input("Type item to out : ")
        if Temp1 == "helmet":
            Temp2 = input("how many helmets would You like to out :")
            if helmet <= 0:
                print("there is no helmets!")
            else:
                helmet -= int(Temp2)
        elif Temp1 == "rifle":
            Temp2 = input("how many rifles would You like to out :")
            if rifle <= 0:
                print("there is no rifles!")
            else:
                rifle -= int(Temp2)
        elif Temp1 == "medkit":
            Temp2 = input("how many medkits would You like to out :")
            if medkit <= 0:
                print("there is no medkits!")
            else:
                medkit -= int(Temp2)
        else:
            print("You give wrong imput, try again")

    else:
        print("try again, we accept only 1 or 2: ")

    continue
