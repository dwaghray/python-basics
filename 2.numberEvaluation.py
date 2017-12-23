# Number evauluation program

# get input from the user
number = eval(input("Please enter a number: "))

# determine if the number is odd, even, or not a whole number
if number % 2 == 0:
    print("Even number detected.")
elif number % 2 == 1:
    print("Odd number detected.")
else:
    print("Brace yourself - that's not a whole number!")

