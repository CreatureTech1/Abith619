n=5
for i in range(n):
    for j in range(n, -i, -1):
        print(i+1, end=" ")
    for j in range(-n, -i, -1):
        print(j+1, end="")
    print()