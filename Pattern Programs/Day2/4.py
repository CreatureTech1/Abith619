n=5
for i in range(n):
    for j in range(i):
        print(n-i, end=" ")
    print()
    for j in range(n-i):
        print(j+1, end=" ")
    print()

