from math import *
import sys
from random import*
operators = ['+','-','*','**' ,'/']
difficulty = 0

while difficulty not in [1,2,3]:
    try:
        difficulty = int(input("choose quest lvl(1,2,3)"))
    except ValueError:
        print("Choose quest lvl(1,2,3)")

qc = int(input("How many questsions whould you like to answer?"))
coa=0
ca=0
questsions=True
for x in range(qc):
    if difficulty==1:
        operators = ['+','-','*','**' ,'/']
        max_number=10
    if difficulty==2:
        operators = ['+','-','*','**' ,'/']
        max_number=50
    if difficulty==2:
        operators = ['+','-','*','**' ,'/']
        max_number=100

while ca<qc:
    num1=random.randint(1,max_number)
    num2=random.randint(2,max_number) 
    operator = random.choice(operators) if operator=='/' else random.randit(1,num1)

    questsion=("{num1} {operator} {num2}")
    ca=eval(questsion)
    ua=float(input(questsion)) if operator=='/' else random.randint(1,num1)
    
    if abs(ua-ca)<0.01:
        print("NICE")
        ca+=1
    else:
            print("Wrong answer! correct is {ca}")

            ca+=1
    score=(ca/qc)*100
    if score<60:
        g="Hinne2"
    elif score<75:
        g="Hinne3"
    elif score<90:
        g="Hinne<4"
    else:
        g="Hinne5"

    print("Your result:{g}")
