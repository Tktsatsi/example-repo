count = 0
again = "yes"  # Initialize the loop variable

while again == "yes" or again == "y":  # Initialize the loop variable
    # Repeatedly ask for input until valid numbers are provided
    
    input1 = input("Please enter the 1st number: ")
    operation = input("Please choose the operation (+, -, * or /): ")
    input2 = input("Please enter the 2nd number: ")

    
    # Attempt to convert each input individually
    
    try:
        num1 = float(input1)
    except ValueError:
        print(f"Error: The first input '{input1}' is not a valid number.")
        continue

    try:
        num2 = float(input2)
    except ValueError:
        print(f"Error: The second input '{input2}' is not a valid number.")
        continue

# Perform the operation now that both numbers are valid
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        try:
            if num2 != 0:        # try except block to handle division by zero
                result = num1 / num2
        except ZeroDivisionError:
            result = "Error: Division by zero is not allowed."
    else:
        result = f"Invalid operation: '{operation}'"
        
    print(f"The calculation of {input1} {operation} {input2} = {result}")
    
    with open("equations.txt", "a") as file:
        file.write(f"{count}. Calculation {input1} {operation} {input2} = {result}\n")
    
    again = input("Would you like to perform another calculation? (yes/no): ").strip().lower() #striping whitespace and converting to lower case to use in conditions
    if again == "yes" or again == "y":
        count += 1
    if again != "yes" or again != "y": # set break point, use a condition that will break the loop
        print("Goodbye!")
    
history = input("Would like to view history of calculation? (yes/no):")
if history == "yes" or history == "y":
    with open("equations.txt", "r") as equations:
        lines = equations.read()
        print(lines)  
        
        