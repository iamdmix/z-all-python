#to find the sum of the numbers in a list.

my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0         #initialising the variable 

for item in my_list:
    counter += item #counter = counter + item 

print(counter)


q = int(input("Please enter last number in range- "))

j = q+1
for i in range(j):
    print(i)
