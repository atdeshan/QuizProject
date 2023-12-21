from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_object_list = []
for current_q in question_data:
    new_question = Question(current_q["text"],current_q['answer'])
    question_object_list.append(new_question)

new = QuizBrain(question_object_list)
new.next_question()