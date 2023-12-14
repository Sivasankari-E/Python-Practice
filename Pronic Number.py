n = int(input("Enter a number: "))
f = 0
for i in range(n):
    if i * (i + 1) == n:
        f = 1
        break

if f==1:
    print("Pronic number")
else:
    print("Not a Pronic number")