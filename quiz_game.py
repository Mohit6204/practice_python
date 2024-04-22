questions={
    "Who created Python?: ":"A",
    "What year was Python created?:":"B",
    "Python is tributed to which comedy group?: ":"C",
    "Is the Earth round?: ":"A"
}
options=[["A. Guido van Rossum","B.Elon Musk","C. Bill Gates","D. Mark Zukerberg"],
         ["A. 1989","B. 1991","C. 2000","D. 2010"],
         ["A. Lonely Island", "B. Smosh", "C. Monty Python","D. SNL"],
         ["A. True","B. False","C. Sometimes","D. What's Earth?"]]

print("----------------------------------------------------")

def calculate_score(players_answers):
    score=0
    i=0
    for value in questions.values():
        if value==players_answers[i]:
            score+=1
        i+=1
    score*=100
    score/=4
    return int(score)

number=0
players_answers=[]
for key in questions.keys():
    print(key)
    for guess in options[number]:
        print(guess)
    guessed_answer=input("Choose option A, B, C or D\n")
    players_answers.append(guessed_answer)
    number+=1
    print("----------------------------------------------------")

print("Correct answers are: ")
for values in questions.values():
    print(values,end=' ')
print('\n')
print("Your guesses are: ")
for players_guesses in players_answers:
    print(players_guesses,end=' ')
print('\n')
print("Your final score is",calculate_score(players_answers),"%")