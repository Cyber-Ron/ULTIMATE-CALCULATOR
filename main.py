import style
import time


print(style.dash)
print(style.logo)

print(style.dash)
print(style.space)
print(style.author)
print(style.space)

for i in range(1):
    time.sleep(0.50)
    print(" (1)CALCULATOR ")
    time.sleep(0.40)
    print(" (2)GRADES-CALCULATOR ")
    time.sleep(0.8)
    print(" (3)EXIT ")

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
    time.sleep(0.1)
    print("  (1).7  ")
    time.sleep(0.1)
    print("  (2).8  ")
    time.sleep(0.1)
    print("  (3).9  ")
    time.sleep(0.1)
    print("  (4).10  ")
    time.sleep(0.1)
    print("  (5).11  ")
    time.sleep(0.1)
    print("  (6).12  ")
    limit = input(" EnterLimit Grades: ")
    if limit == "1" or limit == "7":
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
    elif limit == "2" or limit == "8":
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

    elif limit == "3" or limit == "9":
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

    elif limit == "4" or limit == "10":
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

    elif limit == "5" or limit == "11":
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

    elif limit == "6" or limit == "12":
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
    else:
        print("Try Again")
        exit()
elif user == "3" or user == "EXIT":
    exit()

else:
    print("Try Again")
    exit()
