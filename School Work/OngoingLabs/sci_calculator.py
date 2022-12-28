#Variables, Lists, Libraries
from math import log
ContinueCalculator = True
ValidInput = True
CurNum= 0
AmountOfCalculations = 0
Values = []
SumValues = 0
AverageValues = 0
option = 5

#This is run via a while loop to keep the calculator running until the user chooses to exit
while ContinueCalculator == True:
    #If the user picked any option that isn't zero from the menu previously, the script will print out the calculator menu
    if option != 0 :
        AmountOfCalculations += 1
        print("\nCurrent Result:",float(CurNum))
        CurNum = 0
        print("\nCalculator Menu")
        print("---------------")
        print("0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average")

        option = int(input("\nEnter Menu Selection:"))
    else:
        pass

   #This Boolean ensures that the user only inputs a number between one and seven (inclusive)
    if -1 < option < 8:
        ValidInput = True
    else:
        ValidInput = False
        print("Error: Invalid selection!")
        while ValidInput == False:
            option = int(input("Enter Menu Selection:"))
            if -1 < option < 8:
                ValidInput = True
            else:
                print("Error: Invalid selection!")
                continue

    #This makes sure the user isn't prompted to enter two different numbers if they selected option 7 or 0 from the menu
    if option != 7 and option != 0:
        num1 = float(input("Enter first operand:"))
        num2 = float(input("Enter second operand:"))

    #These are the opperations that occur based on the option the user choose from the menu
    if ValidInput == True:
        if option == 0:
            print("Thanks for using this calculator. Goodbye!")
            ContinueCalculator=False

        elif option == 1:
            CurNum = num1+num2
            SumValues += CurNum

        elif option == 2:
            CurNum = num1 - num2
            SumValues += CurNum

        elif option == 3:
            CurNum = num1 * num2
            SumValues += CurNum

        elif option == 4:
            CurNum = num1 / num2
            SumValues += CurNum

        elif option == 5:
            CurNum = num1 ** num2
            SumValues += CurNum

        elif option == 6:
            CurNum = log(num2 , num1)
            SumValues += CurNum

        elif option == 7:
            #Before following through option 7, the Boolean ensures the user doesn't execute option 7 without and previous calculations
            if SumValues != 0:
                AverageValues = SumValues/(AmountOfCalculations-1)
                print("Sum of calculations:",SumValues)
                print("Number of calculations:",AmountOfCalculations-1)
                print("Average of calculations:", "%.2f" % (AverageValues))
                option = int(input("\nEnter Menu Selection:"))
            else:

                while option == 7 and SumValues == 0:
                    print("Error: No calculations yet to average!\n")
                    option = int(input("Enter Menu Selection:"))

