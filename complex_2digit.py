#simple calculator
should_cont= True
while should_cont:
    try:
        print('''
Pick 1 to perform ADDITION
Pick 2 to perform SUBTRACTION
Pick 3 to perform MULTIPLICAITION
Pick 4 to perform DIVISION
Pick 5 to SQAURE
Pick 6 to CUBE''')
        choice= float(input('Enter your choice- '))
        if choice == 1:
            na= float(input('Enter a number to perform ADDITION for-   '))
            na1= float(input('Enter another number to perform ADDITION for-   '))
            add= na + na1 
            print(f"The sum of the two numbers is {add}\nThank You For Using Dharmik's Calculators\n\n")

        elif choice == 2:
            ns= float(input('Enter a number to perform SUBTRACTION for-   '))
            ns1= float(input('Enter another number to perform SUBTRACTION for-   '))
            sub= ns - ns1
            print(f"The difference of the two numbers is {sub}\nThank You For Using Dharmik's Calculators\n\n")

        elif choice == 3:
            nm= float(input('Enter a number to perform MULTIPLICATION for-   '))
            nm1= float(input('Enter another number to perform MULTIPLICATION for-   '))
            mul= nm * nm1 
            print(f"The product of the two numbers is {mul}\nThank You For Using Dharmik's Calculators\n\n")

        elif choice == 4:
            nd= float(input('Enter a number to perform DIVISION for-   '))
            nd1= float(input('Enter another number to perform DIVISION for-   '))
            div= nd / nd1
            print(f"The quotient of the two numbers is {div}\nThank You For Using Dharmik's Calculators\n\n")

        elif choice == 5 :
            sq1= float(input('Enter the number to find the square of-  ') )
            square= sq1 **2 
            print(f"The square of the numbers is {square}\nThank You For Using Dharmik's Calculators\n\n")   

        elif choice == 6:
            cu1= float(input("Enter the number to find cube of-   "))
            cube= cu1 ** 3
            print(f"The cube of the numbers is {cube}\n Thank You For Using Dharmik's Calculators\n\n")   

        elif choice <= 0 :
            print("Invalid Value\nThank You For Using Dharmik's Calculators\n\n")

        elif choice >= 7 :
            print("Invalid Value\nThank You For Using Dharmik's Calculators\n\n")    


    except ValueError:
        print("Invalid Value\n Please Try Again.\nThank You For Using Dharmik's Calculators\n\n")


    print('To continue please enter "continue"\nTo terminate please enter "terminate"')
    user_continue= input('>')

    if user_continue=='continue':
        should_cont= True
    
    elif user_continue== 'terminate':
        should_cont=  False
        print("Successesful termination!\nThank You For Using Dharmik's Calculators")
    else:
        should_cont= False
        print("Sorry, didn't understand that.\nTerminated\nThank You For Using Dharmik's Calculators")        