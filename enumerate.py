movies = ["Avengers", "Avengers - 1", "Avengers - 2"]
print(list(enumerate(movies)))

for index, movie in enumerate(movies):
    print(f"{index}: {movie}")
