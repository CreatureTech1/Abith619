n = 6
for i in range(n):
    for j in range(n-i-1):
        print(j+1, end=" ")
    print()

"""
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1
"""