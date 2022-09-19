import style
import time


print(style.dash)
print(style.logo)

print(style.dash)
print(style.space)
print(style.author)
print(style.space)

for i in range(1):
    print(" (1)CALCULATOR ")
    print(" (2)GRADES-CALCULATOR ")
    print(" (3)(x5)  ")
    print(" (4)BMI-CALCULATOR  ")
    print(" (5)EXIT  ")

user = input("Enter: ")
if user == "1" or user == "CALCULATOR":
    print(style.dash)
    for v in range(1):
        time.sleep(0.70)
        print("[1]SUBTRACTION")
        time.sleep(0.60)
        print("[2]ADDITION")
        time.sleep(0.50)
        print("[3]MULTIPLICATION")
        time.sleep(0.40)
        print("[4]DIVISION")
        time.sleep(0.30)
        print("[5]MODULUS")
        time.sleep(0.20)
        print("[6]FLOOR DIVISION")
        time.sleep(0.10)
        print("[7]EXPONET")
        pick = input("Enter: ")
        if pick == "1" or pick == "SUBTRACTION":
            num1 = input("Enter Number: ")
            num2 = input("Enter Another Number: ")
            result = int(num1) - int(num2)
            for x in range(1):
                time.sleep(0.30)
                print(num1 + " - " + num2 + " = " + str(result))
        elif pick == "2" or pick == "ADDITION":
            num1 = input("Enter Number: ")
            num2 = input("Enter Another Number: ")
            result = int(num1) + int(num2)
            for q in range(1):
                time.sleep(0.30)
                print(num1 + " + " + num2 + " = " + str(result))

        elif pick == "3" or pick == "MULTIPLICATION":
            num1 = input("Enter Number: ")
            num2 = input("Enter Another Number: ")
            result = int(num1) * int(num2)
            for g in range(1):
                time.sleep(0.30)
                print(num1 + " x " + num2 + " = " + str(result))

        elif pick == "4" or "DIVISION":
            num1 = input("Enter Number: ")
            num2 = input("Enter Another Number: ")
            result = int(num1) % int(num2)
            for h in range(1):
                time.sleep(0.30)
                print(num1 + " % " + num2 + " = " + str(result))
        elif pick == "5" or pick == "MODULUS":
            num1 = input("Enter Number: ")
            num2 = input("Enter Another Number: ")
            result = int(num1) % int(num2)
            for e in range(1):  
                time.sleep(0.30)
                print(num1 + " % " + num2 + " = " + str(result))

        elif pick == "6" or pick == "FLOOR DIVISION":
            num1 = input("Enter Number: ")
            num2 = input("Enter Another Number: ")
            result = int(num1) // int(num2)
            time.sleep(0.30)
            print(num1 + " // " + num2 + " = " + str(result))

        elif pick == "7" or pick == "EXPONET":
            num1 = input("Enter Number: ")
            num2 = input("Enter Another Number: ")
            result = int(num1) ** int(num2)
            time.sleep(0.30)
            print(num1 + " ** " + num2 + " = " + str(result))
        else:
            print("Try Again")
            quit()
elif user == "2" or user == "GRADES-CALCULATOR":
    time.sleep(0.20)
    print(style.dash)
    time.sleep(0.020)
    print(" (1).4 ")
    time.sleep(0.020)
    print(" (2).5  ")
    time.sleep(0.020)
    print(" (3).7  ")
    time.sleep(0.020)
    print(" (4).8  ")
    time.sleep(0.020)
    print(" (5).9  ")
    time.sleep(0.020)
    print(" (6).10  ")
    time.sleep(0.020)
    print(" (7).11 ")
    time.sleep(0.020)
    print(" (8).12  ")
    limit = input(" EnterLimit Grades: ")
    if limit == "3" or limit == "7":
        g1 = int(input("Enter Grades: "))
        g2 = int(input("Enter Grades: "))
        g3 = int(input("Enter Grades: "))
        g4 = int(input("Enter Grades: "))
        g5 = int(input("Enter Grades: "))
        g6 = int(input("Enter Grades: "))
        g7 = int(input("Enter Graees: "))
        add = g1 + g2 + g4 + g5 + g6 + g7
        avarage = add / 7 
        time.sleep(0.3)
        print(" Total Avarage is  ", avarage)
    elif limit == "4" or limit == "8":
        g1 = int(input("Enter Grades: "))
        g2 = int(input("Enter Grades: "))
        g3 = int(input("Enter Grades: "))
        g4 = int(input("Enter Grades: "))
        g5 = int(input("Enter Grades: "))
        g6 = int(input("Enter Grades: "))
        g7 = int(input("Enter Graees: "))
        g8 = int(input("Enter Grades: "))
        add = g1 + g2 + g4 + g5 + g6 + g7 + g8
        avarage = add / 8
        time.sleep(0.3)
        print("Total Avarage is ", avarage)

    elif limit == "5" or limit == "9":
        g1 = int(input("Enter Grades: "))
        g2 = int(input("Enter Grades: "))
        g3 = int(input("Enter Grades: "))
        g4 = int(input("Enter Grades: "))
        g5 = int(input("Enter Grades: "))
        g6 = int(input("Enter Grades: "))
        g7 = int(input("Enter Graees: "))
        g8 = int(input("Enter Grades: "))
        g9 = int(input("Emter Grades: "))
        add = g1 + g2 + g4 + g5 + g6 + g7 + g8 + g9
        avarage = add / 9
        time.sleep(0.3)
        print("Total Avarage is ", avarage)

    elif limit == "6" or limit == "10":
        g1 = int(input("Enter Grades: "))
        g2 = int(input("Enter Grades: "))
        g3 = int(input("Enter Grades: "))
        g4 = int(input("Enter Grades: "))
        g5 = int(input("Enter Grades: "))
        g6 = int(input("Enter Grades: "))
        g7 = int(input("Enter Graees: "))
        g8 = int(input("Enter Grades: "))
        g9 = int(input("Enter Grades: "))
        g10  = int(input("Enter Grades: "))
        add = g1 + g2 + g4 + g5 + g6 + g7 + g8 + g9 + g10
        avarage = add / 10
        time.sleep(0.3)
        print("Total Avarage is ", avarage)

    elif limit == "7" or limit == "11":
        g1 = int(input("Enter Grades: "))
        g2 = int(input("Enter Grades: "))
        g3 = int(input("Enter Grades: "))
        g4 = int(input("Enter Grades: "))
        g5 = int(input("Enter Grades: "))
        g6 = int(input("Enter Grades: "))
        g7 = int(input("Enter Graees: "))
        g8 = int(input("Enter Grades: "))
        g9 = int(input("Enter Grades: "))
        g10 = int(input("Enter Grades: "))
        g11 = int(input("Enter Grades: "))
        add = g1 + g2 + g4 + g5 + g6 + g7 + g8 + g9 + g10 + g11
        avarage = add / 11
        time.sleep(0.2)
        print("Total Avarage is ", avarage)

    elif limit == "8" or limit == "12":
        g1 = int(input("Enter Grades: "))
        g2 = int(input("Enter Grades: "))
        g3 = int(input("Enter Grades: "))
        g4 = int(input("Enter Grades: "))
        g5 = int(input("Enter Grades: "))
        g6 = int(input("Enter Grades: "))
        g7 = int(input("Enter Graees: "))
        g8 = int(input("Enter Grades: "))
        g9 = int(input("Enter Grades: "))
        g10 = int(input("Enter Grades: "))
        g11 = int(input("Enter Grades: "))
        g12 = int(input("Enter Grades: "))
        add = g1 + g2 + g4 + g5 + g6 + g7 + g8 + g9 + g10 + g11 + g12
        avarage = add / 12 
        print("Total Avarage is ", avarage)
    elif limit == "1" or limit == "4":
        g1 = int(input("Enter Grades: "))
        g2 = int(input("Enter Grades: "))
        g3 = int(input("Enter Grades: "))
        g4 = int(input("Enter Grades: "))
        add = g1 + g2 + g3 + g4
        avarage = add / 4
        print("Total Avarage is ", avarage)

    elif limit == "2" or limit == "5":
        g1 = int(input("Enter Grades: "))
        g1 = int(input("Enter Grades: "))
        g2 = int(input("Enter Grades: "))
        g3 = int(input("Enter Grades: "))
        g4 = int(input("Enter Grades: "))
        g5 = int(input("Enter Grades: "))
        g1 + g2 + g3 + g4 + g5
        avarage = add / 5
        print("Total Avarage is ", avarage)
    else:
        print("Try Again")
        exit()

elif user == "3":
    print(" (1).x5  ")
    time.sleep(00.20)
    print(" (2).x6  ")
    time.sleep(00.20)
    print(" (3).x7  ")
    time.sleep(00.20)
    print(" (4).x8  ")
    time.sleep(00.20)
    print(" (5).x9  ")
    time.sleep(00.20)

    x = input("Enter MaximumNumber: ")
    if x == "1" or x == "x5":
        num1 = lambda b: b * 5
        print(num1(int(input("Enter Number: "))))
    elif x == "2" or x == "x6":
        num1 = lambda c: c * 6
        print(num1(int(input("Enter Number: "))))
    elif x == "3":
        num1 = lambda n: n * 7
        print(num1(int(input("Enter Number: "))))
    elif x == "4":
        num1 = lambda n: n * 8
        print(num1(int(input("Enter Number: "))))
    elif x == "5":
        num1 = lambda n: n * 9 
        print(num1(int(input("Enter Number: "))))
    elif x == "6":
        num1 = lambda n: n * 9
        print(num1(int(input("Enter Number: "))))

elif user == "4":
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))

    BMI = weight / (height/100)**2
    if BMI <=18.5:
        print("\t(UNDER WEIGHT)")

    elif BMI >=18.5 or BMI >=24.9:
        print("\t(NORMAL)")

    elif BMI >=25 or BMI >=29.9:
        print("\t(OVER WEIGHT)")
    elif BMI >=30:
        print("\t(OBESITY)")


    print(f"You BMI is {BMI}")

elif user == '5':
    time.sleep(0.03)
    print("bye-bye")


else:
    print("Try Again")
    exit()
