# returns a string with "-" around & between each character:

def dasher(message):
    newMessage = ""
    for num in message:
        newMessage += "-" + num
    return newMessage + "-"
    

#main
print(dasher("Hello"))
print(dasher("Greetings"))
print(dasher(dasher("TEST?")))




# returns a string with "-" on either side so that the
# total length of the line is ALWAYS 20:

def dasher2(message):
    if len(message) <= 20:
        if len(message) % 2 == 0:
            dashes = (20 - len(message)) // 2
            message = ("-" * dashes) + message + ("-" * dashes)
        else:
            dashes = (20 - len(message)) // 2
            message = ("-" * dashes) + message + ("-" * dashes) + "-"
    else:
        message = "-------Error--------"
    return message


        
print(dasher2("Hello"))
print(dasher2("Welcome"))
print(dasher2("Super long string test"))



# similar to dasher2 but instead takes the total line length
# as an argument in the function:

def dasher3(message, length=20):
    if len(message) <= length:
        if len(message) % 2 == 0:
            dashes = (length - len(message)) // 2
            message = ("-" * dashes) + message + ("-" * dashes)
        else:
            dashes = (length - len(message)) // 2
            message = ("-" * dashes) + message + ("-" * dashes) + "-"
    else:
        message = "-------Error--------"
    return message


        
print(dasher3("Hello", 10))
print(dasher3("Welcome", 15))
print(dasher3("Default"))
