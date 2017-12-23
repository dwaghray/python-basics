# print the number of times a character appears in a string:

lowercase = input("Please enter a string in lowercase: ")
letter = input("What letter are you looking for? ")
count = 0
for char in lowercase:
    if char == letter:
        count += 1
        
print("I found", letter, count, "times!")


# or use the .count() method

lowercase = input("Please enter a string in lowercase: ")
letter = input("What letter are you looking for? ")

print("I found", letter, lowercase.count(letter), "times!")



# print the position of the letter in a string:

lowercase = input("Please enter a string in lowercase: ")
letter = input("What letter are you looking for? ")

for i in range(len(lowercase)):
    if lowercase[i] == letter:
        print(letter, "found at position", i)
        
print(letter, "was found", lowercase.count(letter), "times!")



# remove the vowels in a string:
    
text = input("Please enter some text: ")
newString = ""
for char in text:
    if char not in "aeiou":
        newString += char
print("Your text with the vowels removed:", newString)
        
        

