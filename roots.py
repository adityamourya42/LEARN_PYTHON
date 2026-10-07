import math
a = int(input("Enter a first number in equation : "))
b = int(input("Enter a second number in equation : "))
c = int(input("Enter a third number in equation : "))
d = pow(b,2) - 4*a*c
if d < 0:
    print("Roots are imaginary")
else:
    root1 = (-b + pow(d, 0.5)) / (2*a)
    root2 = (-b - pow(d, 0.5)) / (2*a)
    print("Roots are real")
    print(math.floor(root1), math.floor(root2))