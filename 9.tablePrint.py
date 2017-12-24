# formats data to be printed in a tabulated format

def table_print(headers, data, width):
    output = "{0:>" + str(width) + "} {1:>" + str(width) + "}"

    print(output.format(headers[0], headers[1]))

    print("-" * (width + 1) * 2)

    for item in data:
        print(output.format(item[0], item[1]))
    print()

#main - Don't change this part!
labels = ["Name", "Score"]
scores = [("Abe", 200), ("Bill", 180), ("Mary", 215)]

table_print(labels, scores, 6)

labels2 = ["Capital", "State"]
state_data = [("Atlanta", "GA"), ("Boise", "ID"), ("Boston", "MA"), ("Austin", "TX")]

table_print(labels2, state_data, 8)
