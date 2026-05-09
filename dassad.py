import requests 
import random
import html
API_URL="https://opentdb.com/api.php?amount=10&category=26&difficulty=easy&type=multiple"
def get_games():
    response=requests.get(API_URL)
    if response.status_code==200:
        data=response.json()
        if data["response_code"]==0 and data["results"]:
            return data["results"]
    return None
def run_quiz():
    questions=get_games()
    if not questions:
        print("Failed to fetch entertainment questions")
        return
    score=0
    print("welcome to celebrity quizzzzz")
    for i,q in enumerate(questions,1):
        question=html.unescape(q["question"])
        correct=html.unescape(q["correct_answer"])
        incorrects=[html.unescape(a)for a in q["incorrect_answers"]]
        options=incorrects+[correct]
        random.shuffle(options)
        print(f"question {i}:{question}")
        for j,option in enumerate(options,1):
          print(f"{j}.{option}")
        while True:
            try:
                choice=int(input("your answer(1-4)"))
                if 1<=choice<=4:
                    break
            except ValueError:
                pass
            print("invalid input")
        if options[choice-1]==correct:
            print("correct")
            score+=1
        else:
            print("wrong! corect answer is",correct)
    print("final score:",score/len(questions))
"run_quiz()"
def get_games():
    response=requests.get(API_URL)
    if response.status_code==200:
        data=response.json()
        if data["response_code"]==0 and data["results"]:
            return data["results"]
    return None
def run_quiz():
    questions=get_games()
    if not questions:
        print("Failed to fetch entertainment questions")
        return
    score=0
    print("welcome to celebrity quizzzzz")
    for i,q in enumerate(questions,1):
        question=html.unescape(q["question"])
        correct=html.unescape(q["correct_answer"])
        incorrects=[html.unescape(a)for a in q["incorrect_answers"]]
        options=incorrects+[correct]
        random.shuffle(options)
        print(f"question {i}:{question}")
        for j,option in enumerate(options,1):
          print(f"{j}.{option}")
        while True:
            try:
                choice=int(input("your answer(1-4)"))
                if 1<=choice<=4:
                    break
            except ValueError:
                pass
            print("invalid input")
        if options[choice-1]==correct:
            print("correct")
            score+=1
        else:
            print("wrong! corect answer is",correct)
    print("final score:",score/len(questions))
run_quiz()