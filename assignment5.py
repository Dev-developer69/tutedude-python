# creating a dictionary of students name and marks
dict={'Ram':99,'shyam':95,'hari':80,'mohan':60,'alice':70}

# asking user to enter the name of the student
name=input("Enter the name of the student:")
try:
    print(dict[name])
except KeyError:
    print("student not found")


# TASK 2
# creating a list of numbers from 1 to 10
list=[1,2,3,4,5,6,7,8,9,10]
print(list)
# slicing the list to get the first 5 elements
list1=list[0:5]
print(list1)
# reversing the sliced list
list1.reverse()
print(list1)

