def perform_operation(num1: float, num2: float, operation: str):
   
    if operation == 'add':
        return float(num1 + num2)
    
    elif operation == 'subtract':
        return float(num1 - num2)
    
    elif operation == 'multiply':
        return float(num1 * num2)
    
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return float(num1 / num2)
    
    else:
        return "Error: Invalid operation. Choose from 'add', 'subtract', 'multiply', or 'divide'."

