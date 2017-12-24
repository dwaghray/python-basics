# counts the number of words in a user input and displays the longest
# word in the entire message by breaking it into a list of words

message = input("Please enter a message: ")

wordList = message.split()

longest = ""

for word in wordList:
    if len(word) > len(longest):
        longest = word
        
print("That message had", len(wordList), "words.")
print("The longest word was:", longest)
