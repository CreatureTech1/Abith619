n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(i, -1, -1):
        print(j+1, end=" ")
    print()

"""
        1 
      2 1 
    3 2 1 
  4 3 2 1 
5 4 3 2 1
"""