class QuizBrain:

    def __init__(self,quiz_list) -> None:
        self.current_quiz_num = 0
        self.quiz_list = quiz_list
        self.marks = 0
    
    


    def next_question(self):
        if(self.current_quiz_num<len(self.quiz_list)):
            answer = input(f"{self.quiz_list[self.current_quiz_num].question} : true/false : ")
            self.check_answer(self.quiz_list[self.current_quiz_num].answer,answer)
            
        else:
            print(self.marks)
            
    def check_answer(self,corect_answer,user_answer):
        if(corect_answer == user_answer):
            self.marks+=1
            self.current_quiz_num+=1
            self.next_question()
        else:
            print("Answer is wrong\n")
            self.next_question()