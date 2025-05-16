def add(n1, n2):
    return n1 + n2
# TODO 1: Write out the other 3 functions subtract, multiply and divide
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
 # TODO 2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
# TODO 3 use the dictionary operations to perform calculations
def calculator():
    should_accumulate = True
    num1=float(input("What is the first number? "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("Pick an operation: ")
        num2=float(input("What is the next number? "))

        result = operations[operation_symbol](num1, num2)
        print(f"The result of {num1} {operation_symbol} {num2} = {result}")
        choice=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if choice=="y":
            num1=result
        else:
            should_accumulate = False
            calculator()

calculator()