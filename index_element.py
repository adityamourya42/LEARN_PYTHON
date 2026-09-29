marvel_movies = ["Avengers", "Avengers-2", "Avengers-3"]
index = 0
for movie in marvel_movies:
    print(f"{index} {movie}")
    index+=1
print(list(enumerate(marvel_movies)))
for index, movies in enumerate(marvel_movies):
    print(f"Index {index} and  {movies}")
print("-" * 30)
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}')

developer = ["naomi", "dario", "jessica","tom"]
ids = [1,2,3,4]
print(list(zip(developer, ids)))