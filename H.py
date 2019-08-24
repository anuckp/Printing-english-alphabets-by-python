n=int(input("enter"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==int(n/2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
