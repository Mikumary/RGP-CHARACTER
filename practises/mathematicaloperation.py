while True:
    user_input = input("Enter mathematical operation (e.g., 5 + 3) or type 'quit' to exit: ")

    # Check if the user wants to quit
    if user_input.lower() == "quit":
        print("Thank you for your time!")
        break

    # Split the input into parts
    parts = user_input.split()

    # Validate correct format
    if len(parts) != 3:
        print("❌ Please enter in the correct format: number1 operator number2 (e.g., 5 + 3)")
        continue

    num1, operation, num2 = parts

    # Validate that the numbers are valid
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("❌ Please enter valid numbers.")
        continue

    # Perform the operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("⚠️ You cannot divide by zero!")
            continue
        result = num1 / num2
    else:
        print("❌ Invalid operator! Please use +, -, * or /.")
        continue

    # Display the result
    print(f"✅ Result: {result}")
