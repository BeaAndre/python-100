class QuizBrain:
    
    def __init__(self, question_list):
        self.score = 0
        self.q_number = 0
        self.q_list = question_list
    
    def show_next_question(self):
        current = self.q_list[self.q_number]
        self.q_number += 1
        print(f"Q {self.q_number}: {current.question}")
        answer = input("(true/false): ")
        self.evaluate_answer(answer, current)
    
    def still_has_questions(self):
        return self.q_number < len(self.q_list)
    
    def evaluate_answer(self, user_answer, current_q):
        if(user_answer == current_q.answer.casefold()):
            self.score += 10
        elif(user_answer.casefold() != "true" and user_answer.casefold() != "false"):
            self.q_number -= 1
            print("Invalid answer. Try again.")
            
    def show_score(self):
        print("----------- QUIZ END ----------")
        print(f"You finished the quiz! You got a score of {self.score} / {len(self.q_list) * 10}")