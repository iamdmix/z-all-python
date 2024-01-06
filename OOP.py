#OOP - Object Oriented Programming 
# We can have different objects in one peice of code.
# Let us assume this is a paid game.

class PlayerCharacter:
    paid_subscirption = True  # This is called the Class Object Attribute
    def __init__(self, name, age): #constructor (__init__) is called to instantiate an object
        self.name = name  # This assigns the value of name to the .name attribute
        self.age = age  # Similarly here for age 

    def run(self):
        print('run')
        return "done"
    
    def shout(self): 
        print(f"My name is {self.name}")

player1 = PlayerCharacter("Dharmik", 16)
player2 = PlayerCharacter("Wizard", 102930)
player1.age = 40
del player2.age
print(player1.age)
print(player1.name)
print(player2.shout())
print(player2.age)
print(player1.paid_subscirption)

#classes are used as they are DRY(DO NOT REPEAT YOURSELF) and are memory efficient.

#Use the __init__() function to assign values to object properties,
#  or other operations that are necessary to do when the object is being created.

#The self parameter is a reference to the current instance of the class,
#  and is used to access variables that belong to the class.

#It does not have to be named self , you can call it whatever you like,
#  but it has to be the first parameter of any function in the class:

