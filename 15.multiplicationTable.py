# prints out a 10x10 multiplication table - row by row, then column by column
# NOTE: adjust the size of the shell window to fit the table correctly


# rows
for i in range(11):

    # columns
    for j in range(11):

        if (i == 0) and (j == 0):
            print("\t *", end = "")

        elif (i == 0) or (j == 0):
            print("\t", i + j, end = "")

        else:
            print("\t", i * j, end = "")

    print()
