#Function to take two strings from the user 
def fullname(x,y):
    return x+" "+y

#Function that returns every other char in the full_name string
def string_alternative(z):
    return z[::2]

#taking input and assigning to variables
First_name = input("your first name : ")
last_name = input("your last name : ")

#Calling fullname function
Full_name= fullname(First_name,last_name)

#Printing Full Name
print("Full Name: "+Full_name)

#Calling string_alternative and printing the same
print(string_alternative(Full_name))


