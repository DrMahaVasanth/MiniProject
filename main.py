from quiz import run_quiz
import re


print("*"*140)
name=input("Hi!!!!  What's your name?  ")
res_name=re.findall("[A-z]",name)

if res_name:
    print("****************************************************")
    print(f"\4 \4 \4 \4  Hello {name}!! Welcome to Quiz!!!  \4 \4 \4 \4 ")
    while True:
        if __name__=="__main__":

            print("##################### TOPICS ###################\n1. Python\n2. MySQL\n3. Exit")
            try:
                option=int(input("Select the option: "))
            except:
                print("Invalid option!!! Try again!!!")
                break
            obj_quiz=run_quiz()
            if option==1:
                print("\n************** WELCOME TO PYTHON QUIZ **************")
                print("No. of Questions: 10\nYou will be graded at the end!! \nALL THE BEST")
                if (choice:=int(input("\nAre you ready to take the quiz?\n1.Yes\n2.No\n")))==1:
                    obj_quiz.run(path="G:\\Python\\MiniProject\\quiz_python.json")
                else:
                    print("\3 \3 \3 \3 Thank you!!!! Have a great day!!!! \3 \3 \3 \3")
                    exit()
            elif option==2:
                print("\n************** WELCOME TO MYSQL QUIZ **************\n")
                print("No. of Questions: 10\nYou will be graded at the end!! \nALL THE BEST!!!!!")
                if (choice:=int(input("\nAre you ready to take the quiz?\n1.Yes\n2.No\n")))==1:
                    obj_quiz.run(path="G:\\Python\\MiniProject\\quiz_mysql.json")
                else:
                    print("\3 \3 \3 \3 Have a great day!!!! \3 \3 \3 \3")
                    exit()
            else:
                exit()
else:
    print("Invalid input!!! Try entering again!!!!") 
    exit()
    



