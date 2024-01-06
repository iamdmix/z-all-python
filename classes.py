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

print(player1.age)
print(player1.name)
print(player2.shout())
print(player2.age)
print(player1.paid_subscirption)

#classes are used as the are DRY and are memory efficient.
