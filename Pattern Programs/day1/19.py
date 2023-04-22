n=5
for i in range(n):
    for j in range(n, 1, -1):
        if i==j:
            print("*", end=' ')
        else:
            print(j, end=" ")

    print()

"""
5 4 3 2 
5 4 3 2 
5 4 3 * 
5 4 * 2 
5 * 3 2 
"""