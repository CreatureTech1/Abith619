n=5
for i in range(n):
    for j in range (i+1):
        if j % 2 == 0:
            print("0", end=' ')
        else:
            print("1",end=' ')
    print()

"""
0 
0 1 
0 1 0 
0 1 0 1 
0 1 0 1 0 
"""