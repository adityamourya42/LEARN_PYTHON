rows = int(input("Enter the numbers of rows:"))
cols = int(input("Enter the numbers of colums:"))
for i in range(1, rows+1):
    for j in range(1, cols+1):
        print(f"{i*j:4}", end = " ")
    print("")