# adds up the numbers in an imported text file

text_file = open("numbers.txt", "r")
lines = text_file.readlines()
text_file.close()

for i in range(len(lines)):
    lines[i] = int(lines[i])

print("The total is:", sum(lines))
