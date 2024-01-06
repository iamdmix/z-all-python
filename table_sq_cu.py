# table of squares and cubes
a= int(input('Enter the first number in range to find square of - '))
b= int(input('Enter the last number in range to find square of - '))
print('Number\tSquare\tCube')
for i in range(a,b + 1):
    if i == 15:
        pass
    
    cube= i**3
    square = i**2
    print('  ', i,'\t', square,'\t',cube )