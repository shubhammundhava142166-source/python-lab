def f(a,b,op):
 return a+b if op=='+' else a-b if op=='-' else a*b if op=='*' else a/b
print(f(float(input()),float(input()),input()))