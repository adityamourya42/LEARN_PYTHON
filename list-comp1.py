even = [num for num in range(21) if num %2 == 0]
print(even)
odd = [num for num in range(22) if num % 2 != 0]
print(odd)
numbers = [1,2,3,4,5,6]
res = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(res)