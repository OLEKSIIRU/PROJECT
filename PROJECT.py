






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

