# Temperature conversion program

# get input from the user
temp = eval(input("Please enter a temperature: "))

# ask the user what conversion they would like
unitsCorF = input("Would you like that converted to C or F? ")

# do our calculations
tempCtoF = ((9/5.0) * temp) + 32
tempFtoC = (temp - 32) * (5.0/9)

# display the results
if unitsCorF in ("C", "F"):
    if unitsCorF == "C":
        print("The converted temperature is", tempFtoC, "C.")
    else:
        print("The converted temperature is", tempCtoF, "F.")
else:
    print("You didn't enter C or F! ")
