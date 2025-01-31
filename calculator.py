def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b
def exponentiate(a, b):
    return a ** b
def main():
    print("Welcome to the Python Calculator!")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+ or - or * or / or ^): ")

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    elif operation == "^":
        result = exponentiate(num1, num2)
    else:
        print("Invalid operation!")
        return

    print(f"The result of {num1} {operation} {num2} is: {result}")

if __name__ == "__main__":
    main()