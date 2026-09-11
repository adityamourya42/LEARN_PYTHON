developer = ["Alice", 25, ["Python", "Rust"]]
print(developer)
print(developer[2])

developer1 = ["Alice", 34, "Java Developer"]
name, age, job = developer1
print(name)
print(age)
print(job)

developer2 = ["MOURYA", 22, "Student"]
name, *rest = developer2
print(name)
print(rest)