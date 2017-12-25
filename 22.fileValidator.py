# takes a file name as an argument and loops until it is valid so it can open,
# read, remove any newlines from, and return it

def open_file(filename):

    while True:
        try:
            file = open(filename, "r")
            lines = file.readlines()
            file.close()
        except:
            filename = input("That file name doesn't exist. Please enter a filename: ")
        else:
            break

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    return lines

#main

data = open_file("doesn'texist.txt")
print("The contents of the file:")
print(data)
