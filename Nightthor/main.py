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
        w_string = ""
        for w in word_list:
            w_string += w + ', '
        print(w_string[:-1])

        while True:
            word = input("\n> ")
            word = word.lower().strip()
            if word in word_list:
                return word
            else:
                print("'%s' is not in the list of words. Please choose from the following:\n%s" % (word, w_string[:-1]))
    word = get_word()
    print(word)
    #Wprowadzenie danych -ilość
    i = input ("Please input amount\n")
    #if i <= 0:  <---------  jak wylaczyc cyfre mniejsze od 0????
        #print("Incorrect amount\n")
    #podsumowanie
    print("Entered data")
    print("Product", s, "type", word, "amount", i )
    def question():
        ans = 0
        while ans < 2:
            answer = input("Do You want add anything else? (yes or no)")
            if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
                print("OK")
            elif any(answer.lower() == f for f in ['no', 'n', '0']):
                print("Thank You. See You next time")
            else:
                ans += 1
                if ans < 2:
                    print('Please enter yes or no')
                else:
                    print("Nothing done")