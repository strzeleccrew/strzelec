helmet = 0
rifle = 0
medkit = 0

print('Hello in our werehouse')
while True:
    print("We have: " + str(helmet) + " helmets, " + str(rifle) + " rifles, and " + str(medkit) + " medkits"  )
    user_choice = input("Type 1 to add or 2 for out item: ")
    if user_choice == "1":

        input_type = input("Type item to add : ")
        if input_type == "helmet":
            item_count = input("how many helmets would You like to add :")
            if int(item_count) <= 0:
                print("use positive number!")
            else:
                helmet += int(item_count)
        elif input_type == "rifle":
            item_count = input("how many rifles would You like to add :")
            if int(item_count) <= 0:
                print("use positive number!")
            else:
                rifle += int(item_count)
        elif input_type == "medkit":
            item_count = input("how many medkits would You like to add :")
            if int(item_count) <= 0:
                print("use positive number!")
            else:
                medkit += int(item_count)
        else:
            print("You give wrong imput, use: helmet, rifle or medkit, try again")

    elif user_choice == "2":
        input_type = input("Type item to out : ")
        if input_type == "helmet":
            item_count = input("how many helmets would You like to out :")
            if int(item_count) >= helmet:
                print("there is no helmets or its count is too low!")
            else:
                helmet -= int(item_count)
        elif input_type == "rifle":
            item_count = input("how many rifles would You like to out :")
            if int(item_count) >= rifle:
                print("there is no rifles or its count is too low!")
            else:
                rifle -= int(item_count)
        elif input_type == "medkit":
            item_count = input("how many medkits would You like to out :")
            if int(item_count) >= medkit:
                print("there is no medkits or its count is too low!")
            else:
                medkit -= int(item_count)
        else:
            print("You give wrong imput, use: helmet, rifle or medkit, try again")

    else:
        print("try again, we accept only 1 or 2: ")
