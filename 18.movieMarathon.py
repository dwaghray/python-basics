import random

# uses the movie lists from top100movies and chooses a random listing of movies
# for a marathon, without creating duplicates

movie_file = open("top100moviesAFI.txt", "r")
movies_AFI = set(movie_file.readlines())
movie_file.close()

movie_file = open("top100moviesRT.txt", "r")
movies_RT = set(movie_file.readlines())
movie_file.close()

# | is the union of two sets
all_movies = movies_AFI | movies_RT

movie_num = eval(input("How many movies do you want in your marathon? "))
print("\nYour custom", movie_num, "movie marathon:")

shuffled = list(all_movies)
random.shuffle(shuffled)

for i in range(movie_num):
    print(shuffled[i], end = '')

