l=[int(input()) for _ in range(10)];
for n in l:
 t=n;s=0
 while t>0:
  d=t%10;s+=d**3;t//=10
 if s==n:print(n)