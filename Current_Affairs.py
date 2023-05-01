

from os import system

import time





print("***Welcome to Current-Affairs quiz***".center(100))
width=100

def CA():
    from os import system
    guesses = []
    correct_gusses = 0
    question_num = 1

    for key in current_affairs_questions:

        print("\n*************************************************")
        print(key)
        for i in current_affairs_questions_options[question_num - 1]:
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
                correct_gusses += check_answer(current_affairs_questions.get(key), guess)
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
    for i in current_affairs_questions:
        print(current_affairs_questions.get(i), end=" ")
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




current_affairs_questions ={
"1. Why now india can't use atomic bombs against pakistan?":"D",
"2. Which political party isn't accepting the results of 6th pakistan population sense?":"B",
"3. Paradise leaks has disclosed the off shore company of former prime minister of pakistan?":"C",
"4. FATA has become the part of______?":"A",
"5. New GHQ is being built in____?":"C",
"6. Hazara province movement is continue in which province of pakistan?":"C",
"7. Daughter of Sanam Bhutto has joined______ profession?":"D",
"8. CPEC has ___ routes?":"A",
"9. Motor bike ambulance service has been launched in _____province?":"B",
"10. Which coal power plant is considered as to be the cause of smog?":"B"

}
current_affairs_questions_options = [
["a. because we have hydrogen bomb","b. due to our missile program","c. due to support of china","d. due to our submarine which can carry atomic missiles"],
["a. PML N","b. MQM pakistan","c. PPP","d. PTI"],
["a. Nawaz sharif","b. ch shujat hussain","c. shaukat aziz","d. raja parvez ashraf"],
["a. KPK","b. GB","c. AJK","d. FANA"],
["a. rawalpindi","b. lahore","c. islamabad","d. abbottabad"],
["a. sindh","b. punjab","c. KPK","BALOchistan"],
["a. legal","b. banking","c. teaching","d. modeling"],
["a. 2","b. 3","c. 4","d. 1"],
["a. KPK","b. punjab","c. sindh","d. balochistan"],
["a. thar coal power plant","b. sahiwal coal power plant","c. sui coal power plant","d. none of these"]
    
]

CA()

while play_again():
    system('cls')
    from main import menue
    menue()

system('cls')    

print("GOOD BYEEEE!!!!".center(width))

