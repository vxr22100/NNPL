#Definig a function to delete 'h' and 'o' and reverse a string.
def reverse(string):
    string = string.replace('h','')
    string = string.replace('o','')
    rev = string[::-1]
    return rev

#Taking input and assigning to a variable
a = input("Enter a word: ")

#calling print statement
print(a)

#calling reverse function and print statement
print(reverse(a))

print("--------------------------")

#taking input, casting into int and assigning to two different variables
b = int(input("Enter 1st number: "))
c = int(input("Enter 2st number: "))

#Addition
add = b+c
#Subtraction
sub = b-c
#Multiplication
mul = b*c
#Division
div = b/c

#print statements
print("Addition: ",add)
print("Subtraction: ",sub)
print("Multiplication: ",mul)
print("Division: ",div)

