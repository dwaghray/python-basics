# takes numbers from the user until they input "STOP" and prints the sum

total = 0

num = input("Please enter a number or STOP: ")

while num.upper() != "STOP":
    total += int(num)
    num = input("Please enter a number or STOP: ")

print("The total sum is", total)
