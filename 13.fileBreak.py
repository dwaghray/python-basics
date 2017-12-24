# gets a file name from the user to open, read, and close it
# will continue to ask for input until the user inputs "STOP"

while True:
    file_name = input("Please enter a file name or STOP: ")

    if file_name.upper() == "STOP":
        break

    file = open(file_name, "r")
    lines = file.readlines()
    file.close()

    print(file_name, "has", len(lines), "lines of data in it!\n")
