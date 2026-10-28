emp = ["John", "Jane", "Jim"]
id = [123,555, 453]
for name, id in zip(emp, id):
    print("Name: {}, ID: {}".format(name,id))

movies = ["Avengers", "Avengers - 1", "Avengers - 2"]
for index, movie in zip(range(len(movies)), movies):
    print("Index: {}, Movie: {}".format(index, movie))