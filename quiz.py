import random
import json
from string import ascii_lowercase

class run_quiz:
    def run(self,path):
        num_questions_quiz=10
        questions=self.prepare_questions(path,num_questions=num_questions_quiz)
        num_correct=0
        for num,question in enumerate(questions,start=1):
            print(f"\nQuestion {num}:")
            num_correct+=self.ask_question(question)
        print(f"\n You got {num_correct} correct out of {num} questions")
        if num_correct>=7:
            print("########### Successfully passed the quiz!!!! ########")
            choice=int(input("\nDo you want to try again? \n1.Yes\n2.No\n"))
            if choice==1:
                pass
            else:
                exit()
        else:
            print("#######  OOPS!!! Try again!!!! All the best!!!!  ###########")
            exit()


    def prepare_questions(self,path,num_questions):
        with open(path,"r+") as file:
            questions=json.load(file)
            num_questions=min(num_questions,len(questions))
            return random.sample(questions,k=num_questions)
    
    def ask_question(self,question):
        correct_answer=question["answer"]
        ordered_choices=random.sample(question["choices"],len(question["choices"]))
        answer=self.get_answer(question["question"],ordered_choices)
        if answer==correct_answer:
            print("CORRECT!!!")
            return 1
        else:
            print(f"No!!! \nThe answer is {correct_answer!r} not {answer!r}.")
            print("Explanation: ",question["explanation"])
            return 0

    def get_answer(self,question,choices):
        print(f"{question}?")
        labeled_choices=dict(zip(ascii_lowercase,choices))
        for label,choices in labeled_choices.items():
            print(f"{label}) {choices}")
        while (answer_label:=input("\nChoice? ")) not in labeled_choices:
            print(f"Please answer one of {' , '.join(labeled_choices)}")
        return labeled_choices[answer_label]

