def cube(num):
    cu = num **3
    return cu
    print(cu)
    

lambda_square = lambda sq:    sq * sq
print(lambda_square(5))

# What is lambda function in python? well it is basically that,"A lambda function is a small anonymous function.

#Enumerate is used to make a table of index followed by value 


for octagon, character in enumerate(list(range(100))):
    if octagon == 50:
        print(f"Index of 50 is {character}")


#list(*args) = (input('Enter three numbers of a list- '))