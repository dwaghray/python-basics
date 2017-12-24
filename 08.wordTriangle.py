# takes a message as user input and prints it out in a "triangle"
# shape with one character added on to a new line


message = input("Please enter a message: ")
for i in range(len(message) + 1):
    print(message[:i])

