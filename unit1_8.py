s=input();
v=sum(1 for c in s.lower() if c in 'aeiou');
print(v,len(s),s[::-1],s.replace('a','@'),s==s[::-1])