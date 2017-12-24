# compares top 100 movie lists from the American Film Institute (AFI) and
# Rotten Tomatoes (RT) to alphabetically print which movies appear in both

movie_file = open("top100moviesAFI.txt", "r")
movies_AFI = set(movie_file.readlines())
movie_file.close()

movie_file = open("top100moviesRT.txt", "r")
movies_RT = set(movie_file.readlines())
movie_file.close()

print("The movies on both lists are:")

for movie in sorted(movies_AFI & movies_RT):
    print(movie.strip())

