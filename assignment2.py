# The code takes an integer input from the user and checks if it is even or odd.
a=int(input("Enter a number"))
if(a%2==0):
    print(a,"is an Even number")
else:   
    print(a,"is an odd number")



    # problem 2
# sum of integer from 1 to 50 using a loop

sum=0
for i in range(1,51):
    sum+=i
print("The sum of integers from 1 to 50 is",sum)