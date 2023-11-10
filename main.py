import CalculatorModule

first_number = input("Please enter first number>>> ")
second_number = input("Please enter second number>>> ")
operation = input("Will you add, subtract, multiply or divide? ")

first_number = float(first_number)
second_number = float(second_number)
operation = operation.lower()

if operation == "add":
    result = CalculatorModule.add(first_number,second_number)
    print(f"Your result: {result}")
elif operation == "subtract":
    result = CalculatorModule.subtract(first_number,second_number)
    print(f"Your result: {result}")
elif operation == "multiply":
    result = CalculatorModule.multiply(first_number,second_number)
    print(f"Your result: {result}")
elif operation == "divide":
    result = CalculatorModule.divide(first_number,second_number)
    print(f"Your result: {result}")