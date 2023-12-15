n=int(input())
for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(0,i+1):
        print(j+1,end="")
    t=i
    for j in range(0,i):
        print(t,end="")
        t-=1
    print()