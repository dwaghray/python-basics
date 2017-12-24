# copies the contents of a file to another file

def copy_file(from_file, to_file):
    
    with open(from_file, "r") as f:
        lines = f.readlines()

    with open(to_file, "w") as f:
        f.writelines(lines)

#testcode
file_f = input("Please enter the name of the file to copy FROM: ")
file_t = input("Please enter the name of the file to copy TO: ")
copy_file(file_f, file_t)
