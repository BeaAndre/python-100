from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# SETUP

question_bank = []

for q in question_data:
    new_question = Question(q['text'], q['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# QUIZ START

print("---------- QUIZ GAME ----------")

while(quiz.still_has_questions()):
    quiz.show_next_question()
    
quiz.show_score()