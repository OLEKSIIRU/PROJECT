#Kordused
from math import *
from re import X
for x in range(1,11):
    R=float(input("{0}.R: ".format(x)))
    if R>0:
        S=pi*R**2
    else:
        S="R peab > kui 0 olema"
    print("S={0}".format(S))
x=0
while True:
    x+=1
    R=float(input("{0}.R: ".format(x)))
    if R>0:
        S=pi*R**2
    else:
        S="R peab > kui 0 olema"
    print("S={0}".format(S))    
    if x==10:
        break
x=0
while x<10:
    x+=1
    R=float(input("{0}.R: ".format(x)))
    if R>0:
        S=pi*R**2
        x+=1
        if R<0:
            x-1
    else:
        S="R peab > kui 0 olema"
    print("S={0}".format(S))    
    if x==10:
        break
#1
t=0
for x in range(15):
    E=float(input("SISESTA E: ".format(x)))
    if E.is_integer():
       t+=1
print(t)
#2
summa=0
A=int(input("Siseta N: "))
for x in range(1,A+1,1):
    summa+=x
print("Summa: {0}".format(summa))
#3
p=1
lause=""
for x in range(8):
    G=float(input("{0} samm\nSisesta G: ".format(x+1)))
    if G>0:
        p*=G
        lause=lause+str(G)+"*"
print(lause[:-1],"=",G)

#4
x=0
for x in range(10,21):
    co=x**2
    print("square of {x} is equal to{co}".format(x))
#5
x=0
N= int(input("Введите кол-во чисел: "))
for _ in range(N):
	number = int(input("Введите число: "))
	if number < 0:
		sum_negative+= number
print("Сумма отрицательных чисел: {sum_negative}")
#6
x=0
N = int(input("Введите количество чисел: "))
cnegative = 0
cpositive = 0
czero = 0
for x in range(N):
number = float(input("Введите число: "))
 if number < 0:
  count_negative += 1
   elif number > 0:
   	count_positive += 1
   else:
   	count_zero += 1
print(f"Количество отрицательных чисел: {cnegative}")
print(f"Количество положительных чисел: {cpositive}")
print(f"Количество нулей: {czero}")
#7
num=0
A=int(input("Введите первое число промежутка"))
B=int(input("Введите последнее число промежутка"))
К=int(input("Введите значение К"))
print("Числа, кратные {K}, из промежутка [{A},{B}]:")
for num in range(A,B+1):
	if num % K==0:
		print(num)
#8
print("Дюймы/Сантиметры")
for x in range (1,21):
	centimeters=x*2.5
print("{x}{centimeters:.2}")
#9






#Скорость из 7 варианта
Скоростьвмс=float(input("Скорость в метрах в секунду: "))
Скоростькмч=float(input("Cкорость в километрах в час: "))
if Скоростьвмс*3.6>Скоростькмч:
    print("Скорость в метрах в секунду больше")
else:("Скорость в километрах в час")






#Võileib
soov=input("Kas tahad süüa?").lower()
if soov=="jah" or soov=="yes"or soov=="yeah":
    valik=int(input("1´juustuga võileib\n2´võrstiga võileib"))
    if valik in [1,2]:
        if valik==1:
           print("Palun juustuga võileib")
        else:
            print("Palun vorstiga võileib")
    else:
        print("Vale valik!")
else:
    print("Ei taha, siis ei taha")








#Calculator Kalkulaator
try:
    a=float(input("Esimene arv:"))
    try:
        b=float(input("Teine arv:"))
        t=input("Tehe:")
        if t in ['+','-','/','*','%','//','**']:
            if t=='+':
                v=a+b
            elif t=='-':
                v=a-b
            elif t=='*':
                v=a*b
            elif t=='**':
                v=a**b
            elif t=='/':
                if b==0:
                    v="DIV/0"
                else:
                    v=a/b
            elif t=='%':
                v=a%b
            else:
                v=a//b
            print("{0}{1}{2}={3}").format(a,t,b,v)
        else:
            print("Tuhndmatu märk")
    except :
        print("Vale b arvu andmetüüp")
except :
    print("Vale a arvu andmetüüp")





#Kolmkurk
a=float(input("Alpha:"))
b=float(input("Betta:"))
c=float(input("Gamma:"))
if a>0 and b>0 and c>0:
    if a+b+c==180:
        print("Kolmnurk")
    else:
        print("Nurgad")
else: 
    print("Andmed ei ole õiged")

#new
a=input("Код группы: ")
if a==b"TARgv23":
   C=(int(input("Кол-во пропусков:")))
   if C<15:
       F=float(input("Какой средний бал?:"))
       if F>3.8:
           print("Toetus!")
       else:
           print("Liiga madal keskmine hinne. Toetust ei ole!")
   else: 
       print("Не начисляется стипендия")
else:
    print("Не подходит название группы")
    

a=input("Код группы: ")
C=(int(input("Кол-во пропусков:")))
F=float(input("Какой средний бал?:"))
if a==b"TARgv23" and F>3.8 and C<15:
    print("Toetus!")
else:("Toetus ei ole")

