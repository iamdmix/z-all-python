usrname = input('PLEASE ENTER USERNAME- ')
pswrd = input('PLEASE ENTER THE PASSWORD- ')

length = len(pswrd)

pswrd_length = '*' * length

print(f"Hey {usrname}, your password {pswrd_length} is {length} characters long.")