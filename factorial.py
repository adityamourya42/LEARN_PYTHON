n = int(input())
fact = 1
if n < 0:
  print("Factorial for negative numbers does not exit")
elif n == 1 or n == 0:
  print(n)
else:
  i = 1
  while(i<=n):
    fact = fact * i
    i += 1
  print(fact)