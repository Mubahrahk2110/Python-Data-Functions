def calculator(num1, num2):
    operator = input("Enter the operator (+, -, *, /): ").strip()

    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2

    raise ValueError("Invalid operator. Please choose +, -, *, or /.")


def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = calculator(num1, num2)
    except ValueError as error:
        print(f"Error: {error}")
    except ZeroDivisionError as error:
        print(f"Error: {error}")
    else:
        print(f"The result is: {result:g}")


if __name__ == "__main__":
    main()