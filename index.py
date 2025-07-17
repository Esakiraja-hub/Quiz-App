import json

def load_questions():
    with open('index.json', 'r') as file:
        return json.load(file)
    
def run_quiz(questions):
    score = 0
    for q in questions:
        print(q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        answer = input("Your answer (1-4): ")
        
        if q["options"][int(answer)-1] == q["answer"]:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was: {q['answer']}\n")
    print(f"Your final score: {score}/{len(questions)}")

questions = load_questions()
run_quiz(questions)