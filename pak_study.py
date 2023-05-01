
from os import system

import time







width=100
def pak():
    print("***Welcome to Pak-Studies quiz***".center(100))
    from os import system
    guesses = []
    correct_gusses = 0
    question_num = 0

    for key in pak_studies_questions:

        print("\n*************************************************")
        print(key)
        for i in pak_studies_options[question_num]:
            print(i)
        while True:
            guess = input("Enter a, b, c, or d: ")
            answers = ["A", "B", "C", "D"]
            guess = guess.upper()
            if guess not in answers:
                print("Try again")
                continue

            else:
                guesses.append(guess)
                system('cls')
                correct_gusses += check_answer(pak_studies_questions.get(key), guess)
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
    for i in pak_studies_questions:
        print(pak_studies_questions.get(i), end=" ")
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



pak_studies_questions = {
"1. urdu was declared national language of pakistan in:": "A",
"2. In which province maximum languages are spoken?": "D",
"3. Which urdu has been taken from the following languages?": "C",
"4. Word urdu means": "C",
"5. How many letters are there in urdu alphabets?": "C",
"6. Who composed the verses of pakistan national anthem?": "A",
"7. Which country to help pakistan introduce genetically_engineered corn?": "A",
"8. Prime minister Imran khan approves a grant of Rs____ billion for kamyab jawan national youth development programme:": "A",
"9. _____ resumes flights to pakistan in june,2019 after 10 years?": "A",
"10. Which country hosting FIFA women's world cup 2019?": "A"
}
pak_studies_options = [
["a. April 1954","b. April 1950", "c. April 1955",  "d. April 1952"],
["a. sindh", "b. punjab", "c. KPK","d. balochistan"],
["a. persian", "b. arabic", "c. turkish", "d. none of these"],
["a. believers", "b. a group of student", "c. army", "d. none of these"],
["a. 35", "b. 36", "c. 37", "d. 39"],
["a. Hafeez jallandri", "b. nasir kazmi", "c. allama iqbal", "d. faiz ahmed faiz"],
["a. china", "b. united states", "c. united kingdom", "d. none of these"],
["a. 1 billion", "b. 100 billions", "c. 10 billions", "d. none of these"],
["a. british airways", "b. qarar airways", "c. new york airways", "d. none of these"],
["a. france", "b. germany", "c. Russia", "d. None of these"]
]

pak()
while play_again():
    system('cls')
    from main import menue
    menue()
system('cls')    

print("GOOD BYEEE!!!".center(width))


