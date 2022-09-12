#Wprowadzenie danych -nazwa
print ("Welcome")
while True:
    s = input ("Please input product name\n")
    while not (1 <=len(s) < 60):
        if not s:
            print ("You didn't put any name\n")
        elif len(s) >60:
            print ("Incorrect name\n")
        s = input ("Please input correct product name\n")
    #Wprowadzenie danych -typ
    word_list = ['medkit', 'helmet', 'rifle']

    def get_word():
        print("Please choose the type from the following:")
        w_string = ",".join(word_list)
        print(w_string)

        while True:
            word = input("\n> ").lower().strip()
            if word in word_list:
                return word
            else:
                print(f"'{word}' is not in the list of words. Please choose from the following:\n{w_string}")
    word = get_word()
    print(word)
    #Wprowadzenie danych -ilość
    i = input ("Please input amount\n")
    #if i <= 0:  <---------  jak wylaczyc cyfre mniejsze od 0????
        #print("Incorrect amount\n")
    #podsumowanie
    print("Entered data")
    print("Product", s, "type", word, "amount", i )
        ans = 0
        askUserForNewItem = False
        while ans < 2:
            answer = input("Do You want add anything else? (yes or no)")
            if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
                print("OK")
                askUserForNewItem = True
            elif any(answer.lower() == f for f in ['no', 'n', '0']):
                print("Thank You. See You next time")
                askUserForNewItem = False
            else:
                ans += 1
                if ans < 2:
                    print('Please enter yes or no')
                else:
                    askUserForNewItem = False
        if not askUserForNewItem:
          break # that should end top-level `while True` loop