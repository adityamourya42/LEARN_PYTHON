movie_name = "   deadpool & wolverine    "
print(movie_name.islower())
print(movie_name.isupper())
print(movie_name.upper())
print(movie_name.lower())
web_series_name = "FLASH"
print(web_series_name.isupper())
print(web_series_name.lower())
print(web_series_name.islower())
p=movie_name.strip()
print(p)
print(movie_name.replace("wolverine", "spiderman"))
movie_characters = "deadpool&spider-man&hulk"
p1=movie_characters.split("&")
print("#".join(p1))
movie = "spider-man, iron-man, hulk"
print(movie.startswith("spi"))
print(movie.endswith('lk'))
dc_characters = "flash, superman,arrow"
print(dc_characters.find("arrow"))
print(dc_characters.find("hulk"))
print(dc_characters.count("a"))
print(web_series_name.capitalize())
dc = "superman & batman"
print(dc.title())