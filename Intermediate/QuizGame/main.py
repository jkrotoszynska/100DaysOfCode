from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:

    question_text = question["text"]
    question_answer = question["answer"]

    q = Question(question_text, question_answer)
    question_bank.append(q)


game = QuizBrain(question_bank)

while game.still_has_questions():
    game.next_question()

print("You've completed the quiz")
print(f"Your final score was: {game.score}/{game.question_numer}")