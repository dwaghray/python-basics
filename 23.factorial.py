# prints the factorial of a number

def factorial(num):
    if num == 1:
        return 1
    else:
        return factorial(num - 1) * num

print("5! =", factorial(5))




