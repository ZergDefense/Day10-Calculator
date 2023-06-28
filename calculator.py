import calc_art


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(calc_art.logo)
    num1 = float(input("What's the first number?: "))

    need_to_continue = True

    while need_to_continue:

        for operation in operations:
            print(operation)

        operation = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        function = operations[operation]

        result = function(num1, num2)
        first_run = False
        print(f"{num1} {operation} {num2} = {result}")

        go_forward = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation.: ")

        if go_forward == "y":
            num1 = result
        else:
            need_to_continue = False
            calculator()

calculator()
