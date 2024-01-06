# 153= 1*1*1 + 5*5*5 + 3*3*3 
#An Armstrong number is a number such that the sum of its digits raised to the third power is equal to the number itself.


def Armstrong(num):
    # initialize sum
    sum = 0

    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp //= 10

    # display the result
    if num == sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number") 


Armstrong(153)


