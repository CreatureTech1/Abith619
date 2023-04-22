n = 5
num = 15
for i in range(n):
    for j in range(n-i, 0, -1):
        print(" ", end="")
    for j in range(i+1):
        print(num, end=" ")
        num=num-1
    print(" ")

"""
     15  
    14 13  
   12 11 10  
   9 8 7 6  
  5 4 3 2 1  
"""