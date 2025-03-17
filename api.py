import requests
import html
import pandas as pd
url = "https://opentdb.com/api.php?amount=50&category=18&type=multiple"
response = requests.get(url)
data = response.json()

for i, question in enumerate(data["results"], start=1):
    print(f"Q{i}: {question['question']}")
    print(f"A: {question['correct_answer']}")
    print(question['incorrect_answers'])
    print("-" * 30)
questions_list=[]
for question in data['results']:
    questions_list.append({
            "Question":html.unescape(question['question']),
            "Correct Answer":html.unescape(question["correct_answer"]),
            "Incorrect Answer":[html.unescape(ans) for ans in question["incorrect_answers"]]



        })
df=pd.DataFrame(questions_list)
df.to_csv('Quizfile.csv',index=False,encoding="utf-8")