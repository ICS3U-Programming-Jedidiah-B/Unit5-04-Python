# input
def calculate(operator_input, number1, number2):

    # process

    # addition
    if operator_input == "+":
        equation = number1 + number2
        return equation
    # subtraction
    elif operator_input == "-":
        equation = number1 - number2
        return equation
    # multiplcation
    elif operator_input == "*":
        equation = number1 * number2
        return equation
    # divison
    elif operator_input == "/":
        equation = number1 / number2
        return equation
    # remainder
    elif operator_input == "%":
        equation = number1 % number2
        return equation
    else:
        equation = "nothing"
        return equation


def main():
    # values
    number1 = 0
    number2 = 0
    # input
    try:
        operator_input = input("Enter an operator ex..'+' '%' '/' '-' '*' : ")
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
    except ValueError:
        print("Please enter a integer")
    # call functions
    calculate(operator_input, number1, number2)
    # solution
    sol = calculate(operator_input, number1, number2)
    if sol != "nothing":
        print("The result of {} {} {} is {}".format(
            number1, operator_input, number2, sol))
    elif sol == "nothing":
        print("Enter a valid operator")


if __name__ == "__main__":
    main()
