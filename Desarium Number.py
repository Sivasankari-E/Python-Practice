n=input()
s=0
l=len(n)
for i in range(0,l):
  s+=(int(n[i])**(i+1))
if(s==int(n)):
   print("yes")
else:
   print("no")