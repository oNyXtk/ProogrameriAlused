try:
    file = open('numbers.txt', 'r')
    
    # Read first line with two numbers
    line1 = file.readline().strip()
    num1_str, num2_str = line1.split()
    num1 = float(num1_str)
    num2 = float(num2_str)

    # Read second line with the operation
    operation = file.readline().strip()

    # Calculate based on the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero!")
            exit()
        result = num1 / num2
    else:
        print("Error: Unsupported operation!")
        exit()

    print("Result:", result)

except FileNotFoundError:
    print("Error: File not found!")
except ValueError:
    print("Error: Invalid numbers in the file!")
