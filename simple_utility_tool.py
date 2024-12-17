# simple_utility_tool.py
import time

def greet_user():
    print("👋 Hello! Welcome to my Simple Utility Tool.")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}! Let's get started.\n")

def calculator():
    print("📊 Quick Math Calculator")
    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Choose an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operation == "+":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif operation == "-":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif operation == "*":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif operation == "/":
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operation. Please try again!")
    except Exception as e:
        print(f"Error: {e}. Please input valid numbers.")

def farewell():
    print("\n✨ Thank you for using this tool. Have a great day ahead!")

# Main Function
if __name__ == "__main__":
    greet_user()
    calculator()
    farewell()
    time.sleep(1)
