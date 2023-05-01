

from os import system

import time





print("***Welcome to Islamic_Studies quiz***".center(100))
width=100

def Islamic():
    from os import system
    guesses = []
    correct_gusses = 0
    question_num = 1

    for key in islamic_studies_questions:

        print("\n*************************************************")
        print(key)
        for i in islamic_studies_options[question_num - 1]:
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
                correct_gusses += check_answer(islamic_studies_questions.get(key), guess)
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
    for i in islamic_studies_questions:
        print(islamic_studies_questions.get(i), end=" ")
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



islamic_studies_questions = {
"1. For how many years, Prophet Muhammad(PBUH) lived in madinah?":"B",
"2. Prophet Muhammad(PBUH) belonged to which family":"A",
"3. In the beginning, to which Arab tribe Prophet Muhammad(PBUH) worked as a shepherd?":"A",
"4. Which Prophet is called the FATHER OF MUSLIMS?":"B",
"5. Which Prophet was able to talk with animals and jinns?":"C",
"6. How many Prophets are mentioned in the holy Quran?":"B",
"7. The color of the first Islamic flag was?":"A",
"8. After how many months of the migration of Prophet Muhammad(PBUH) to Madina the change of Qibla was occurred?":"D",
"9. Prophet Muhammad(PBUH) was born in the_____ year of Elephant.":"A",
"10. Which of the following first Muslim who migrated to Madina?":"A"
}


islamic_studies_options=[["a. 5","b. 10","c. 15","d. 20"],
["a. Hashmi","b. Quraishi","c. Makki","d. Madni"],
["a. Banu saad","b. Banu asad","c. Banu Ummayya","Banu Makhzoom"],
["a. Prophet Adam(A.S)","b. Prophet Ibraheem(A.S)","c. Prophet Ismaeel(A.S)","d. Prophet Sulaiman(A.S)"],
["a. Prophet Adam(A.S)","b. Prophet Ibraheem(A.S)","c. Prophet Sulaiman(A.S)","d. Prophet Daniyal(A.S)"],
["a. 16","b. 26","c. 36","d. 46"],
["a. white","b. black","c. white and black","d. green"],
["a. 12","b. 14","c. 16","d. 18"],
["a. first","b. second","c. third","d. fourth"],
["a. Hazrat Abu Salam(RA)","b. Hazrat Talha(RA)","c. Hazrat Bilal(RA)","d. Hazrat Umar(RA)"]

]


Islamic()
while play_again():
    system('cls')
    from main import menue
    menue()

system('cls')    

print("GOOD BYEEE!!!!".center(width))
