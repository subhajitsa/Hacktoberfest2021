#Input numbers from user.
a = int(input("Enter first number to compare: "))
b = int(input("Enter second number to compare: "))
#float data type can be used if the input is in decimal value or any other.


#Defining a function to check the possible conditions.
def maximum(a, b):  
    if a > b:
        print(a, " is larger than ", b)
    elif a==b:
        print("Both the numbers are equal.")
    else:
        print(b, " is larger than ", a)
     
     
#Calling the function.
maximum(a, b)
