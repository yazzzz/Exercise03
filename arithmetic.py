def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by 0!"
    else:
        return float(num1) / float(num2)

def square(num1):
    return num1 * num1

def cube(num1):
    return num1 ** 3

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    if num2 == 0:
        return "Cannot divide by 0!"
    else:
        return num1 % num2
