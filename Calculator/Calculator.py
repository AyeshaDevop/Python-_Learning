# Function to add two numbers
def add( a , b):
    return a + b
# Function to subtract two numbers
def subtract(a , b):
    return a - b

# Function to multiply two numbers
def multiply(a , b):
    return a * b

# Function to divide two numbers
def divide(a , b):
    if b != 0:  # To avoid division by zero
        return a / b
    else:
        return "Error! Division by zero."

# Main program
print("Select operation:")
print("1. Add")                 #( + )
print("2. Subtract")             #( -  )
print("3. Multiply")            #( *  )
print("4. Divide")              #(  /  )

# Take input from the user
choice = input("Enter choice (1/2/3/5/%): ")

# Check if the user has chosen a valid option
if choice in ('1', '2', '3', '4' ):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")

    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
  
       

else:
    print("Invalid input")
