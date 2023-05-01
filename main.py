
def menue():
    
   
    
    
    from os import system
    
    import time
    width=100


    while True:
        print("\t\t\t****Welcome to the quiz game****")





        print("""\t\t***Select a subject below and enjoy the quiz***
        \nNote:- Here all questions are MCQs based\n
        \n1.Computer\n2.Current affairs\n3.Islamic-Studies\n4.Pak-Studies\n5.Exit""")
        select=str(input("\tEnter 1, 2, 3, 4 or 5: "))
        if select == '1':
            system('cls')
            from Computer import comp
            comp()
            break

        elif select == '2':
            system('cls')
            from Current_Affairs import CA
            CA()
        elif select == '3':
            system('cls')
            from Islamic_Studies import Islamic
            Islamic()
            break
        elif select == '4':
            system('cls')
            from pak_study import pak
            pak()
        elif select == '5':
            system('cls')
            print("GOOD BYEEEEE!!! ".center(width))

            
            break
        break
    
menue()