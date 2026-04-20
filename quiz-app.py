import json
import random

valid_answers = ["A","B","C","D"]

def load_questions():
    with open("example.json", "r") as f:
        data = json.load(f)
        random.shuffle(data)
    return data

def ask_question(question):
    while True:
        s = input(f"Question: {question['question']}\nA: {question['options'][0]}\nB: {question['options'][1]}\nC: {question['options'][2]}\nD: {question['options'][3]}\n")
        s = s.strip().upper()

        if s in valid_answers:
            s = valid_answers.index(s)
            if s == question['answer']:
                return True
            else:
                inp = input("\nYou answered incorrectly, do you want to retry? Yes/No... ")
                inp = inp.strip().upper()
                if inp != "YES":
                    return False
                    
        else:
            print("\nYou have written an invalid answer\n")

def run_quiz(data):
    score = 0
    for question in data:
        if ask_question(question):
            score += 1
        print(f"Current progress: {score}/{len(data)}\n")
    return score

    


def show_results(score, total):
    percentage = round(score/total * 100, 2)
    grade = ["A","B","C","D","F"]
    if percentage >= 90:
        grade = grade[0]
    elif percentage <90 and percentage >= 75:
        grade = grade[1]
    elif percentage <75 and percentage >= 50:
        grade = grade[2]
    elif percentage <50 and percentage >= 30:
        grade = grade[3]
    else:
        grade = grade[4]
    
    print(f"Final score: {score}/{total}")
    print(f"Percentage: {percentage}%")
    print(f"Grade: {grade}")

data = load_questions()
score = run_quiz(data)
show_results(score, len(data))