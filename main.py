"""
2 methods

first,appear question.
second,notice to miss.  #  

first method is repeated 'while'.
"""
miss=0
import random as rd

def appearQuestion():
    number1=rd.randint(0,10)
    number2=rd.randint(0,10)

    message=number1, "+", number2, "=?"
    print(number1, "+", number2, "=?")
    answer=int(input()) #  i want to fix this int to be able to float.
    if(answer == number1+number2):
        input("correct!!")
    else:
        miss=1
        print("incorrect...")
        
        print(miss)


while miss == 0:
    appearQuestion() 
    print(miss)

input("Press return...")
