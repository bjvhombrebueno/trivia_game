from data import question_data
from question_model import Question
import quiz_brain
question_bank = [Question(question["text"],question["answer"]) for question in question_data]
#question_bank = []
#for question in question_data:
    #question_text = question["text"]
    #question_answer = question["answer"]
    #new_question = Question(question_text,question_answer)
    #question_bank.append(new_question)
#for myquestion in question_bank:
#   print(myquestion.text)

quiz = quiz_brain.Quiz_brain(question_bank)
while quiz.question_number < len(question_bank):
    quiz.next_question()
