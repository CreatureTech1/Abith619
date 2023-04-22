n = 5
for i in range(5):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(i*2+1):
        print(j+1, end=" ")
    print()

"""
        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9
"""