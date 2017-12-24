import os

# prints out a list of all text files (files with the .txt extension) that
# are in the current directory

contents = os.listdir(os.getcwd())

text_list = []

for item in contents:
    if item[-4:] == ".txt":
        text_list.append(item)

print("Current directory's text files:\n", text_list)
