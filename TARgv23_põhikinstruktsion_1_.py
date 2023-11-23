print   ("Tere tulemast!".center(50))
kool=input("\tMis koolis sa õpid?: ") #str kool
while 1:
    kursus = input("\tMis kursusel?: ") #int kursus

    if kursus.isdigit(): 
        kursus = int(kursus) 
        break 
    else:
        print("\tPalun sisestage ainult numbrid!")


   
print("Tere tulemast kooli "+kool+"!\nOle hea"+str(kursus)+".kuursuse õpilaseks!")
print("Tere tulemst kooli", kool,"!\nOle hea",kursus,".kuursuse õpilaseks!")
print("Tere tulemast kooli {0}!\nOle hea {1}.kuursuse õpetajaks!". format(kool,kursus))
