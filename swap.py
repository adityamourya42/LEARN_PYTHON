a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Before swapping: a =", a, "b =", b)
temp = 0
temp = a
a = b
b = temp
print("After swapping: a =", a, "b =", b)

#explaining the code:
# The code takes two integers as input from the user
# After that, it prints the values of a and b before swapping
#Then, create a temporary variable called temp and assign the value of a to it
#Next, assign the value of b to a and the value of temp to b
#Finally, it prints the values of a and b after swapping
