#To check whether the user is old enough to drive
def drive(age = 0, lis = 'n'):     #(age = 0, lis = 'n') is called default parameter
    '''
    Info: This functions checks whether you are allowed to drive a car. 
    '''# This is a doc string that will show up when you call the function.

    print('\n\nWelcome to the International Road Safety Programme for Auto-drive Cars.\n\n')

    if age >= 18:
        
        if lis == 'y':
            lis = True 

        elif lis == "n":
            lis = False

        else:
            print("\nI didn't understand,")



    if age >= 18 and lis is False:
        print('\nAccess denied as you do not have a license.')

    elif age >= 18 and lis is True:
        print('\nAccess granted, Starting the car, you can drive')

    else:
        print("\nAccess denied, you cannot drive the car.")

    print("-International Road Safety Programme")


drive(47,"y")
drive(17,'y')  
#We can do it this way, it is called keyword arguements but this is conider bad practice.

