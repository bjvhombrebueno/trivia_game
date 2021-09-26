from data import question_data
class Quiz_brain:

    def __init__(self, question_data):
        self.question_number = 0
        self.question_list = question_data
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        my_ans = input(f"Q{self.question_number+1}: {current_question.text}")
        self.question_number += 1
        self.check_answer(my_ans, current_question.answer)

    def check_answer(self, my_answer, correct_answer):

        if my_answer == correct_answer:
            print("Correct")
            self.score += 1
        else:
            print("Wrong")

        print (f"{self.score} /{self.question_number}")
