# set up the mad lib with placeholders marked with "_"
mad_lib = """
---------------------------------------------------------------------
In the book War of the _noun1_, the main character is an anonymous
_occupation_ who records the arrival of _animals_ in _place_.
Needless to say, havoc reigns as the _animals_ continue to _verb_
everything in sight, until they are killed by the common _noun2_.
---------------------------------------------------------------------
"""

# get input from the user - tell them what it needs to be!

pluralNoun = input("Please enter a plural noun: ")
occupation = input("Please enter an occupation: ")
pluralAnimal = input("Please enter a plural word for an animal: ")
place = input("Please enter a place: ")
verb = input("Please enter a verb: ")
secondNoun = input("Please enter a second noun: ")

# replace all of the placeholders with user input.
# the first noun and the place need to have their
# first letters capitalized

mad_lib = mad_lib.replace("_noun1_", pluralNoun.title()) \
          .replace("_occupation_", occupation) \
          .replace("_animals_", pluralAnimal) \
          .replace("_place_", place.title()) \
          .replace("_verb_", verb) \
          .replace("_noun2_", secondNoun)

# print the resulting mad lib
print(mad_lib)
