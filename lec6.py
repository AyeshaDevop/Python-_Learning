#Functions and Recursion
#Function
# Defining a function
# def welcome(name):
#     print(f"Hello, {name}! Welcome to Python class.")

# Calling the function
welcome ("Ali")
welcome ("zara")
welcome ("Ayesha")
welcome (name=("ali" , "ahmad"))

#Recursion
def factorial(n):
    # Base case: if n is 1 or 0, return 1 (since 0! and 1! are both 1)
    if n == 0 or n == 1:
        return 1
    #  multiply n by the factorial of n-1
    else:
        return n * factorial(n-1)

print(factorial(5))  



