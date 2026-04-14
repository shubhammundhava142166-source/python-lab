add=lambda a,b:a+b
sub=lambda a,b:a-b
mul=lambda a,b:a*b
div=lambda a,b:a/b
a=float(input());b=float(input());op=input();print(add(a,b) if op=='+' else sub(a,b) if op=='-' else mul(a,b) if op=='*' else div(a,b))