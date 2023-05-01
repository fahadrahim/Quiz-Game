while True:
    from os import system
    u_name = str(input("Enter your name: "))
    if u_name.isdigit():
        system('cls')
        print("Enter a valid name")
        continue
    else:
        u_name = u_name.title()
        while True:
            
            u_age = str(input("Enter your age: "))
            system('cls')
            if u_age.isdigit(): 
                u_age = int(u_age)
                
                if u_age <= 18:




                    for i in range(100):
                        print('Loading...',i)
                        system('cls')
                    print(f"Hell00000 {u_name}")

                    from main import menue
                    menue()
                else:
                    print(f"Oops {u_name} you are 18+ this game is only for under 18\nGood Bye")
                    break
            else:
                print("Enter an valid age")
        break
            
        