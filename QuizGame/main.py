from question_model import Question
from data import question_data

question_bank = []

for question in question_data:

    question_text = question["text"]
    question_answer = question["answer"]

    q = Question(question_text, question_answer)
    question_bank.append(q)

print(question_bank[0].text)