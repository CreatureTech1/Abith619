n = 7
for i in range(5):
    for j in range(5-i):
        print(i+1, end=' ')
    k=n-j
    print()
for i in range(0, i+1):
    # for l in range(0, i):
    #     print("*", end=' ')
    for m in range(0, i):
        print(n-m, end=' ')
    print()
    
"""
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 

7 
7 6 
7 6 5 
7 6 5 4 
"""