movies = ["Battleship", "Spiderman", "Alien", "Captain America","Avatar", "Thor", "Seven"]
marvel_movies = ["Spiderman", "Thor", "Captain America"]

for movie in movies:   # use a different loop variable name
    if movie in marvel_movies:   # check membership
        print(movie)
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)