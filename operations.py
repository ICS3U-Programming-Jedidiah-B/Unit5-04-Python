# input 
def calculate(operation_input,number1,number2):
 
    
    # process
    
    # addition 
    if operation_input == "+": 
        equation = number1 + number2
        return equation
    # subtraction 
    elif operation_input == "-":
        equation = number1 - number2 
        return equation
    # multiplcation 
    elif operation_input == "*":
        equation = number1 * number2 
        return equation 
    # divison 
    elif operation_input == "/":
        equation = number1 / number2 
        return equation 
    # remainder
    elif operation_input == "%":
        equation = number1 % number2 
        return equation 
    else: 
        print("invalid operation, enter a operation")
def main():
    # values 
    number1 = 0
    number2 = 0 
    # input 
    try: 
        operation_input = input("enter an operation: ")
        number1 = int(input("enter a number: "))
        number2 = int(input("enter a number again: ")) 
    except ValueError: 
        print("please enter a integer")
    # call functions 
    calculate(operation_input,number1,number2) 
    
    end = calculate(operation_input,number1,number2)
    
    print("the result of {} {} {} is {}".format(number1, operation_input,number2, end))

if __name__ == "__main__":
            main() 