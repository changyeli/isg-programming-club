'''
This script serves as the first programming assignment of Python workshop.
In this script, you are asked to complete the blank lines to implement the required features, including
    - addition
    - subtraction
    - multiplication
    - division
        - the result as int
        - the result as float
        - the modules
    - equal
    - 
More specifically, replace None to appropriate operations
You can assume that both two user-defined numbers are integers
'''
def add(num1, num2):
    """
    return addition between two numbers,
    return the addtion

    :param num1: the first number
    :type num1: int
    :param num2: the second number
    :type num2: int
    """
    return None


def subtract(num1, num2):
    """
    return subtracting between two numbers

    :param num1: the first number
    :type num1: int
    :param num2: the second number
    :type num2: int
    """
    return None


def multiply(num1, num2):
    """
    return multilication between two numbers

    :param num1: the first number
    :type num1: int
    :param num2: the second number
    :type num2: int
    """
    return None


def divide_with_int(num1, num2):
    """
    return the divition between two numbers, which the result returns as an integer

    :param num1: the first number
    :type num1: int
    :param num2: the second number
    :type num2: int
    """
    return None


def divide_with_float(num1, num2):
    """
    return the division between two numbers, which the result returns as a float

    :param num1: the first number
    :type num1: int
    :param num2: the second number
    :type num2: int
    """
    return None


def divide_with_module(num1, num2):
    """
    return the divition between two numbers, which the result returns the module of the operations

    :param num1: the first number
    :type num1: int
    :param num2: the second number
    :type num2: int
    """
    return None


def is_equal(num1, num2):
    """
    check if two numbers are equal,

    :param num1: the first number
    :type num1: int
    :param num2: the second number
    :type num2: int
    """
    return None


if __name__ == "__main__":
    while True:
        print("Welcome to the simple Python calculator!")
        print("We offer the following functions:")
        print("1. addition")
        print("2. subtraction")
        print("3. multiplication")
        print("4. division, result as int")
        print("5. division, result as float")
        print("6. division, returns the module")
        print("7. check if two numbers are equal")
        print("8. exit the program")
        choice = int(input("Enter choice (1/2/3/4/5/6/7/8): "))
        if choice in range(1, 8):
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            if choice == 1:
                res = add(num1, num2)
            elif choice == 2:
                res = subtract(num1, num2)
            elif choice == 3:
                res = multiply(num1, num2)
            elif choice == 4:
                res = divide_with_int(num1, num2)
            elif choice == 5:
                res = divide_with_float(num1, num2)
            else:
                res = divide_with_module(num1, num2)
            print("The result is {}".format(res))
        elif choice == 8:
            print("Thanks for using this calculator!")
            break
        else:
            raise ValueError("Invalid input.")
