import math  # Importing the math module for mathematical functions

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract the second number from the first
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide the first number by the second
def divide(x, y):
    try:
        return x / y  # Attempt to divide
    except ZeroDivisionError:  # Handle division by zero
        return "Cannot divide by zero."  # Return error message

# Function to perform exponentiation (raise x to the power of y)
def exponentiation(x, y):
    return x ** y

# Function to calculate the square root of a number
def sqrt(x):
    return math.sqrt(x)

# List to store the history of calculations
history = []

# Infinite loop to keep the calculator running until the user decides to quit
while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Show History")
    print("q. Quit")

    choice = input("Enter choice: ")  # Get the user's choice
    
    if choice == 'q':  # Check if the user wants to quit
        break

    # Check if the choice is one of the arithmetic operations
    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))  # Get the first number
        num2 = float(input("Enter second number: "))  # Get the second number
        
        # Perform the selected operation
        if choice == '1':
            result = add(num1, num2)  # Call the add function
            print(f"Result: {result}")  # Display the result
            history.append(f"{num1} + {num2} = {result}")  # Log the operation in history

        elif choice == '2':
            result = subtract(num1, num2)  # Call the subtract function
            print(f"Result: {result}") 
            history.append(f"{num1} - {num2} = {result}") 

        elif choice == '3':
            result = multiply(num1, num2)  # Call the multiply function
            print(f"Result: {result}") 
            history.append(f"{num1} * {num2} = {result}") 

        elif choice == '4':
            result = divide(num1, num2)  # Call the divide function
            print(f"Result: {result}")  
            history.append(f"{num1} / {num2} = {result}")  

        elif choice == '5':
            result = exponentiation(num1, num2)  # Call the exponentiation function
            print(f"Result: {result}")  
            history.append(f"{num1} ^ {num2} = {result}")  

    # Handle the square root operation separately
    elif choice == '6':
        num = float(input("Enter number for square root: "))  # Get the number for square root
        result = sqrt(num)  # Call the sqrt function
        print(f"Result: {result}")  
        history.append(f"√{num} = {result}")  
    
    # Display the calculation history
    elif choice == '7':
        print("\nCalculation History:")  # Print header for history
        for h in history:  # Iterate through the history list
            print(h)  # Print each calculation
    
    else:
        print("Invalid Input")  # Handle invalid choices
