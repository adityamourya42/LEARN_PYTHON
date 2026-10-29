marvel_characters = ["Spider-man", "Losis" ,"Iron Man", "Bane", "Thor", "Nightwing"]
dc_characters = ["Batman", "Supeman", "Jimmy", "Losis" ,"Lex","Nightwing", "Bane", "Joker"]
def separater(name):
    if name in dc_characters:
        return name
print(filter(separater, marvel_characters))