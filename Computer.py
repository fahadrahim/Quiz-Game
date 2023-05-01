def comp():
       
    from os import system

    import time





    print("***Welcome to Computer Science quiz***".center(100))
    width=100

    def Computer_Sci():
        from os import system
        guesses = []
        correct_gusses = 0
        question_num = 1

        for key in computer_questions:

            print("\n*************************************************")
            print(key)
            for i in computer_options[question_num - 1]:
                print(i)
            while True:
                guess = input("Enter a, b, c, or d: ")
                answers = ["A","B","C","D"]
                guess = guess.upper()
                if guess not in answers:
                    print("Try again")
                    continue

                else:
                    guesses.append(guess)
                    system('cls')
                    correct_gusses += check_answer(computer_questions.get(key), guess)
                    question_num += 1
                    time.sleep(2)
                    system('cls')
                    break
            continue

        display_score(correct_gusses, guesses)


    def check_answer(answer, gusses):
        if answer == gusses:
            print("CORRECT!")
            return 5
        else:
            print("WRONG!")

            return 0


    def display_score(correct_gusses, guesses):
        print("Result")
        print("Answers: ", end=" ")
        for i in computer_questions:
            print(computer_questions.get(i), end=" ")
        print("\nGusses: ", end=" ")
        for i in guesses:
            print(i, end=" ")
        score = correct_gusses
        print("\nYour score is: ", score)


    def play_again():
        response = input("Do you want to play again? (Yes/No)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False



    computer_questions = {
        "1. who is the father of computer?":"B",
        "2. who is the father of internet?":"B",
        "3. A light sensitive device that convert drawing.printed text or other images into digital form is ______?":"B",
        "4. WWW stands for____?":"D",
        "5. What type of operating system MS-DOS is?":"A",
        "6. Which technology is used in compact disks?":"B",
        "7. MS-Word is an example of_____?":"C",
        "8. What is the full form of CPU?":"C",
        "9. Which of the following language does the computer understands?":"C",
        "10. Which of the following is the brain of the computer?":"A"

        }

    computer_options = [["a. allen turning","b.charles babbage","c. simur cray","d.Augusta adaming"],
        ["a. charles babbage","b. Vint cerf","c. Denis Riche","d. Martin Cooper"],
        ["a. keyboard","b. scanner","c. OMR","d. none of these"],
        ["a.World Whole Web","b. Wide World Web","c. Web World Wide","d. World Wide Web"],
        ["a. Command line interface","b. Graphical user interface","c.multitasking","d. menu driven interface"],
        ["a. mechanical","b. electrical","c. electro magnetic","d. laser"],
        ["a. an operatinng sysem","b. A peocessing device","c. Application software","d. An impact device"],
        ["a. computer processing unit","b. computer principle unit","c. central processing unit","d. control processing unit"],
        ["a. only C language","b. only assembly language","c. only binary language","d. only BASIC"],
        ["a. central processing unit","b. memory","c. arithmetic and logic unit","d. control unit"]]
        
     
    Computer_Sci()
    while play_again():
        system('cls')
        from main import menue
        menue()
    

    system('cls')    

    print("GOOD BYEEEE!!!!".center(width))
    
comp()



