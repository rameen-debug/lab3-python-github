# python_calc.py
# A menu driven calculator that keeps on running until the user chooses exit.

# "while True" is an infinite loop that repeats the menu forever
# "break" used below is what ends it
print("WELCOME TO CALCULATOR")
print()
while True:
    # Show the menu of operations
    print("The operations are as follows: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")
    print()

    #Ask which operation user wants to perform
    operation=int(input("Enter a number to perform the operation: "))
    print()

    # Option 7: says goodbye and exits the loop (program ends)
    if operation==7:
        print("Goodbye!")
        break #This is the break statement.
    # Anything outside 1 and 7 is invalid
    elif operation<1 or operation> 7:
        print("Invalid Choice. Please enter number from 1-7.")
        continue # goes back to the menu without asking for numbers
    print()

    #Get the two numbers to work with
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    print()
    #Addition
    if operation == 1:
        sum=num1+num2
        print(num1 ,"+",num2, "=",sum)
    #Subtraction
    elif operation == 2:
        sub = num1 - num2
        print(num1, "-",num2,"=",sub)
    #Multiplication
    elif operation == 3:
        prod= num1*num2
        print(num1,"x",num2,"=",prod)
    #Division
    elif operation==4:
        if num2==0: #Dividing by zero is impossible so check num2 first
            print("Error. Division is not allowed.")
        else:
            div = num1/num2
            print( num1 ,"/", num2,"=",div)
    #Even/Odd: a number is even if the remainder after dividng by 2 is 0
    elif operation==5:
        # Checks the first number
        if num1%2==0:
            print("The number",num1,"is an even number.")
        else:
            print("The number",num1,"is an odd number.")
        #Checks the second number
        if num2%2==0:
            print("The number",num2,"is an even number.")
        else:
            print("The number",num2,"is an odd number.")
    # Percentage: what percent num1 is of num2 (num2 can't be zero)
    elif operation==6:
        if (num2==0):
            print("Error. Percentage can not be calculated.")
        else:
            percentage=(num1/num2)*100
            print(num1,"is",percentage,"%","of",num2,".")
    # Blank line to separate this calculation from the next menu
    print()
    # End of program
    
