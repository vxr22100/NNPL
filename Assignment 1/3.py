#Taking input and assigning to a variable
grade = int(input("Enter score: "))

#else if case to determine grade using percentage
#if grade greater than 89 and less that 101 then print grade A will execute
if(grade>89 and grade<101):
    print("A")
#if grade greater than 79 and less that 90 then print grade B will execute
elif(grade>79 and grade<90):
    print("B")
#if grade greater than 69 and less that 80 then print grade B will execute
elif(grade>69 and grade<80):
    print("C")
#if grade greater than 59 and less that 70 then print grade B will execute
elif(grade>59 and grade<70):
    print("D")
#else command if above conditions not met.
else:
    print("F")

