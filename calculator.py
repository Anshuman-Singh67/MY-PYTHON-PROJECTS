# calculator
def his_show() :
    with open("history.txt", "r") as file:
        d = file.read()
    if len(d) == 0 :
        print( "NO HISTORY FOUND !")
    else :
        print(d)

def his_clear() :
    with open("history.txt", "w"):
        pass
    print( "HISTORY CLEARED !")

def update(first , operator , second , answer) :
    with open("history.txt" , 'a') as filee :
        expression = first + operator + second + "=" + answer
        filee.write(expression + "\n")

# main part starts
check = True

while check :

    print ("WELCOME TO THE CALCULATOR !!")
    print(" ")
    print("ENTER THE OPERATION YOU WANT TO PERFORM(eg : 2 + 3) or ")
    print ("( + , - , * , / ) or (history , clear or exit )")
    print(" ")
    inp = (input("--> "))

    low_inp = inp.lower()
    lower_inp = low_inp.strip()
    exp = inp.split()

    if len(exp) > 1 :

        if exp[1] == "+":
            ans = int(exp[0]) + int(exp[2])
            print("THE ANSWER IS " , ans)
        elif exp[1] == "-" :
            ans = int(exp[0]) - int(exp[2])
            print("THE ANSWER IS " , ans)                                                                                                
        elif exp[1] == "*" :
            ans = int(exp[0]) * int(exp[2])
            print("THE ANSWER IS " , ans)
        elif exp[1] == "/" :
            ans = int(exp[0]) / int(exp[2])
            print("THE ANSWER IS " , ans)
        else:
            print("ENTER A VALID INPUT :(")
            check = False
            break

        update(str(exp[0]) , str(exp[1]) , str(exp[2]) , str(ans))
    else :
        if lower_inp == "history" :
            his_show()
            
        elif lower_inp == "clear" :
            his_clear()
            
        elif lower_inp == "exit" :
            check = False
            print("GOOD BYE !")
            break 
        else :
            print("ENTER A VALID INPUT :(")
            check = False
            break



    inp2 = input("DO YOU WANT TO CONTINUE ( YES / NO ) ?")
    inp3 = inp2.lower().strip()

    if inp3 == "no" :
        check = False
    
