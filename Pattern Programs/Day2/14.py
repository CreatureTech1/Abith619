n=5
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(n-i-1, -1, -1):
        print(n-j, end=" ")
    print()
    for j in range(i, -1, -1):
        print(n-j, end=" ")
    print()