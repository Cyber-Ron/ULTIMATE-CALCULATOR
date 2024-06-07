import style
import time

while True:
    print(style.dash)
    print(style.logo)
    print(style.dash)
    print(style.space)
    print(style.author)
    print(style.space)

    print(" (1)CALCULATOR ")
    print(" (2)GRADES-CALCULATOR ")
    print(" (3)BMI-CALCULATOR  ")
    print(" (4)EXIT  ")

    user = input("Enter: ")

    if user == "1" or user.upper() == "CALCULATOR":
        while True:
            print(style.dash)
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
            print("[7]EXPONENT")
            print("[0]BACK TO MAIN MENU")
            print(style.dash)

            pick = input("Enter: ")
            print(style.dash)

            if pick == "0":
                break

            try:
                if pick == "1" or pick.upper() == "SUBTRACTION":
                    num1 = int(input("Enter Number: "))
                    num2 = int(input("Enter Another Number: "))
                    result = num1 - num2
                    time.sleep(0.30)
                    print(f"{num1} - {num2} = {result}")
                elif pick == "2" or pick.upper() == "ADDITION":
                    num1 = int(input("Enter Number: "))
                    num2 = int(input("Enter Another Number: "))
                    result = num1 + num2
                    time.sleep(0.30)
                    print(f"{num1} + {num2} = {result}")
                elif pick == "3" or pick.upper() == "MULTIPLICATION":
                    num1 = int(input("Enter Number: "))
                    num2 = int(input("Enter Another Number: "))
                    result = num1 * num2
                    time.sleep(0.30)
                    print(f"{num1} x {num2} = {result}")
                elif pick == "4" or pick.upper() == "DIVISION":
                    num1 = int(input("Enter Number: "))
                    num2 = int(input("Enter Another Number: "))
                    result = num1 / num2
                    time.sleep(0.30)
                    print(f"{num1} / {num2} = {result}")
                elif pick == "5" or pick.upper() == "MODULUS":
                    num1 = int(input("Enter Number: "))
                    num2 = int(input("Enter Another Number: "))
                    result = num1 % num2
                    time.sleep(0.30)
                    print(f"{num1} % {num2} = {result}")
                elif pick == "6" or pick.upper() == "FLOOR DIVISION":
                    num1 = int(input("Enter Number: "))
                    num2 = int(input("Enter Another Number: "))
                    result = num1 // num2
                    time.sleep(0.30)
                    print(f"{num1} // {num2} = {result}")
                elif pick == "7" or pick.upper() == "EXPONENT":
                    num1 = int(input("Enter Number: "))
                    num2 = int(input("Enter Another Number: "))
                    result = num1 ** num2
                    time.sleep(0.30)
                    print(f"{num1} ** {num2} = {result}")
                else:
                    print("Invalid, try again.")
            except ValueError:
                print("Invalid input, please enter numbers only.")

    elif user == "2" or user.upper() == "GRADES-CALCULATOR":
        while True:
            time.sleep(0.20)
            print(style.dash)
            time.sleep(0.020)
            
            print(" (0). BACK TO MAIN MENU ")

            limit = input("Enter Limit Subjects: ")

            if limit == "0":
                break

            try:
                limit = int(limit)
                grades = []
                for i in range(limit):
                    grade = int(input(f"Enter Grade {i + 1}: "))
                    grades.append(grade)
                average = sum(grades) / limit
                print(style.dash)
                print(f"Total Average is {average}")
                
            except ValueError:
                print("Invalid, try again.")

    elif user == "3" or user.upper() == "BMI-CALCULATOR":
        while True:
            try:
                height = float(input("Enter your height in cm: "))
                weight = float(input("Enter your weight in kg: "))
                print(style.dash)
            except ValueError:
                print("Invalid, try again.")
                continue

            BMI = weight / (height / 100) ** 2

            if BMI <= 18.5:
                print("\t(UNDER WEIGHT)")
            elif 18.5 < BMI <= 24.9:
                print("\t(NORMAL)")
            elif 25 <= BMI <= 29.9:
                print("\t(OVER WEIGHT)")
            elif BMI >= 30:
                print("\t(OBESITY)")

            print(f"Your BMI is {BMI}")
            print(style.dash)
            time.sleep(1)
            break

    elif user == "4" or user.upper() == "EXIT":
        time.sleep(0.03)
        print("bye-bye")
        break

    else:
        print("Invalid, try again.")
