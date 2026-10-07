n = int(input("Enter a number: "))
sum = 0
for i in range(n+1):
    p = pow(i,3)
    sum += p
print(sum)